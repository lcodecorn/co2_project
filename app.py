import json
import pandas as pd
import plotly.express as px
import streamlit as st

#App config
st.set_page_config(
    page_title="Global CO₂ Explorer",
    layout="wide"
)

st.markdown("""
<style>
/* Hide header anchor links */
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🌍 Global CO₂ Emissions Explorer")
st.caption("Interactive visualization of global emissions, energy use, and economic indicators")



@st.cache_data
def load_data():
    try:
        with open("Data/clean_data.csv", "r", encoding="utf-8") as f:
            df = pd.read_csv(f)
    except UnicodeDecodeError:
        with open("Data/clean_data.csv", "r", encoding="latin-1") as f:
            df = pd.read_csv(f)
    return df

@st.cache_data
def load_geojson():
    # open geojson with explicit encoding
    try:
        with open("Data/world.geo.json", "r", encoding="utf-8") as f:
            geojson = json.load(f)
    except UnicodeDecodeError:
        with open("Data/world.geo.json", "r", encoding="latin-1") as f:
            geojson = json.load(f)
    return geojson

df = load_data()
world_geo = load_geojson()

#Sidebar controls
st.sidebar.header("Controls")

year = st.sidebar.slider(
    "Select year",
    int(df["year"].min()),
    int(df["year"].max()),
    int(df["year"].max())
)

metric = st.sidebar.selectbox(
    "Select metric",
    options=list({
        "Energy per capita": "energy_per_capita",
        "Energy per GDP": "energy_per_gdp",
        "Coal CO₂": "coal_co2",
        "Oil CO₂": "oil_co2",
        "Gas CO₂": "gas_co2",
        "Total CO₂": "co2_total",
        "Total Fossil CO₂": "co2_fossils"
        }.keys())
)

metric_map = {
    "Energy per capita": "energy_per_capita",
    "Energy per GDP": "energy_per_gdp",
    "Coal CO₂": "coal_co2",
    "Oil CO₂": "oil_co2",
    "Gas CO₂": "gas_co2",
    "Total CO₂": "co2_total",
    "Total Fossil CO₂": "co2_fossils"
    }
metric = metric_map.get(metric)

metric_label_map = {
    "energy_per_capita": "Energy per capita (kWh per person)",
    "energy_per_gdp": "Energy per GDP (kWh per 2017-USD)",
    "coal_co2": "Coal CO₂ emissions (million tonnes)",
    "oil_co2": "Oil CO₂ emissions (million tonnes)",
    "gas_co2": "Gas CO₂ emissions (million tonnes)",
    "co2_total": "Total CO₂ emissions (million tonnes)",
    "co2_fossils": "Fossil fuel CO₂ emissions (million tonnes)",
}

# In your choropleth:
labels={metric: metric_label_map.get(metric, metric.replace("_", " ").title()), "year": "Year"}

# In your titles/legends, use metric_label_map[metric] instead of metric.replace(...)

df_year = df[df["year"] == year]

fig = px.choropleth(
    df_year,
    geojson=world_geo,
    locations="iso_code",
    featureidkey="properties.iso_a3_eh",
    color=metric,
    hover_data=["year"],
    labels={metric: metric_label_map[metric].title(), "year": "Year"},
    hover_name="country",
    color_continuous_scale="Reds"
)

fig.update_geos(
    fitbounds="locations",
    visible=False
)

fig.update_layout(
    height=600,
    margin={"r":0,"t":0,"l":0,"b":0}
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("📈 Country Trend")

country = st.selectbox(
    "Select a country",
    sorted(df["country"].unique())
)

df_country = df[df["country"] == country]

fig_line = px.line(
    df_country,
    x="year",
    y=metric,
    title=f"{country} — {metric_label_map[metric].title()} Over Time",
    color_discrete_sequence=["#FF0000"]
)


st.plotly_chart(fig_line, use_container_width=True)


st.subheader("📊 Data Table")


df_yearly = df_country.groupby("year", as_index=False).sum(numeric_only=True).reset_index(drop=False)

fig_bar = px.bar(
    df_yearly,
    x="year",
    y="Electricity Installed Capacity (MW)",
    labels={"Electricity Installed Capacity (MW)": "Installed Capacity (MW)", "year": "Year"},
    title=f"{country} — Installed Capacity and {metric.replace('_', ' ').title()} Over Time",
    color_discrete_sequence=["#00FF22"]
    )

fig_bar.data[0].name = "Installed Capacity (MW)"
fig_bar.data[0].showlegend = True

if metric:
    line_trace = px.line(df_yearly, x="year", y=metric, color_discrete_sequence=["#FF0000"]).data[0]
    line_trace.name = metric_label_map[metric].title()
    line_trace.showlegend = True
    fig_bar.add_trace(line_trace)

fig_bar.update_layout(
    height=500, 
    margin={"r":0,"t":30,"l":0,"b":0},
    showlegend=True
)

st.plotly_chart(fig_bar, use_container_width=True)