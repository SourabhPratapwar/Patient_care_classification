# 🏥 Patient Care Classification System

This project is a machine learning-based classification system to determine if a patient requires hospitalization (**In Care**) or can be treated at home (**Out Care**), using various blood test parameters. It includes a Jupyter notebook for data analysis and model training, and a Streamlit app for real-time predictions.

---

## 🚀 Why Patient Care Classification?

This system assists medical professionals by offering fast, data-driven insights into patient care needs. It uses historical patient data and a trained Random Forest model to make accurate predictions.

### 🔑 Core Features

* 🔬 **Medical Data Processing**: Analyzes key health metrics such as HAEMOGLOBINS, MCH, MCV, and others.
* 🌲 **Machine Learning Model**: Utilizes a trained Random Forest Classifier.
* ⚙️ **Interactive Prediction UI**: Built with Streamlit for ease of use by healthcare staff.
* 🧪 **Jupyter Notebook**: Offers full exploratory data analysis and model-building steps.
* 🗂️ **Reusable Dataset**: Comes with a sample dataset of patient records (`PatientCare.csv`).

---

## 🛠️ Getting Started

### ✅ Prerequisites

* Python >= 3.7
* pandas, scikit-learn, streamlit, matplotlib, seaborn

---

## 🚦 Usage

### 📊 For Data Analysis & Model Training

```bash
jupyter notebook Patient_Care_Classification.ipynb
```

### 🧠 For Running the Prediction Web App

```bash
streamlit run main.py
```

---

## 📁 Dataset

Included dataset:

* `PatientCare.csv` – Contains medical test records used for training and evaluation.

---

## 🧾 Inputs Used for Prediction

* HAEMATOCRIT
* HAEMOGLOBINS
* ERYTHROCYTE
* LEUCOCYTE
* THROMBOCYTE
* MCH
* MCHC
* MCV
* AGE
* SEX

---

## ⚠️ Disclaimer

This tool is intended for educational or assistive purposes only and should not be used as a sole diagnostic tool without professional consultation.
