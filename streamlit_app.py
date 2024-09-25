import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('NFDI4Earth Streamlit Test Page')

df = pd.read_csv('data/Bastar Craton.csv')

elements = df.columns.tolist()[27:]


col1, col2 = st.columns([20, 80])

with col1:
    x_axis_el = st.selectbox('x-axis', elements)
    y_axis_el = st.selectbox('y-axis', elements)

with col2:
    fig = plt.figure()
    plt.scatter(df[x_axis_el]/10000, df[y_axis_el]/10000)
    plt.xlabel(f'{x_axis_el} (wt%)')
    plt.ylabel(f'{y_axis_el} (wt%)')
    st.pyplot(fig)


st.dataframe(df)

tab1, tab2 = st.tabs(['Plot', 'Data'])

with tab1:
    x_axis_el = st.selectbox('x-axis', elements)
    y_axis_el = st.selectbox('y-axis', elements)

with tab2:
    fig = plt.figure()
    plt.scatter(df[x_axis_el]/10000, df[y_axis_el]/10000)
    plt.xlabel(f'{x_axis_el} (wt%)')
    plt.ylabel(f'{y_axis_el} (wt%)')
    st.pyplot(fig)