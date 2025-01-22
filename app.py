import streamlit as st
import joblib
import numpy as np
import pandas as pd

def predict(data):
    """Making prediction

    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data

    Returns:
        str: Prediction result (Good, Standard, or Poor)
    """
    result = model.predict(data)
    prediction_mapping = {
        0: "Dropout",
        1: "Enrolled",
        2: "Graduate"
    }
    final_result = prediction_mapping[result[0]]
    return final_result


model = joblib.load('/content/sample_data/lr_model.joblib')
feature = ['Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade', 'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 'Tuition_fees_up_to_date', 'Scholarship_holder', 'Curricular_units_2nd_sem_enrolled', 'Curricular_units_1st_sem_enrolled', 'Admission_grade', 'Displaced', 'Previous_qualification_grade', 'Application_mode', 'Gender', 'Debtor', 'Age_at_enrollment']
col1, col2 = st.columns([6, 1])
with col1:
    st.header('Student Performance Prediction', anchor=False)
data = pd.DataFrame()
col1, col2, col3 = st.columns(3)
with col1:
  Curricular_units_1st_sem_approved = st.number_input('Curricular units 1st sem approved', min_value=0)
  Curricular_units_2nd_sem_approved = st.number_input('Curricular units 2nd sem approved', min_value=0)
  Tuition_fees_up_to_date = st.number_input('Tuition fees up to date', min_value=0)
  Scholarship_holder = st.number_input('Scholarship holder', min_value=0)
  Admission_grade = st.number_input('Admission grade', min_value=0.0)
  Previous_qualification_grade = st.number_input('Previous qualification grade', min_value=0.0)
  Age_at_enrollment = st.number_input('Age at enrollment', min_value=15)

with col2:
  Curricular_units_1st_sem_grade = st.number_input('Curricular units 1st sem grade', min_value=0.0)
  Curricular_units_2nd_sem_grade = st.number_input('Curricular units 2nd sem grade', min_value=0.0)
  Curricular_units_2nd_sem_enrolled = st.number_input('Curricular units 2nd sem enrolled', min_value=0)
  Displaced = st.number_input('Displaced', min_value=0)
  Application_mode = st.number_input('Application mode', min_value=0)
  Gender = st.number_input('Gender', min_value=0)

with col3:
  Curricular_units_1st_sem_enrolled = st.number_input('Curricular units 1st sem enrolled', min_value=0)
  Debtor = st.number_input('Debtor', min_value=0)


data['Curricular_units_2nd_sem_approved'] = [Curricular_units_2nd_sem_approved]
data['Curricular_units_2nd_sem_grade'] = [Curricular_units_2nd_sem_grade]
data['Curricular_units_1st_sem_approved'] = [Curricular_units_1st_sem_approved]
data['Curricular_units_1st_sem_grade'] = [Curricular_units_1st_sem_grade]
data['Tuition_fees_up_to_date'] = [Tuition_fees_up_to_date]
data['Scholarship_holder'] = [Scholarship_holder]
data['Curricular_units_2nd_sem_enrolled'] = [Curricular_units_2nd_sem_enrolled]
data['Curricular_units_1st_sem_enrolled'] = [Curricular_units_1st_sem_enrolled]
data['Admission_grade'] = [Admission_grade]
data['Displaced'] = [Displaced]
data['Previous_qualification_grade'] = [Previous_qualification_grade]
data['Application_mode'] = [Application_mode]
data['Gender'] = [Gender]
data['Debtor'] = [Debtor]
data['Age_at_enrollment'] = [Age_at_enrollment]


with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    st.write("Prediction: {}".format(predict(data)))
