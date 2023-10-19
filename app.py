import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('RidgeModel.pkl','rb'))
st.title('Predicting House Sale Value')
st.markdown('Using indicators to determine how much your house should retail for!')
st.header('House Characteristics')
quality = st.slider('House Quality on a scale of 1 to 10 (Very Poor to Excellent)', 1, 10, 1)
bath = st.slider('Number of bathrooms above ground level', 1, 10, 1)
st.subheader("Enter the year the house was built")
year = st.number_input('', 0,2024)
st.subheader("Enter the year the house was remodeled (same as construction year if no remodels)")
year_rem = st.number_input('', 0,2024, key = "remodel")
st.subheader("Enter the living area in square feet")
livarea = st.number_input('', 0,10000, key = "living")
st.subheader("Enter the total basement area in square feet")
bsmt = st.number_input('', 0,10000, key = "basement")
st.subheader("Enter the first floor square feet")
firstflr = st.number_input('', 0,10000, key = "floor")
if st.button("Predict Sale Price"):
             prediction = model.predict(np.array([[quality, bath, year, year_rem, livarea, bsmt, firstflr]]))
             st.text(abs(prediction))
