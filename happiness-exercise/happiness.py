import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('happy.csv')

st.header('In Search for Happiness')

options = ['GDP', 'Happiness', 'Generosity']
optionx = st.selectbox("Select data for X axis", options)
optiony = st.selectbox("Select data for y axis", options)

st.subheader(f"{optionx} and {optiony}")

x = df[optionx.lower()]
y = df[optiony.lower()]

figure = px.scatter(x=x, y=y, labels=dict(x=optionx, y=optiony))
st.plotly_chart(figure, use_container_width=True)
