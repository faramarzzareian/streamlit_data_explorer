import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset Uploader", page_icon=":guardsman:", layout="wide")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.dataframe(data.sample(10))