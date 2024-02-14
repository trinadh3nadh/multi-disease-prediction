
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the models
diabates_model = pickle.load(open("C:/Users/TRINADH/Desktop/stramlit/multi_disease_webapp/saved_models/diabates_model.sav","rb"))

heart_model = pickle.load(open("C:/Users/TRINADH/Desktop/stramlit/multi_disease_webapp/saved_models/heart_model.sav","rb"))
                             
breast_cancer_model = pickle.load(open("C:/Users/TRINADH/Desktop/stramlit/multi_disease_webapp/saved_models/breast_cancer_model.sav","rb"))

                                  
#side bar menu

with st.sidebar:
    selected = option_menu("Multiple Disease Prediction",
                           
                           ["Diabates Prediction",
                            "Heart Disease Predction",
                            "Breast Cancer Prediction"],
                           
                           icons = ["activity","heart","bandaid"],
                           
                           default_index = 0)
    
# diabates prediction page
if (selected=="Diabates Prediction"):
    
    st.title("Diabates Prediction Using ML")
    st.subheader('Creator: Trinadh Kolluboyina')
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    diabates_diagnosis = ""
    
    if st.button("Diabates Test Results"):
        diab_pred = diabates_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_pred[0]==1):
            diabates_diagnosis = "The person is Diabateic"
        else:
            diabates_diagnosis = "The person is not Diabatic"
    st.success(diabates_diagnosis)
    
    
    
    
if (selected=="Heart Disease Predction"):
    #title
    st.title("Heart Disease Prediction Using ML")
    st.subheader('Creator: Trinadh Kolluboyina')
    
    col1,col2 = st.columns(2)
    
    with col1:
        age = st.text_input('Age of the person')
    with col2:
        sex = st.text_input("Sex [M or F]")
    with col1:
        cp = st.text_input('Chest Pain value')
    with col2:
        trestbps = st.text_input('Resting Blood Pressure')
    with col1:
        chol = st.text_input('Cholestral Level')
    with col2:
        fbs = st.text_input('Fasting Blood Sugar')
    with col1:
        restecg= st.text_input('Resting ElectroCardicGraphic Result')
    with col2:
        thalach = st.text_input("Max Heart Rate Achived")
    with col1:
        exang = st.text_input('Exercise Induced Angina')
    with col2:
        oldpeak = st.text_input('Old peak')
    with col1:
        slope = st.text_input('Slope of the peak')
    with col2:
        ca = st.text_input('Ca')
    with col1:
        thal = st.text_input('Thal')
    
    heart_diagnosis = ""
    
    if st.button("Heart Disease Results"):
        heart_pred = heart_model.predict([[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg), int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]])
        
        if(heart_pred[0]==0):
            heart_diagnosis= "The Person Don't Have Heart Disease"
        else:
            heart_diagnosis = "The Person Have Heart Diasease"
    
    st.success(heart_diagnosis)
    
    
    
if (selected=="Breast Cancer Prediction"):
    
    st.title("Breast Cancer Prediction Using ML")
    st.subheader('Creator: Trinadh Kolluboyina') 
    
    col1,col2,col3 = st.columns(3)
    with col1:
       radius_mean = st.text_input("Radius mean")
    with col2:
        perimeter_mean = st.text_input("Perimeter Mean")
    with col3:
        area_mean = st.text_input("Area mean")
    with col1:
        compactness_mean= st.text_input("Compactness mean")
    with col2:
        concavity_mean= st.text_input("Concavity mean")
    with col3:
        concave_points_mean= st.text_input("Concavity Point mean")
    with col1:    
        radius_se = st.text_input("Radius se")
    with col2:    
        area_se = st.text_input("Area se")
    with col3:
        concave_points_se = st.text_input("Concave Points se")
    with col1:
        radius_worst = st.text_input("Radius Worst")
    with col2:
        perimeter_worst = st.text_input("Perimeter Worst")
    with col3:
        compactness_worst = st.text_input("Compactness Worst")
    
    breast_diagnosis = ""
    
    if st.button('Breast Cancer Results'):
        breast_pred = breast_cancer_model.predict([[float(radius_mean),float(perimeter_mean),float(area_mean),float(compactness_mean),float(concavity_mean),float(concave_points_mean),float(radius_se),float(area_se),float(concave_points_se),float(radius_worst),float(perimeter_worst),float(compactness_worst)]])
        
        if(breast_pred[0]==0):
            breast_diagnosis ="The Breast Cancer is Malignant"
        
        else:
            breast_diagnosis ="The Breast Cancer is Benign"
    
    st.success(breast_diagnosis)
    
    
    
    
    
    
    
    
    
    