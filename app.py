import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import warnings
warnings.filterwarnings("ignore")
from PIL import Image


pickle_in = open("Xgboost.pkl","rb")
classifier=pickle.load(pickle_in)

st.set_page_config(layout="wide")

def welcome():
    return "Welcome All"

def predict(radius_mean, texture_mean, perimeter_mean, area_mean,
       smoothness_mean, compactness_mean, concavity_mean,
       concave_points_mean, symmetry_mean, fractal_dimension_mean,
       radius_se, texture_se, perimeter_se, area_se, smoothness_se,
       compactness_se, concavity_se, concave_points_se, symmetry_se,
       fractal_dimension_se, radius_worst, texture_worst,
       perimeter_worst, area_worst, smoothness_worst,
       compactness_worst, concavity_worst, concave_points_worst,
       symmetry_worst, fractal_dimension_worst):
    
    prediction= classifier.predict([[radius_mean, texture_mean, perimeter_mean, area_mean,
       smoothness_mean, compactness_mean, concavity_mean,
       concave_points_mean, symmetry_mean, fractal_dimension_mean,
       radius_se, texture_se, perimeter_se, area_se, smoothness_se,
       compactness_se, concavity_se, concave_points_se, symmetry_se,
       fractal_dimension_se, radius_worst, texture_worst,
       perimeter_worst, area_worst, smoothness_worst,
       compactness_worst, concavity_worst, concave_points_worst,
       symmetry_worst, fractal_dimension_worst]])
    print(prediction)
    return prediction



def main():
    html_temp = """
    <div style="background-color:grey;padding:10px">
    <h2 style="color:white;text-align:center;"> Benign and Malign Cancer Classification Application </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1], gap="large")
    with col1 :
        st.markdown("### Mean Values")
        radius_mean = st.number_input("radius_mean",)
        texture_mean = st.number_input("texture_mean",)
        perimeter_mean = st.number_input("perimeter_mean",)
        area_mean = st.number_input("area_mean",)
        smoothness_mean = st.number_input("smoothness_mean",)
        compactness_mean = st.number_input("compactness_mean",)
        concavity_mean = st.number_input("concavity_mean",)
        concave_points_mean = st.number_input("concave_points_mean",)
        symmetry_mean = st.number_input("symmetry_mean",)
        fractal_dimension_mean = st.number_input("fractal_dimension_mean")
        
    with col2 :
        st.markdown("### SE Values")
        radius_se = st.number_input("radius_se",)
        texture_se = st.number_input("texture_se",)
        perimeter_se = st.number_input("perimeter_se",)
        area_se = st.number_input("area_se",)
        smoothness_se = st.number_input("smoothness_se",)
        compactness_se = st.number_input("compactness_se",)
        concavity_se = st.number_input("concavity_se",)
        concave_points_se = st.number_input("concave_points_se",)
        symmetry_se = st.number_input("symmetry_se",)
        fractal_dimension_se = st.number_input("fractal_dimension_se",)
        
    with col3 :
        st.markdown("### Worst Values")
        radius_worst = st.number_input("radius_worst",)
        texture_worst = st.number_input("texture_worst",)
        perimeter_worst = st.number_input("perimeter_worst",)
        area_worst = st.number_input("area_worst",)
        smoothness_worst = st.number_input("smoothness_worst",)
        compactness_worst = st.number_input("compactness_worst",)
        concavity_worst = st.number_input("concavity_worst",)
        concave_points_worst = st.number_input("concave_points_worst",)
        symmetry_worst = st.number_input("symmetry_worst",)
        fractal_dimension_worst = st.number_input("fractal_dimension_worst",)
        
    

    result = ""
    if st.button("Predict"):
        result= predict(radius_mean, texture_mean, perimeter_mean, area_mean,
       smoothness_mean, compactness_mean, concavity_mean,
       concave_points_mean, symmetry_mean, fractal_dimension_mean,
       radius_se, texture_se, perimeter_se, area_se, smoothness_se,
       compactness_se, concavity_se, concave_points_se, symmetry_se,
       fractal_dimension_se, radius_worst, texture_worst,
       perimeter_worst, area_worst, smoothness_worst,
       compactness_worst, concavity_worst, concave_points_worst,
       symmetry_worst, fractal_dimension_worst)
        if(result[0]):        
            st.error("It is a malignant (cancerous) tumour")
        else:
            st.success("It is a benign (non-cancerous) tumour")



  

if __name__=='__main__':
    main()
    
    
