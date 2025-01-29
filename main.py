import streamlit as st

st.Page("main.py",title='Weather APP')

st.title('Weather forcast for the next days')
place = st.text_input("Place: ")
days = st.slider('Forcast Days', min_value=1, max_value=5,
                 help="Select the number of forcasted days")

options = st.selectbox('Select data to view', ("Temperature", "Sky"))
st.subheader(f"{options} for the next {days} days in {place}")