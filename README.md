# Global CO₂ Emissions Explorer

An interactive data visualization dashboard to explore global CO₂ emissions, renewable energy capacity, and economic indicators by country and year.

**Hypothesis**: Countries with higher renewable energy production capacity tend to have lower CO₂ emissions.

This project uses real-world data from **Our World in Data** and **IRENA** (International Renewable Energy Agency), presented through an interactive **Streamlit + Plotly** dashboard.

---

## Features

- **Interactive world map** with choropleth visualization
- **Year slider** to explore temporal changes
- **Country-level trend analysis** for selected metrics
- Compare emissions, GDP, energy indicators, and renewable capacity
- Cleaned and processed datasets ready for analysis

---

## Project Structure

```
CO2_project/
│
├── Data/
│   ├── owid-co2-data.csv          # Raw CO₂ emissions dataset
│   ├── clean_data.csv              # Cleaned & processed data
│   └── world.geo.json              # World map geometry (GeoJSON)
│
├── Notebook/
│   ├── import_clean_data.ipynb     # Data cleaning & preprocessing
│   └── vis.ipynb                   # Exploratory analysis & visualizations
│
├── app.py                          # Streamlit application
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## How to Run the App Locally

### 1. Clone the repository

```bash
git clone https://github.com/lcodecorn/CO2_project.git
cd CO2_project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## Data Sources

- [Our World in Data - CO₂ Emissions Dataset](https://data360.worldbank.org/en/dataset/OWID_CB)
- [IRENA - Renewable Capacity Statistics 2025](https://www.irena.org/Publications/2025/Mar/Renewable-capacity-statistics-2025)

---

## Tech Stack

- **Python** - Core programming language
- **pandas** - Data loading and manipulation
- **Plotly** - Interactive charts and maps
- **Streamlit** - Web application framework
- **GeoJSON** - Country boundaries for mapping

---

## Project Goals

- Practice working with real-world country-level panel data
- Build interactive visualizations for data storytelling
- Present environmental and economic indicators in a clear, accessible way
- Explore the relationship between renewable energy capacity and CO₂ emissions
- Create a reproducible, portfolio-ready data project

---

## Future Improvements

- [ ] Add per-capita and intensity-based metrics
- [ ] Cluster countries by emissions profiles using machine learning
- [ ] Implement emissions trend forecasting
- [ ] Deploy the app publicly using Streamlit Cloud
- [ ] Add statistical analysis of renewable energy vs. emissions correlation

---

## Author

**Léo Souris**

---

## License

This project is open source and available under the [MIT License](LICENSE).