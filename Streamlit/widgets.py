# Here we'll create a simple form that has options like input fields, slider, drop-down menu, checkboxes, and buttons.
# The form will have a title and a description.


import streamlit as st
import pandas as pd
import numpy as np


st.title("My Streamlit Form")
yourName = st.text_input("Enter your name:")
st.write(f"Hello {yourName}, how are you?")

yourAge = st.slider("Select your age", 0, 100, 20)
st.write(f"You are {yourAge} years old")

yourFavLanguage = st.selectbox("Select your favorite programming language", ["Python", "Java", "C++", "JavaScript"])
st.write(f"Your favorite programming language is {yourFavLanguage}. Good choice!")

# upload a file (CSV, Excel, or image)
uploaded_file = st.file_uploader("Upload your resume", type=["csv", "xlsx", "png", "jpg"])


# Button to submit the form
st.button("Submit")


# for more such interactive elements, you can check out streamlit.io        