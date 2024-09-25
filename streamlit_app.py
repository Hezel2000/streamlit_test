import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('NFDI4Earth Streamlit Test Page')

df = pd.read_csv('data/Bastar Craton.csv')

st.dataframe(df)