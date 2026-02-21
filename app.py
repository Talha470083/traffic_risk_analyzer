import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os  # <-- keep this only once at the top

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="Traffic Accident & Congestion Predictor",
    layout="wide"
)

# -------------------------------
# Load model safely
# -------------------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "traffic_accident_model.pkl")

model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
    except Exception as e:
        st.warning(f"Error loading model: {e}")
else:
    st.warning(f"Model file not found at: {MODEL_PATH}")

# -------------------------------
# Default values for features
# -------------------------------
DEFAULTS = {
    "Start_Lat": 40.0,
    "Start_Lng": -84.0,
    "Visibility(mi)": 10.0,
    "Traffic_Signal": 0,
    "Estimated_Speed_Limit": 30,
    "Hour": 12,
    "DayOfWeek": 0,
    "Month": 1,
    "Road_Type": 0,
    "Weather_Code": 35
}

FEATURES = list(DEFAULTS.keys())

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🚦 Smart Traffic Accident & Congestion Predictor")
st.sidebar.header("Input Traffic & Environmental Features")

inputs = {}
inputs['Start_Lat'] = st.sidebar.number_input("Start Latitude", value=DEFAULTS['Start_Lat'])
inputs['Start_Lng'] = st.sidebar.number_input("Start Longitude", value=DEFAULTS['Start_Lng'])
inputs['Visibility(mi)'] = st.sidebar.slider("Visibility (miles)", 0.0, 20.0, DEFAULTS['Visibility(mi)'])
inputs['Traffic_Signal'] = st.sidebar.selectbox("Traffic Signal Nearby", [0, 1], index=DEFAULTS['Traffic_Signal'])
inputs['Estimated_Speed_Limit'] = st.sidebar.selectbox(
    "Estimated Speed Limit",
    [25, 30, 35, 40, 45, 50, 55, 60, 65],
    index=DEFAULTS['Estimated_Speed_Limit']//5 - 5
)
inputs['Hour'] = st.sidebar.slider("Hour of Day (0-23)", 0, 23, DEFAULTS['Hour'])
inputs['DayOfWeek'] = st.sidebar.selectbox("Day of Week", list(range(7)), index=DEFAULTS['DayOfWeek'])
inputs['Month'] = st.sidebar.slider("Month", 1, 12, DEFAULTS['Month'])
inputs['Road_Type'] = st.sidebar.selectbox("Road Type (0=Local,1=Highway)", [0,1], index=DEFAULTS['Road_Type'])
inputs['Weather_Code'] = st.sidebar.slider("Weather Code", 0, 100, DEFAULTS['Weather_Code'])

# -------------------------------
# Prediction Function
# -------------------------------
def predict(inputs):
    if model is None:
        return None, None, None
    
    df_input = pd.DataFrame([inputs])
    
    # Accident Probability
    accident_prob = model.predict_proba(df_input)[:,1][0]
    accident_pred = model.predict(df_input)[0]
    
    # Simulated Congestion Level (simple heuristic)
    congestion_score = df_input['Hour'][0] * 0.6 + np.random.normal(0, 1)
    if congestion_score < 8:
        congestion_level = "Low"
        action = "No immediate action required."
    elif congestion_score < 15:
        congestion_level = "Medium"
        action = "Monitor traffic, consider minor reroutes."
    else:
        congestion_level = "High"
        action = "Implement traffic control, signal adjustments, or reroutes."
    
    return round(accident_prob, 4), congestion_level, action

# -------------------------------
# Run Prediction
# -------------------------------
if st.button("Predict"):
    accident_prob, congestion_level, action = predict(inputs)
    
    if accident_prob is None:
        st.error("Model not loaded or error in prediction.")
    else:
        st.subheader("Prediction Results")
        st.write(f"**Accident Probability:** {accident_prob}")
        st.write(f"**Predicted Congestion Level:** {congestion_level}")
        st.write(f"**Suggested Action:** {action}")
