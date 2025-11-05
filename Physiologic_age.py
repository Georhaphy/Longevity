# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 17:08:24 2025

@author: polas
"""
import streamlit as st 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://img5.pic.in.th/file/secure-sv1/smsk-1e26f337bb6ec6813.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black ; font-size: 25px ;'>Calculate Physiological Age</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black ; font-size: 12px ;'>By Levine PhenoAge Biological Age</h1>", unsafe_allow_html=True)







col1, col2 = st.columns([1,1]) 
with col1:
     st.write("ALbumin(g/dL)")
with col2:
    Alb = st.number_input('##',value = 4.0, step= 0.1 , format="%0.1f" , label_visibility = "collapsed", key =1)

col21, col22 = st.columns([1,1]) 
with col21:
     st.write("Creatinine(mg/dL)")
with col22:
    Cr = st.number_input('##',value = 80 , step= 1 , label_visibility = "collapsed", key =2)
    
col31, col32 = st.columns([1,1]) 
with col31:
     st.write("Glucose(mg/dL)")
with col32:
    Glu = st.number_input('##',value = 80 , step= 1 , label_visibility = "collapsed", key =3)

col41, col42 = st.columns([1,1]) 
with col41:
     st.write("hsCRP(mg/L)")
with col42:
    CRP = st.number_input('##',value = 0.50 , step= 0.10 , format="%0.01f" , label_visibility = "collapsed", key =4)

col51, col52 = st.columns([1,1]) 
with col51:
     st.write("LYM(%)")
with col52:
    LYM = st.number_input('##',value = 60 , step= 1, label_visibility = "collapsed", key =5)

col61, col62 = st.columns([1,1]) 
with col61:
     st.write("MCV(fL)")
with col62:
    MCV = st.number_input('##',value = 80 , step= 1 , label_visibility = "collapsed", key =6)

col71, col72 = st.columns([1,1]) 
with col71:
     st.write("RDW(%)")
with col72:
    RDW= st.number_input('##',value = 13.8 , step= 0.1 , format="%0.1f" , label_visibility = "collapsed", key =7)

col81, col82 = st.columns([1,1]) 
with col81:
     st.write("ALP(%)")
with col82:
    ALP= st.number_input('##',value = 45 , step= 1  , label_visibility = "collapsed", key =8)

col91, col92 = st.columns([1,1]) 
with col91:
     st.write("WBC(cells/µL)")
with col92:
    WBC= st.number_input('##',value = 4500 , step= 100  , label_visibility = "collapsed", key =9)
    
col101, col102 = st.columns([1,1]) 
with col101:
     st.write("Age(years)")
with col102:
    Age = st.number_input('##',value = 42 , step= 1  , label_visibility = "collapsed", key =10)
        
    
    
if st.button("Calculate"):
 
    chrome_options = Options()

    chrome_options.add_argument("--headless=new")

    driver=webdriver.Chrome(options=chrome_options)
    
    driver.get(f"https://www.longevity-tools.com/levine-pheno-age#S-albumin={Alb}&S-creatinine={Cr}&S-glucose={Glu}&S-hsCRP={CRP}&LYM={LYM}&MCV={MCV}&S-ALP={ALP}&WBC={WBC}&age={Age}&RDW={RDW}")
    
    actual_age = driver.find_element("xpath",'/html/body/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]')

    mortal = driver.find_element("xpath",'/html/body/div[2]/div/div[1]/div[2]/div[2]/div[3]/div[2]')
    
    st.write(f"Your estimated biological age = {(actual_age.text.split(' ')[0])} years")
    
    st.write(f"Your change of dying in the next 10 years = {mortal.text.split(' ')[0]} %")


