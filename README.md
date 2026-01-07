# Global CO₂ Emissions Explorer

H1 Plus la capacité de production d'energie renouvelable est haute plus les emissions de co2 d'un pays diminue

An interactive data visualization app to explore global CO₂ emissions, energy use, and economic indicators by country and year.

This project uses real-world data from **Our World in Data** and presents it through an interactive **Streamlit + Plotly** dashboard.

---

## Features

- **Interactive world map** (choropleth)
- **Year slider** to explore changes over time
- **Country-level trends** for selected metrics
- Compare emissions, GDP, and energy indicators
- Cleaned and processed dataset

---

## Project Structure

CO2_project/
│
├── Data/
│ ├── owid-co2-data.csv # raw dataset
│ ├── clean_data.csv # cleaned & processed data
│ └── world.geo.json # world map geometry
│
├── Notebook/
│ ├── import_clean_data.ipynb # data cleaning & preprocessing
│ └── vis.ipynb # exploratory analysis & plots
│
├── app.py # Streamlit application
├── requirements.txt
└── README.md



## How to Run the App Locally

### 1️ Clone the repository
Data Source
https://data360.worldbank.org/en/dataset/OWID_CB
https://www.irena.org/Publications/2025/Mar/Renewable-capacity-statistics-2025


git clone https://github.com/lcodecorn/CO2_project.git
cd CO2_project.git

2️ Install dependencies
bash
Copier le code
pip install -r requirements.txt

3️ Run the Streamlit app
bash
streamlit run app.py
The app will open automatically in your browser.

Tech Stack
Python

pandas – data loading and manipulation

Plotly – interactive charts and maps

Streamlit – web application framework

GeoJSON – country boundaries for mapping

Project Goals
Practice working with real-world country-level panel data

Build interactive visualizations for data storytelling

Present environmental and economic indicators in a clear, accessible way

Create a reproducible, recruiter-friendly data project

Possible Future Improvements
Add per-capita and intensity-based metrics

Cluster countries by emissions profiles

Forecast emissions trends

Deploy the app publicly using Streamlit Cloud

Author
Léo Souris