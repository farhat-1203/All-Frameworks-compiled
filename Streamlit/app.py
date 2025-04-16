import streamlit as st


# Title of the app
st.title("My Streamlit App")

# Description of the app
st.write("This is a simple Streamlit app.")

# Create a text input field
user_input = st.text_input("Enter some text:")
# Display the input text
st.write("You entered:", user_input)



# The main beauty of this framework is that it allows you to create interactive web applications with Python code only.
# We can use various Streamlit components to create a user-friendly interface.
# For example, we can use sliders, checkboxes, and buttons to create interactive elements.
# There is no need to separately write HTML, CSS, or JavaScript code as Streamlit takes care of that for us.
# But we can view the HTML code by right-clicking on the page and selecting "Inspect" or "View Page Source".



# Example: Create a simple dataframe and display it
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "first column" : [1, 2, 3, 4],
    "second column" : [10, 20, 30, 40]
})
# Display the dataframe
st.write("Here is a simple dataframe:")
st.dataframe(df)


# Example: Create a line chart using the dataframe
st.write("Here is a simple line chart:")
st.line_chart(df)

# we can even save the dataframe that is being displayed (by either line chart or dataset) as a CSV file, PNG file, or PDF file.