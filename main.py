import streamlit as st
import plotly.express as px

st.header("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [days * t for t in temperatures]
    return dates, temperatures


d, t = get_data(days)
labels = dict(x='Date', y='Temperature (C)')
figure = px.line(x=d, y=t, labels=labels)
st.plotly_chart(figure, use_container_width=True)
