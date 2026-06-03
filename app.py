import streamlit as st
from forecasting import run_forecasting
from theft_detection import run_theft_detection
from evaluation import run_evaluation
from styles import CUSTOM_CSS


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Electra AI - CSPDCL Smart Grid",
    page_icon="⚡",
    layout="wide"
)

# =========================
# LOAD CSS
# =========================
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# =========================
# TOP NAVBAR
# =========================
st.markdown("""
<div class="navbar" style="padding: 15px 0; border-bottom: 2px solid #f1f5f9; margin-bottom: 20px;">
    <div class="nav-left" style="display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 28px;">⚡</span>
        <span style="font-weight: 800; font-size: 26px; color: #0f172a; letter-spacing: -0.5px;">
            Electra <span style="color: #4f46e5;">AI</span>
        </span>
        <span style="background: #e0f2fe; color: #0369a1; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 20px; margin-left: 10px; border: 1px solid #bae6fd;">
            CSPDCL ENTERPRISE INTEGRATION
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# TOP NAVIGATION MENU
# =========================
# Clean, horizontal layout tabs acting as our premium header menu
menu = st.radio(
    "",
    [
        "📊 Dashboard Overview",
        "📈 Demand Forecasting",
        "🚨 Theft Detection",
        "🎯 Model Evaluation"
    ],
    horizontal=True
)

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# DASHBOARD PAGE OVERVIEW
# =========================
if menu == "📊 Dashboard Overview":

    st.markdown("<h1 style='font-size: 38px; font-weight: 800; color: #0f172a; letter-spacing: -1px; margin-bottom: 5px;'>Smart Energy Monitoring Platform</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 16px; margin-top: 0; margin-bottom: 30px;'>Advanced Machine Learning Suite for Automated Power Demand Forecasting & Non-Technical Loss (Theft) Detection.</p>", unsafe_allow_html=True)

    # --- MAIN STATE OVERVIEW KPI CARDS ---
    st.markdown("### 📡 Active Grid Operational Matrix")
    
    # Custom HTML styling injectors that override basic components to mimic high-end enterprise telemetry grids
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card" style="background: white; padding: 24px; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);">
            <div style="color: #64748b; font-size: 12px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase;">Total Active Load</div>
            <div style="color: #0f172a; font-size: 32px; font-weight: 800; margin-top: 5px;">1,250 <span style="font-size: 16px; font-weight: 500; color: #64748b;">MW</span></div>
            <div style="color: #10b981; font-size: 12px; font-weight: 600; margin-top: 8px;">▲ 4.2% vs last week</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card" style="background: white; padding: 24px; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);">
            <div style="color: #64748b; font-size: 12px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase;">Peak Projected Load</div>
            <div style="color: #4f46e5; font-size: 32px; font-weight: 800; margin-top: 5px;">1,340 <span style="font-size: 16px; font-weight: 500; color: #4f46e5;">MW</span></div>
            <div style="color: #64748b; font-size: 12px; font-weight: 500; margin-top: 8px;">Prophet Model Prediction</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card" style="background: white; padding: 24px; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);">
            <div style="color: #64748b; font-size: 12px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase;">Flagged DTR Anomalies</div>
            <div style="color: #ef4444; font-size: 32px; font-weight: 800; margin-top: 5px;">12 <span style="font-size: 16px; font-weight: 500; color: #ef4444;">Nodes</span></div>
            <div style="color: #ef4444; font-size: 12px; font-weight: 600; margin-top: 8px;">⚠️ High-Risk Action Required</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card" style="background: white; padding: 24px; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);">
            <div style="color: #64748b; font-size: 12px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase;">Average Aggregate Risk</div>
            <div style="color: #f59e0b; font-size: 32px; font-weight: 800; margin-top: 5px;">76%</div>
            <div style="color: #64748b; font-size: 12px; font-weight: 500; margin-top: 8px;">Hybrid Score Confidence</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- SYSTEM OVERVIEW ACTION CALL CONTAINER ---
    st.subheader("📋 System Deployment Overview")
    st.info(
        "Welcome to the CSPDCL Electra AI Command Panel. Navigate using the tabs header above to upload live feeder "
        "consumption matrices, view predictive time-series trends, or generate verified consumer threat inspection lists."
    )
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- CORE DESIGN FEATURE INFORMATION MATRIX ---
    st.subheader("🚀 Operational Subsystem Capacities")
    
    c1, c2 = st.columns(2)
    
    with c1:
        with st.container(border=True):
            st.markdown("<h4 style='color:#4f46e5; margin-top:0;'>📈 Smart Demand Forecasting</h4>", unsafe_allow_html=True)
            st.markdown("""
            Uses robust machine learning to analyze substation parameters and schedule loads.
            - **Prophet Engine:** Handles seasonal patterns and macro distribution analysis.
            - **Trend Slicing:** Tracks time-series data at the Feeder and Transformer (DTR) level.
            - **Grid Outlook:** Provides a 7-day outlook to safely manage operational demand peaks.
            """)

    with c2:
        with st.container(border=True):
            st.markdown("<h4 style='color:#ef4444; margin-top:0;'>🚨 Theft & Anomaly Core</h4>", unsafe_allow_html=True)
            st.markdown("""
            Uses unsupervised models to spot unexpected power drops and reduce non-technical losses.
            - **Isolation Forest Model:** Isolates anomalous consumption drops from normal usage.
            - **Local Outlier Factor (LOF):** Cross-verifies anomalies against local peer group behavior.
            - **Hybrid Risk Scoring:** Blends model results with local transformer baselines to reduce false alarms.
            """)

# =========================
# FORECASTING PAGE TRIGGER
# =========================
elif menu == "📈 Demand Forecasting":
    run_forecasting()

# =========================
# THEFT DETECTION PAGE TRIGGER
# =========================
elif menu == "🚨 Theft Detection":
    run_theft_detection()

# =========================
# MODEL EVALUATION PAGE TRIGGER
# =========================
elif menu == "🎯 Model Evaluation":
    run_evaluation()