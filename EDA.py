# ===============================
# Phase 4: Exploratory Data Analysis
# ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Load Cleaned Dataset
df = pd.read_csv(r"C:\Users\User\Desktop\processed_accident_data.csv")
print("Columns in dataset:", df.columns.tolist())

# -----------------------------------
# 1️⃣ Time-Based Accident Analysis
# -----------------------------------

# 'Hour' and 'DayOfWeek' already exist in your dataset
# Map numeric DayOfWeek to names for plotting
day_map = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday',
           4:'Friday', 5:'Saturday', 6:'Sunday'}
df['DayOfWeek_Name'] = df['DayOfWeek'].map(day_map)

plt.figure(figsize=(10,5))
sns.countplot(x='Hour', data=df)
plt.title("Accidents by Hour of Day")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(x='DayOfWeek_Name', data=df,
              order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
plt.title("Accidents by Day of Week")
plt.xticks(rotation=45)
plt.show()

# -----------------------------------
# 2️⃣ Weather Impact (using Weather_Code)
# -----------------------------------

if 'Weather_Code' in df.columns:
    top_weather = df['Weather_Code'].value_counts().head(10)

    plt.figure(figsize=(10,6))
    sns.barplot(x=top_weather.values, y=top_weather.index)
    plt.title("Top 10 Weather Codes During Accidents")
    plt.xlabel("Number of Accidents")
    plt.ylabel("Weather Code")
    plt.show()

# -----------------------------------
# 3️⃣ Traffic Signal Impact
# -----------------------------------

if 'Traffic_Signal' in df.columns:
    plt.figure(figsize=(6,4))
    sns.countplot(x='Traffic_Signal', data=df)
    plt.title("Accidents Near Traffic Signals")
    plt.show()

# -----------------------------------
# 4️⃣ Estimated Speed Limit vs Accident Count
# -----------------------------------

if 'Estimated_Speed_Limit' in df.columns:
    plt.figure(figsize=(10,5))
    sns.countplot(x='Estimated_Speed_Limit', data=df)
    plt.title("Accidents by Estimated Speed Limit")
    plt.xticks(rotation=45)
    plt.show()

# -----------------------------------
# 5️⃣ Simulated Congestion Score
# -----------------------------------

df['Congestion_Score'] = (
    df['Hour'] * 0.6 +
    np.random.normal(0, 1, len(df))
)

plt.figure(figsize=(10,5))
sns.histplot(df['Congestion_Score'], bins=30, kde=True)
plt.title("Simulated Congestion Score Distribution")
plt.show()

# -----------------------------------
# 6️⃣ Geographic Heatmap (Folium)
# -----------------------------------

# Sample to avoid browser crash
sample_df = df.sample(5000, random_state=42)

map_center = [sample_df['Start_Lat'].mean(),
              sample_df['Start_Lng'].mean()]

m = folium.Map(location=map_center, zoom_start=5)

heat_data = list(zip(sample_df['Start_Lat'],
                     sample_df['Start_Lng']))

HeatMap(heat_data).add_to(m)

m.save(" ")

print("Heatmap saved as accident_heatmap.html")
