# SETUP

import streamlit as st
import pandas as pd
import datetime


#-------------------
# CREATE DATA

# Simple dataframe
df = pd.DataFrame({
    'A': [1, 4, 3, 2],
    'B': [10, 20, 30, 40]
    })

#-------------------
# START OF APP

#-------------------
# HEADER

# Title of our app
st.title("Meine erste eigene App")

# Add header
st.header("Mein Header")

# Add a gif from https://giphy.com/

st.markdown("![Alternativtext](https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif)")
  #  https://giphy.com/clips/SCUBroncos-basketball-iVxiBph4TpuVV83kWC)")
st.markdown('_https://giphy.com/clips/SCUBroncos-basketball-iVxiBph4TpuVV83kWC_')
st.markdown(("https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif"))

st.image('hdm-logo.jpg')

#-------------------
# BODY

#-------------------
# Show static DataFrame

st.dataframe(df)


#-------------------
# Bar chart


#sidebar
st.bar_chart(df)


st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")

    age = st.slider('How old are you?', 0, 125, 25)
st.write("I'm ", age, 'years old')
)

add_selectbox = st.sidebar.selectbox(
    "Wie nutzen Sie unsere App?",
("Handy","Computer","Tablet")
)
#slider 
age = st.slider('How old are you?', 0, 125, 25)
st.write("I'm ", age, 'years old')
