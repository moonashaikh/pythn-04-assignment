import streamlit as st # type: ignore
import pandas as pd # type: ignore

st.title("BMI CALCULATOR")

height = st.slider("Enter your height (in cm):-" , 100 , 250 , 175)
weight = st.slider("Enter your weight (in kg):-" , 40 , 200 , 70)

bmi = weight /((height/100) ** 2)
st.write(f"Your BMI is {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("-UnderWeight : BMI less than 18.5")
st.write("-Normal Weight : BMI between  18.5 and 24.9")
st.write("-OverWeight : BMI between  25 and 29.9")
st.write("-Obesity Weight : BMI 30 or greater")