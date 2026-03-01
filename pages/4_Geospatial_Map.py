import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🗺 Geospatial Accident Map")

@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\User\Desktop\traffic_risk_analyzer\data\processed_accident_data.csv")

df = load_data()

st.subheader("Accident Locations")

fig = px.scatter_mapbox(
    df.sample(5000),
    lat="Start_Lat",
    lon="Start_Lng",
    color="Accident",
    zoom=3,
    height=600
)

fig.update_layout(mapbox_style="open-street-map")

st.plotly_chart(fig, use_container_width=True)