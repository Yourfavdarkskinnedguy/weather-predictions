#importing needed dependencies
import numpy as np
import streamlit as st
from sklearn.preprocessing import LabelEncoder
import pickle



#loading the model
#loaded_model = pickle.load(open('C:/Users/HP/Desktop/weather/weather_model.sav', 'rb'))
loaded_model = pickle.load(open('weather_model.sav', 'rb'))


def preprocessing(input_data):
    cloud_cover_encoder = LabelEncoder()
    Season_encoder = LabelEncoder()
    Location_encoder = LabelEncoder()
    
    cloud_cover_encoder.fit(['partly cloudy', 'clear', 'overcast', 'cloudy'])
    Season_encoder.fit(['Winter', 'Spring', 'Summer', 'Autumn'])
    Location_encoder.fit(['inland', 'mountain', 'coastal'])
    
    processed_data = []
    
    for feature, value in input_data.items():
        if feature == 'Cloud_Cover':
            processed_data.append(cloud_cover_encoder.transform([value])[0])
        elif feature == 'Season':
            processed_data.append(Season_encoder.transform([value])[0])
        elif feature == 'Location':
            processed_data.append(Location_encoder.transform([value])[0])
        else:
            try:
                processed_data.append(float(value))
            except ValueError:
                processed_data.append(0)
    
    processed_data = np.array(processed_data).reshape(1, -1)
    return processed_data

def main():
    st.title('Weather Forecast')
    
    Temperature = st.text_input('Temperature')
    Humidity = st.text_input('Humidity')
    Wind_Speed = st.text_input('Wind Speed')
    Precipitation = st.text_input('Precipitation')
    Cloud_Cover = st.selectbox('Cloud Cover', ['partly cloudy', 'clear', 'overcast', 'cloudy'])
    Atmospheric_Pressure = st.text_input('Atmospheric Pressure')
    UV_Index = st.text_input('UV Index')
    Season = st.selectbox('Season', ['Winter', 'Spring', 'Summer', 'Autumn'])
    Visibility = st.text_input('Visibility')
    Location = st.selectbox('Location', ['inland', 'mountain', 'coastal'])
    
    if st.button('Weather Prediction'):
        input_data = {
            'Temperature': Temperature,
            'Humidity': Humidity,	
            'Wind_Speed': Wind_Speed,	
            'Precipitation': Precipitation,	
            'Cloud_Cover': Cloud_Cover,	
            'Atmospheric_Pressure': Atmospheric_Pressure,	
            'UV_Index': UV_Index,	
            'Season': Season,
            'Visibility': Visibility,	
            'Location': Location
        }
        
        processed_data = preprocessing(input_data)
        
        predictions = loaded_model.predict(processed_data)
        
        if predictions[0] == 1:
            st.write('The weather will be Rainy')
        elif predictions[0]==0:
            st.write('The weather will be Cloudy')
        elif predictions[0]==3:
            st.write('The weather will be Sunny')
        elif predictions[0]==2:
            st.write('The weather will be snowy')
            
    
if __name__ == '__main__':
    main()
