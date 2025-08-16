import streamlit as st
from weather_forecast_agent import invoke

st.set_page_config(page_title="Weather Forecast 🌦️", layout="centered")
st.title("☀️ Your City Temperature Checker")

city = st.text_input("Enter your city name")

if city:
    with st.spinner("Fetching weather data..."):
        try:
            result = invoke(f"What is the weather in {city}?")
            st.subheader("🌤️ Weather Info")
            st.write(result)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
