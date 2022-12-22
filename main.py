import streamlit as st
import plotly.express as px
from backend import get_data
st.header("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

d, t = get_data(place, days, option)
labels = dict(x='Date', y='Temperature (C)')
figure = px.line(x=d, y=t, labels=labels)
st.plotly_chart(figure, use_container_width=True)
