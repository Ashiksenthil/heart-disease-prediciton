
import streamlit as st
import numpy as np
import requests


st.title("💓 Heart Disease Prediction App")

st.write("Enter the details below to predict if a patient has heart disease.")


age = st.number_input("Age", min_value=29, max_value=77, value=50)
sex = st.selectbox("Sex", ["Female", "Male"])
cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=90, max_value=200, value=120)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=240)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["False", "True"])
restecg = st.selectbox("Resting ECG Results", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
thalach = st.number_input("Max Heart Rate Achieved", min_value=70, max_value=210, value=150)
exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=6.2, value=1.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
ca = st.slider("Number of Major Vessels (0-3) Colored by Fluoroscopy", min_value=0, max_value=3, value=1)
thal = st.selectbox("Thalassemia Type", ["Normal", "Fixed Defect", "Reversible Defect"])


sex = 1 if sex == "Male" else 0
cp = ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"].index(cp)
fbs = 1 if fbs == "True" else 0
restecg = ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"].index(restecg)
exang = 1 if exang == "Yes" else 0
slope = ["Upsloping", "Flat", "Downsloping"].index(slope)
thal = ["Normal", "Fixed Defect", "Reversible Defect"].index(thal)


if st.button("Predict"):

    input_data = {
        "features": [age, sex, cp, trestbps, chol, fbs, restecg, thalach, oldpeak, slope, ca, thal, exang]
    }

    
    api_url = "https://heart-disease-prediciton.onrender.com/predict"
    response = requests.post(api_url, json=input_data)

    if response.status_code == 200:
        result = response.json()["prediction"]
        st.success(f"Prediction: {result}")
    else:
        st.error("Error connecting to the API. Please try again later.")
