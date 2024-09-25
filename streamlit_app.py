import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('NFDI4Earth Streamlit Test Page')

df = pd.read_csv('data/Bastar Craton.csv')

elements = df.columns.tolist()[27:]

x_axis_el = st.selectbox('x-axis', elements)
y_axis_el = st.selectbox('y-axis', elements)

fig = plt.figure()
plt.scatter(df[x_axis_el]/10000, df[y_axis_el]/10000)
plt.xlabel(f'{x_axis_el} (wt%)')
plt.ylabel(f'{y_axis_el} (wt%)')
st.pyplot(fig)

st.dataframe(df)

