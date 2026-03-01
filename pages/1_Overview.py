import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Dataset Overview")

@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\User\Desktop\traffic_risk_analyzer\data\processed_accident_data.csv")
df = load_data()

st.subheader("Accident Distribution")

fig, ax = plt.subplots()
df["Accident"].value_counts().plot(kind="bar", ax=ax)
st.pyplot(fig)

st.subheader("Road Type Distribution")

fig2, ax2 = plt.subplots()
df["Road_Type"].value_counts().head(10).plot(kind="bar", ax=ax2)
st.pyplot(fig2)