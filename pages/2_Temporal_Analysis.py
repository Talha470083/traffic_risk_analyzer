import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("⏰ Temporal Analysis")

@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\User\Desktop\traffic_risk_analyzer\data\processed_accident_data.csv")

df = load_data()

st.subheader("Accidents by Hour")

fig, ax = plt.subplots()
df.groupby("Hour")["Accident"].sum().plot(ax=ax)
st.pyplot(fig)

st.subheader("Accidents by Day of Week")

fig2, ax2 = plt.subplots()
df.groupby("DayOfWeek")["Accident"].sum().plot(kind="bar", ax=ax2)
st.pyplot(fig2)