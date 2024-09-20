import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Hello World')

st.write('*Data Science Course 2024*')

df = pd.read_csv('data/Bastar Craton.csv')

st.dataframe(df)

