import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load(r"D:\District-Level Climate Risk Profiling for Indian Agriculture\risk_model.pkl")# Make sure this file is in same folder

# Set page title
st.set_page_config(page_title="Climate Risk Predictor", layout="centered")

# Title
st.title("🌧️ Climate Risk Prediction App")
st.markdown("Enter normalized rainfall and night-time light to predict risk.")

# Sidebar input sliders
st.sidebar.header("Input Parameters")
rain = st.sidebar.slider("Rainfall (Normalized)", 0.0, 1.0, 0.5, 0.01)
ntl = st.sidebar.slider("NTL (Normalized)", 0.0, 1.0, 0.5, 0.01)

# Predict button
if st.button("Predict Risk Score"):
    input_data = np.array([[rain, ntl]])
    prediction = model.predict(input_data)[0]

    st.subheader(f"Predicted Risk Score: {prediction:.2f}")

    if prediction >= 1.5:
        st.error("High Risk ⚠️")
    elif prediction >= 1.0:
        st.warning("Medium Risk 🟠")
    else:
        st.success("Low Risk 🟢")
