import streamlit as st
from forecasting import run_forecasting
from theft_detection import run_theft_detection
from styles import CUSTOM_CSS


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="GridPulse",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# LOAD CSS
# =========================

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# =========================
# TOP NAVBAR
# =========================

st.markdown("""
<div class="navbar">
    <div class="nav-left">
        ⚡ <span>GridPulse</span>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# TOP MENU
# =========================

menu = st.radio(
    "",
    [
        "Dashboard",
        "Demand Forecasting",
        "Theft Detection"
    ],
    horizontal=True
)

st.markdown("---")

# =========================
# DASHBOARD
# =========================

if menu == "Dashboard":

    st.title("⚡ AI-Powered Smart Energy Monitoring Platform")

    st.caption(
        "Hybrid AI System for Forecasting & Electricity Theft Detection"
    )

    st.markdown("---")

    # KPI CARDS

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

    # SYSTEM OVERVIEW

    st.subheader("📊 System Overview")

    st.info(
        "Upload energy consumption data to generate AI-powered "
        "forecasting and theft detection insights."
    )

    st.markdown("---")

    # FEATURES

    st.subheader("🚀 Core Features")

    c1, c2 = st.columns(2)

    with c1:

        st.success("""
        ✅ Smart Demand Forecasting
        
        • Prophet Forecasting  
        • Load Prediction  
        • Trend Analysis  
        • Future Demand Insights
        """)

        st.warning("""
        🚨 Theft Detection
        
        • Isolation Forest ML  
        • Hybrid Risk Scoring  
        • Anomaly Detection  
        • Consumer Classification
        """)

    with c2:

        st.info("""
        📊 Interactive Analytics
        
        • Real-Time Charts  
        • KPI Dashboard  
        • Dynamic Uploads  
        • Smart Monitoring
        """)

        st.error("""
        ⚡ AI Smart Grid
        
        • Energy Analytics  
        • Risk Assessment  
        • Demand Monitoring  
        • Intelligent Insights
        """)

# =========================
# FORECASTING PAGE
# =========================

elif menu == "Demand Forecasting":

    run_forecasting()

# =========================
# THEFT DETECTION PAGE
# =========================

elif menu == "Theft Detection":

    run_theft_detection()
