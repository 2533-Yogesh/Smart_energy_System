import streamlit as st
from forecasting import run_forecasting
from theft_detection import run_theft_detection
from styles import CUSTOM_CSS

# Page Config
st.set_page_config(
    page_title="AI Smart Energy Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("⚡ Smart Grid AI")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Demand Forecasting",
        "Theft Detection"
    ]
)

# Main Title
st.title("⚡ AI-Powered Smart Energy Monitoring Platform")

st.caption(
    "Hybrid AI System for Forecasting & Electricity Theft Detection"
)

st.markdown("---")

# Dashboard Home
if menu == "Dashboard":

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Total Demand</div>
            <div class="metric-value">1250 MW</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Predicted Load</div>
            <div class="metric-value">1340 MW</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Anomalies</div>
            <div class="metric-value">12</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Risk Score</div>
            <div class="metric-value">76%</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("📊 System Overview")

    st.info(
        "Upload energy consumption data to generate AI-powered forecasting and theft detection insights."
    )

# Forecasting Page
elif menu == "Demand Forecasting":
    run_forecasting()

# Theft Detection Page
elif menu == "Theft Detection":
    run_theft_detection()