#importing needed dependencies

import numpy as np
import streamlit as st
from sklearn.preprocessing import LabelEncoder
import pickle

#loading the model
loaded_model= pickle.load(open('C:/Users/HP/Desktop/weather/weather_model.sav', 'rb'))

def preprocessing(input_data):
    input_data_as_np= np.asarry(input_data)
    input_data_reshaped= input_data_as_np.reshape(1,-1)
    
    
def main():
    st.title('Weather Forecast')    