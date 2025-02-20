
from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


model = joblib.load("heart_disease_model.pkl")

feature_names = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach",
    "oldpeak", "slope", "ca", "thal", "exang"
]  

@app.route("/")
def home():
    return "Heart Disease Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        
        data = request.json
        features = np.array(data["features"]).reshape(1, -1)
        df_input = pd.DataFrame(features, columns=feature_names)

        prediction = model.predict(df_input)[0]

        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
