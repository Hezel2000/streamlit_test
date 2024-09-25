import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('NFDI4Earth Streamlit Test Page')

df = pd.read_csv('data/Bastar Craton.csv')

fig = plt.figure()
plt.scatter(df['Mg'], df['Si'])
st.pyplot(fig)

st.dataframe(df)

