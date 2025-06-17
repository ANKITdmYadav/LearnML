import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Text Input")
name=st.text_input("Enter Name")
if name:
    st.write(f"Hello {name}")

age=st.slider("Select Age",0,100,20)

options=["C","C++","Python"]
choice=st.selectbox("Choose",options)
# already selected one option
if choice:
    st.write(f"You selected {choice}")

uploaded_file=st.file_uploader("choose csv file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
    # df.line_chart(df)
