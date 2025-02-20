# 💓 Heart Disease Prediction Using Machine Learning

##  Project Overview
This project predicts whether a patient has heart disease based on medical data.  
It is an **end-to-end Machine Learning project**, covering **data preprocessing, model training, API deployment, and UI development.**  

✅ **Machine Learning Model** trained using RandomForest & optimized with GridSearchCV  
✅ **Flask API** to serve model predictions  
✅ **Streamlit UI** for an interactive user interface  
✅ **Deployed on Render (API) and Streamlit Cloud (UI)**  

---

##  Tech Stack
This project is built using the following technologies:
| **Component**   | **Technology Used** |
|----------------|--------------------|
| Programming Language | Python |
| Machine Learning | Scikit-learn, XGBoost |
| Web Framework | Flask |
| Frontend UI | Streamlit |
| Model Deployment | Flask API, Render |
| Data Handling | Pandas, NumPy |
| Model Storage | Joblib |

---

##  Dataset
- **Dataset:** [Heart Disease UCI Dataset (Kaggle)](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)  
- **Number of Samples:** 1025  
- **Features Included:**
  - `age` - Age of the patient
  - `sex` - Gender (0 = Female, 1 = Male)
  - `cp` - Chest Pain Type (4 categories)
  - `trestbps` - Resting Blood Pressure (mm Hg)
  - `chol` - Serum Cholesterol (mg/dl)
  - `fbs` - Fasting Blood Sugar > 120 mg/dl (0 = No, 1 = Yes)
  - `restecg` - Resting ECG results (0 = Normal, 1 = ST-T Wave abnormality, 2 = Left Ventricular Hypertrophy)
  - `thalach` - Maximum Heart Rate Achieved
  - `exang` - Exercise-Induced Angina (0 = No, 1 = Yes)
  - `oldpeak` - ST Depression Induced by Exercise
  - `slope` - Slope of the Peak Exercise ST Segment (0 = Upsloping, 1 = Flat, 2 = Downsloping)
  - `ca` - Number of Major Vessels (0-3) Colored by Fluoroscopy
  - `thal` - Type of Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)
  - `target` - 0 = No Heart Disease, 1 = Heart Disease (Label)

---

## 🎯 Features
- **Data Preprocessing**
  - Handled missing values
  - Feature scaling using `StandardScaler`
  - One-hot encoding for categorical variables
- **Machine Learning Model**
  - Tried multiple models (RandomForest, XGBoost, Logistic Regression)
  - Used `GridSearchCV` for hyperparameter tuning
  - Achieved **85%+ accuracy** on validation data
- **Flask API Deployment**
  - Model is served using Flask API
  - Can accept input JSON and return predictions
- **Streamlit UI**
  - Interactive user-friendly web app
  - Users can enter their medical details and get predictions instantly
- **Deployment**
  - **Flask API Deployed on Render** 🌍
  - **Streamlit UI Deployed Online (Optional)** 🎨

---

## How to Run the Project Locally
📌 **Follow these steps to run the project on your local machine.**  

### **1️ Clone the Repository**
```sh
git clone https://github.com/YourGitHubUsername/heart-disease-prediction.git
cd heart-disease-prediction

### **2 Install Dependencies**
```sh
pip install -r requirements.txt

### **3️ Run the Flask API**
```sh
python app.py


### **4 Run the Streamlit UI**
```sh
streamlit run streamlit_app.py
