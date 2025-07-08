# interactive_country_trends_dashboard.py

# 🚀 Streamlit: Global Happiness Country Trends Dashboard
# What it does:
# ✅ Lets users pick multiple countries
# ✅ Shows happiness trends over time using an interactive Plotly line chart
# ✅ Ideal for clean live demo, CV, LinkedIn, and class showcase

import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Global Happiness Country Trends", layout="centered")

# Title
st.title("🌎 Global Happiness Country Trends Dashboard (2015–2019)")

# Load your cleaned merged data
df_all = pd.read_csv('merged_happiness_data.csv')

# Sidebar country multiselect
selected_countries = st.multiselect(
    "Select Countries to Compare:",
    options=sorted(df_all['country'].unique()),
    default=["Norway", "Denmark"]
)

# Filter and plot
if selected_countries:
    df_selected = df_all[df_all['country'].isin(selected_countries)]
    fig = px.line(
        df_selected,
        x='year',
        y='happiness_score',
        color='country',
        markers=True,
        title="Happiness Score Trends (2015–2019) for Selected Countries"
    )
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Happiness Score",
        legend_title="Country"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Please select at least one country to display the trend chart.")
