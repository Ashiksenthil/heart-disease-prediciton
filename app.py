
from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load("heart_disease_model.pkl")

# Define the correct feature names (these must match the features in `X_train`)
feature_names = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach",
    "oldpeak", "slope", "ca", "thal", "exang"
]  # Ensure these match the features used in training!

@app.route("/")
def home():
    return "Heart Disease Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input data
        data = request.json

        # Convert input data into a NumPy array
        features = np.array(data["features"]).reshape(1, -1)

        # Convert NumPy array to Pandas DataFrame with correct column names
        df_input = pd.DataFrame(features, columns=feature_names)

        # Make prediction
        prediction = model.predict(df_input)[0]

        # Convert prediction to human-readable output
        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
