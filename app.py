import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Traffic Accident Analytics Dashboard",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Traffic Accident Analytics Dashboard")

st.markdown("""
This interactive dashboard provides exploratory data analysis of traffic accidents.

### 🔍 What This Dashboard Covers:
- Overview statistics
- Temporal accident patterns
- Weather impact analysis
- Geospatial accident heatmap

Use the sidebar to navigate between pages.
""")

@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Summary")
col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Total Features", len(df.columns))
col3.metric("Accident Rate (%)", round(df["Accident"].mean()*100, 2))
