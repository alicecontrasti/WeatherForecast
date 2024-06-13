import streamlit as st
import pandas as pd

###### CSS BACKGROUND #######################
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2018/06/06/15/06/clouds-3458118_1280.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

st.title("Weather Forecast")

city_name = st.text_input('Inserisci il nome della città:\n')

import requests
API_key = "485a4cca3eb54a50591e4ca9bc473fb0"
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'

result=requests.get(url)
json=result.json()

if city_name:
    
    minima = json['main'].get('temp_min')
    minimaK = round((minima),2)
    minimaC = round((minima - 273.15),2)
    st.write(f'La temperatura minima è:\n\n :blue[{minima} K] - :blue[{minimaC} C]')

    st.divider()

    massima = json['main'].get('temp_max')
    massimaK = round((massima),2)
    massimaC = round((massimaK - 273.15),2)
    st.write(f'La temperatura massima è:\n\n :red[{massimaK} K] -  :red[{massimaC} C]')

    st.divider()

    pressionePSI = json['main'].get('pressure')
    pressioneBAR = round((pressionePSI/14.5),2)
    st.write(f'La pressione atmosferica è di:\n\n :orange[{pressionePSI} psi] - :orange[{pressioneBAR} bar]')
    
    st.divider()    

    umidità = json['main'].get('humidity')
    st.write(f"L'umidità dell'aria' è del:\n\n{umidità}%")

    st.divider()

    clouds = json['weather'][0].get('description')
    st.write(f'Le nuvole oggi:\n\n :grey[{clouds}]')

else:
    st.write(f'Non hai inserito nessuna città')


