import streamlit as st
import pickle
import numpy as np

col1, col2 = st.columns([0.4, 0.6], gap='large')


def load_model():
    with open('model_package_complete.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


with col1:
    st.write("""# Dataset Used""")
    st.write("The Diabetes prediction dataset is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative). The data includes features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. This dataset can be used to build machine learning models to predict diabetes in patients based on their medical history and demographic information. This can be useful for healthcare professionals in identifying patients who may be at risk of developing diabetes and in developing personalized treatment plans. Additionally, the dataset can be used by researchers to explore the relationships between various medical and demographic factors and the likelihood of developing diabetes.")
    st.write(
        "**Project Documentation - [Github Repository](https://github.com/jpedrou/DiabetesML)**")
    st.write("**Made by [@jpedrou](https://github.com/jpedrou)**")


with col2:

    data = load_model()
    rf_over = data['model']
    label_gender = data['encoder_gender']
    label_smoke = data['encoder_smoking']
    scaler = data['scaler']

    st.title('Application for Diabetes Prediction')
    st.write("""#### Please, fill all the fields for better experience.""")

    gender = st.selectbox('Gender', ['Female', 'Male', 'Other'])
    age = st.number_input('Age', 0, 100, 40)
    hyper = st.selectbox('hypertension', ['Yes', 'No'])
    new_hyper = 0
    if hyper == 'Yes':
        new_hyper = 1
    else:
        new_hyper = 0

    hd = st.selectbox('Heart Disease', ['Yes', 'No'])
    new_hd = '0'
    if hd == 'Yes':
        new_hd = 1
    else:
        new_hd = 0

    smoke = st.selectbox('Smoking History', [
        'No Info', 'current', 'ever', 'former', 'never', 'not current'])
    bmi = st.number_input('BMI', 10.1, 80.2, step=None)
    hba = st.number_input('HbA1c Test', 0.0, 50.0, value=5.0, step=None)
    bgl = st.number_input('Blood Glucose Level', 0, 250, value=100)

    st.text("")
    ok = st.button('Predict')
    if ok:
        X = np.array([[gender, age, new_hyper, new_hd, smoke, bmi, hba, bgl]])
        X[:, 0] = label_gender.transform(X[:, 0])
        X[:, 4] = label_smoke.transform(X[:, 4])
        X = scaler.transform(X)

        prediction = rf_over.predict(X)
        if prediction == 0:
            st.success("The pacient will probably not have Diabetes.")
        else:
            st.error("The patient will probably have diabetes.")
