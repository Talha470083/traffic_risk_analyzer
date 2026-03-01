import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌧 Weather Impact on Accidents")

@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\User\Desktop\traffic_risk_analyzer\data\processed_accident_data.csv")

df = load_data()

st.subheader("Accidents by Weather Code")

fig, ax = plt.subplots()
df.groupby("Weather_Code")["Accident"].sum().plot(kind="bar", ax=ax)
st.pyplot(fig)

st.subheader("Visibility vs Accidents")

fig2, ax2 = plt.subplots()
ax2.scatter(df["Visibility(mi)"], df["Accident"], alpha=0.3)
st.pyplot(fig2)