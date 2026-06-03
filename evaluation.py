import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def run_evaluation():
    st.header("📊 Model Evaluation & Mathematical Validation Dashboard")
    st.markdown("---")

    # Guard clause checking if a model has been run during this session
    if "metrics_available" not in st.session_state or not st.session_state["metrics_available"]:
        st.info("📂 No active evaluation data found in session memory. Please navigate to the 'Demand Forecasting' tab and upload a dataset first to populate this analytical dashboard.")
        return

    # Extract metrics from cross-module state cache
    scope_title = st.session_state["scope_title"]
    test_df = st.session_state["eval_test_df"]
    forecast_test = st.session_state["eval_forecast_test"]
    mae = st.session_state["mae"]
    rmse = st.session_state["rmse"]
    mape = st.session_state["mape"]

    st.subheader(f"🎯 Validation Summary: {scope_title}")
    st.markdown("These error metrics are computed using an **80/20 out-of-sample data validation holdout split** to accurately assess predictive accuracy before deploying models to active production environments.")

    # High-impact metric display cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Mean Absolute Error (MAE)", value=f"{mae:.2f} kWh", 
                  help="The average absolute deviation between model predictions and actual grid load.")
    with col2:
        st.metric(label="Root Mean Squared Error (RMSE)", value=f"{rmse:.2f} kWh", 
                  help="Measures error magnitude. Penalizes larger outlier prediction errors more heavily.")
    with col3:
        st.metric(label="Mean Absolute Percentage Error (MAPE)", value=f"{mape:.2f}%", 
                  help="The average relative percentage deviation. Lower values indicate tighter mathematical fit.")

    st.markdown("---")

    # --- CHART 1: ACTUAL VS PREDICTED COMPASS ---
    st.subheader("📈 Model Tracking Fidelity: Actual vs. Predicted Validation Window")
    
    comparison_df = pd.DataFrame({
        "Date": test_df["ds"],
        "Actual Load": test_df["y"].values,
        "Predicted Load": forecast_test["yhat"].values
    })
    
    fig_track = px.line(comparison_df, x="Date", y=["Actual Load", "Predicted Load"],
                        title="Out-of-Sample Performance Alignment (20% Holdout Data Slices)",
                        color_discrete_sequence=["#38bdf8", "#f43f5e"])
    fig_track.update_layout(template="plotly_dark", yaxis_title="Load (kWh)", legend_title="Data Stream")
    st.plotly_chart(fig_track, use_container_width=True)

    # --- CHART 2: RESIDUAL ERROR HISTOGRAM ---
    st.subheader("🧠 Model Bias Assessment: Residual Error Distribution")
    st.markdown("Residual analysis determines if our machine learning model is biased. A perfectly optimized model exhibits a tight, symmetric Gaussian (normal distribution) bell curve centered cleanly around **0**.")

    # Calculate errors: Actuals minus Predictions
    comparison_df["Residuals"] = comparison_df["Actual Load"] - comparison_df["Predicted Load"]

    fig_res = px.histogram(comparison_df, x="Residuals", nbins=15,
                           title="Residual Errors Frequency Distribution Profile ($\epsilon = Y - \hat{Y}$)",
                           color_discrete_sequence=["#10b981"], marginal="rug")
    
    # Add a static vertical reference line exactly at zero error
    fig_res.add_vline(x=0, line_dash="dash", line_color="#ffffff", annotation_text="Zero Error Line", annotation_position="top left")
    fig_res.update_layout(template="plotly_dark", xaxis_title="Error Deviation Magnitude (kWh)", yaxis_title="Frequency Count")
    st.plotly_chart(fig_res, use_container_width=True)