import streamlit as st
import plotly.express as px
from pathlib import Path
from backend import get_data


st.header("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
cache = st.checkbox("use cache")
if place:
    try:
        data, dates = get_data(place, days, option, use_cache=cache, update_cache=True)
        match option.lower():
            case 'temperature':
                labels = dict(x='Date', y='Temperature (C)')
                figure = px.line(x=dates, y=data, labels=labels)
                st.plotly_chart(figure, use_container_width=True)
            case 'sky':
                image_files = dict(
                    Clear='clear.png',
                    Clouds='cloud.png',
                    Rain='rain.png',
                    Snow='snow.png'
                )
                images = [f'images/{image_files[condition]}' for condition in data]
                st.image(images, caption=dates, width=90)
    except KeyError:
        st.error(f'the city {place} does not exist.')
