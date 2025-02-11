from tkinter import Place

import streamlit as st
import plotly.express as px
from Backend import get_data

st.title('Weather forcast for the next days')
place = st.text_input("Place: ")
days = st.slider('Forcast Days', min_value=1, max_value=5,
                 help="Select the number of forcasted days")

options = st.selectbox('Select data to view', ("Temperature", "Sky"))

st.subheader(f"{options} for the next {days} days in {place}")


d, t = get_data(Place, days, options)


figure = px.line(x=d, y=t, labels={"x":"Date","y": "Temperature(C)"})
st.plotly_chart(figure)