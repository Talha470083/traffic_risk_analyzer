# ===========================
# Phase 2: Load & Inspect Dataset (Corrected)
# ===========================

import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv(r"C:\Users\User\Desktop\US_Accidents_March23.csv")

# Quick Overview
print("=== Dataset Shape ===")
print(df.shape)

print("\n=== First 5 Rows ===")
print(df.head())

print("\n=== Column Names ===")
print(df.columns)

# Data Types
print("\n=== Data Types ===")
print(df.dtypes)

# Missing Values
print("\n=== Missing Values ===")
missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)
print(missing)

# Inspect Key Features for Our Project

# Latitude & Longitude
print("\nLatitude Sample Values:")
print(df['Start_Lat'].head())
print("\nLongitude Sample Values:")
print(df['Start_Lng'].head())

# Time / Date
print("\nStart Time Sample:")
print(df['Start_Time'].head())

# Weather Condition
print("\nWeather Condition Sample:")
print(df['Weather_Condition'].value_counts().head(10))

# Visibility
print("\nVisibility Sample:")
print(df['Visibility(mi)'].head())

# Road Type / Road Class (inferred)
print("\nRoad Class Sample:")
print(df['Street'].head())

# Traffic Signal Presence
if 'Traffic_Signal' in df.columns:
    print("\nTraffic Signal Sample:")
    print(df['Traffic_Signal'].value_counts())

# Junction Presence
if 'Junction' in df.columns:
    print("\nJunction Sample:")
    print(df['Junction'].value_counts())

# Stop Sign Presence
if 'Stop' in df.columns:
    print("\nStop Sign Sample:")
    print(df['Stop'].value_counts())

# Speed Limit
if 'Speed_Limit' in df.columns:
    print("\nSpeed Limit Sample:")
    print(df['Speed_Limit'].value_counts().head())

# Accident occurrence (already implied)
print("\nAccident Records Check:")
print("Total Accidents:", df.shape[0])

# Optional: Quick summary statistics
print("\n=== Summary Statistics ===")
print(df.describe())
