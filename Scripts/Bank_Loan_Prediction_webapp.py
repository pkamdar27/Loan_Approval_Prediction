# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 12:50:02 2021

@author: pkamd
"""

import numpy as np
from PIL import Image
import pickle
import streamlit as st

model = pickle.load(open("C:/Users/pkamd/Desktop/Priyanka/Data/End - End Project/For GitHub/Loan Prediction/loan_prediction_model.sav", "rb"))


def loan_prediction():
    st.title ("Bank Loan Prediction")
    
    account_number = st.text_input("Account Number")
    full_name = st.text_input("Full Name")
    
    gender_display = ("Female", "Male")
    gender_options = list(range(len(gender_display)))
    gender = st.selectbox("Gender", gender_options, format_func=lambda x: gender_display[x])
    
    marriage_display = ("No", "Yes")
    marriage_options = list(range(len(marriage_display)))
    marriage = st.selectbox("Marital Status", marriage_options, format_func = lambda x:marriage_display[x]) 
    
    dependent_display = ("No", "One", "Two", "More than Two")
    dependent_options = list(range(len(dependent_display)))
    dependent = st.selectbox("Dependents", dependent_options, format_func = lambda x:dependent_display[x]) 
    
    education_display = ("Not Graduate","Graduate")
    education_options = list(range(len(education_display)))
    education = st.selectbox("Education", education_options, format_func = lambda x:education_display[x]) 
    
    employment_display = ("Job", "Bussiness")
    employment_options = list(range(len(employment_display)))
    employment = st.selectbox("Employment Status", employment_options, format_func = lambda x:employment_display[x]) 
    
    
    property_display = ("Rural", "Semi-Urban", "Urban")
    property_options = list(range(len(property_display)))
    property_area = st.selectbox("Property Area", property_options, format_func = lambda x:property_display[x]) 
    
    credit_display = ("Rural", "Semi-Urban", "Urban")
    credit_options = list(range(len(credit_display)))
    credit_score = st.selectbox("Credit Score", credit_options, format_func = lambda x:credit_display[x]) 
    
    monthly_income = st.number_input("Applicant's Monthly Income($)",value=0)
    co_applicant_monthly_income = st.number_input("Co-Applicant's Monthly Income($)",value=0)
    loan_amt = st.number_input("Loan Amount",value=0)
    
    duration_display = ['2 Month','6 Month','8 Month','1 Year','16 Month']
    duration_options = range(len(duration_display))
    duration = st.selectbox("Loan Duration",duration_options, format_func=lambda x: duration_display[x])
    
    if st.button("Submit"):
        loan_duration = 0
        if duration == 0:
            loan_duration = 60
        if duration == 1:
            loan_duration = 180
        if duration == 2:
            loan_duration = 240
        if duration == 3:
            loan_durationn = 360
        if duration == 4:
            loan_durationn = 480
        features = [[gender, marriage, dependent, education, employment, property_area, credit_score, monthly_income, co_applicant_monthly_income, 
                     loan_amt, duration ]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        
        if ans == 0:
            st.error(
                "Hello: " + full_name +" || "
                "Account number: "+account_number +' || '
                'Sorry according to our calculations, you are not eligible to get loan from Bank')
        else:
            st.success(
                "Hello: " + full_name +" || "
                "Account number: "+account_number +' || '
                'Congratulations!! you will get the loan from Bank')

loan_prediction()