import streamlit as st
import plotly.express as px
from Backend import get_data

st.title('Weather forcast for the next days')
place = st.text_input("Place: ")
days = st.slider('Forcast Days', min_value=1, max_value=5,
                 help="Select the number of forcasted days")

options = st.selectbox('Select data to view', ("Temperature", "Sky"))

st.subheader(f"{options} for the next {days} days in {place.title()}")
try:
    if place:

        filtered_data = get_data(place.title(), days)

        if options == 'Temperature':
            temperatures = [dict['main']['temp'] for dict in filtered_data]
            temperatures = [i / 10 for i in temperatures]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x":"Date","y": "Temperature(C)"})
            st.plotly_chart(figure)

        if options == 'Sky':
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            img = {'Clear': 'img/clear.png', 'Clouds': 'img/clouds.png', 'Rain': 'img/rain.png', 'Snow': 'img/snow.png'}

            img_paths = [img[condition] for condition in sky_conditions]
            st.image(img_paths, width=115)
except KeyError:
    st.warning('We could find the place you introduce, please check')
