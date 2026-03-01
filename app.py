import streamlit as st
from forecasting import run_forecasting
from theft_detection import run_theft_detection

st.set_page_config(
    page_title="Smart Energy Monitoring System",
    layout="wide"
)

st.title("⚡ Smart Energy Monitoring & Forecasting System")

menu = st.sidebar.selectbox(
    "Select Module",
    ["Demand Forecasting", "Theft Detection"]
)

if menu == "Demand Forecasting":
    run_forecasting()

elif menu == "Theft Detection":
    run_theft_detection()