import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Page configuration
st.set_page_config(page_title="Patient Care Classification", layout="centered")

# Load model
@st.cache_resource
def load_model():
    with open("rfmodel.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

# App title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Patient Care Classification System</h1>", unsafe_allow_html=True)
st.markdown("### Provide patient's blood parameters and demographics below:")

# Input form inside expander
with st.expander("🔍 Enter Patient Data"):
    col1, col2 = st.columns(2)

    with col1:
        haem = st.number_input("HAEMATOCRIT")
        hemo = st.number_input("HAEMOGLOBINS")
        ery = st.number_input("ERYTHROCYTE")
        leu = st.number_input("LEUCOCYTE")
        thr = st.number_input("THROMBOCYTE")

    with col2:
        mch = st.number_input("MCH")
        mchc = st.number_input("MCHC")
        mcv = st.number_input("MCV")
        age = st.number_input("AGE")
        sex = st.radio("SEX", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")

# Submit button
if st.button("🔎 Predict Care Requirement"):
    input_data = np.array([[haem, hemo, ery, leu, thr, mch, mchc, mcv, age, sex]])
    columns = ["HAEMATOCRIT", "HAEMOGLOBINS", "ERYTHROCYTE", "LEUCOCYTE",
               "THROMBOCYTE", "MCH", "MCHC", "MCV", "AGE", "SEX"]
    df_input = pd.DataFrame(input_data, columns=columns)

    st.markdown("### 📋 User Input")
    st.dataframe(df_input, use_container_width=True)

    prediction = model.predict(df_input)[0]
    result = "🏠 **Out Care (Home Care) Required**" if prediction == 0 else "🏥 **In Care (Hospitalization) Required**"

    # Display result with style
    st.markdown("---")
    st.markdown("### 🧾 Prediction Result")
    st.markdown(f"<div style='padding: 20px; background-color: #f0f2f6; border-radius: 10px; font-size: 20px; color: #333;'>{result}</div>", unsafe_allow_html=True)
