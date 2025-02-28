import streamlit as st
import pandas as pd


##Title of the application
st.title("Hello Streamlit")

## Display a Simple Text
st.write("This is simple text")

name=st.text_input("Enter Your name",)

if name:
  st.write("Hello "+name)