# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:53:51 2022

@author: amank
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu
#import os


# loading the saved models


diabetes_model = pickle.load(open(
    'C:/Users/amank/OneDrive/Desktop/Multiple Disease Prediction System/Saved Models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(
    'C:/Users/amank/OneDrive/Desktop/Multiple Disease Prediction System/Saved Models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(
    "C:/Users/amank/OneDrive/Desktop/Multiple Disease Prediction System/Saved Models/parkinsons_model.sav", 'rb'))
cancer_model = pickle.load(open(
    "C:/Users/amank/OneDrive/Desktop/Multiple Disease Prediction System/Saved Models/cancer_model.sav", 'rb'))


# sidebar for navigation
with st.sidebar:

    selected = option_menu('DISEASE PREDICTION PORTAL',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction', 'Breast Cancer Detection'],
                           icons=['activity', 'heart', 'person', 'bandaid'],
                           default_index=0)


# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input(
            'Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age')

    with col2:
        sex = st.number_input('Sex')

    with col3:
        cp = st.number_input('Chest Pain types')

    with col1:
        trestbps = st.number_input('Resting Blood Pressure')

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.number_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')

    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.number_input(
            'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.number_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.number_input('MDVP:RAP')

    with col2:
        PPQ = st.number_input('MDVP:PPQ')

    with col3:
        DDP = st.number_input('Jitter:DDP')

    with col4:
        Shimmer = st.number_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.number_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.number_input('Shimmer:APQ5')

    with col3:
        APQ =st.number_input('MDVP:APQ')

    with col4:
        DDA = st.number_input('Shimmer:DDA')

    with col5:
        NHR =st.number_input('NHR')

    with col1:
        HNR =st.number_input('HNR')

    with col2:
        RPDE = st.number_input('RPDE')

    with col3:
        DFA = st.number_input('DFA')

    with col4:
        spread1 = st.number_input('spread1')

    with col5:
        spread2 = st.number_input('spread2')

    with col1:
        D2 = st.number_input('D2')

    with col2:
        PPE = st.number_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict(
            [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

    # code for Breast cancer

if(selected == 'Breast Cancer Detection'):
    st.title('Breast Cancer Detection using ML')
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        meanradius = st.number_input('Mean radius')

    with col2:
        meantexture = st.number_input('Mean texture')

    with col3:
        meanperimeter = st.number_input('Mean Perimeter')

    with col4:
        meanarea = st.number_input('Mean Area')

    with col5:
        meansmoothness = st.number_input('Mean smoothness')

    with col1:
        meancompactness = st.number_input('Mean Compactness ')

    with col2:
        meanconcavity = st.number_input('Mean Concavity')

    with col3:
        meanconcavepoints = st.number_input('Mean Concave points')

    with col4:
        meansymmetry = st.number_input('Mean symmetry')

    with col5:
        meanfractaldimension = st.number_input('Mean fractal dimension')

    with col1:
        radiuserror = st.number_input('Radius error')

    with col2:
        textureerror = st.number_input('texture error')

    with col3:
        perimetererror = st.number_input('Perimeter error')
    with col4:
        areaerror = st.number_input('Area Error')

    with col5:
        smoothnesserror = st.number_input('Smoothness error')

    with col1:
        compactnesserror = st.number_input('Compactness error')

    with col2:
        concavityerror = st.number_input('Concavity error')

    with col3:
        concavepointserror = st.number_input('Concave points error')

    with col4:
        symmetryerror = st.number_input('Symmetry error')

    with col5:
        fractaldimensionerror = st.number_input('Fractal dimension error')

    with col1:
        worstradius = st.number_input('Worst radius')

    with col2:
        worsttexture = st.number_input('Worst Texture')

    with col3:
        worstperimeter = st.number_input('Worst perimeter')

    with col4:
        worstarea = st.number_input('Worst area')

    with col5:
        worstsmoothness = st.number_input('Worst Smoothness')

    with col1:
        worstcompactness =st.number_input('Worst compactness')

    with col2:
        worstconcavity = st.number_input('Worst concavity')

    with col3:
        worstconcavepoints = st.number_input('Worst Concave points')

    with col4:
        worstsymmetry = st.number_input('Worst Symmetry ')

    with col5:
        worstfractaldimension = st.number_input('Worst fractal dimension')

        cancer_diagnosis = ''

        # creating a button for Prediction
        if st.button("Breast Cancer Test Result"):
            cancer_prediction = cancer_model.predict([[meanradius, meantexture, meanperimeter, meanarea, meansmoothness, meancompactness, meanconcavity, meanconcavepoints, meansymmetry, meanfractaldimension, radiuserror, textureerror, perimetererror, areaerror, smoothnesserror,
                                                     compactnesserror, concavityerror, concavepointserror, symmetryerror, fractaldimensionerror, worstradius, worsttexture, worstperimeter, worstarea, worstsmoothness, worstcompactness, worstconcavity, worstconcavepoints, worstsymmetry, worstfractaldimension]])

            if (cancer_prediction[0] == 1):
                cancer_diagnosis = "The person has breast cancer"
            else:
                cancer_diagnosis = "The person does not have breast cancer "

        st.success(cancer_diagnosis)
        

'''
path = "'C:/Users/amank/OneDrive/Desktop/Multiple Disease Prediction System/Saved Models/diabetes_model.sav'"

file_name = os.path.abspath(path)

print(file_name)
        
''' 
        


