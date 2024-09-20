import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

st.title('Hello World')

st.write('*Data Science Course 2024*')

df = pd.read_csv('data/Bastar Craton.csv')

cat_names = df.columns.tolist()[27:]

el1 = st.selectbox('select element', cat_names = df.columns.tolist()[27:]
)
st.write(el1)

st.dataframe(df)

