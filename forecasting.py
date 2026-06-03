import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error

def validate_cspdcl_schema(df):
    """
    Acts as a security filter. Checks the uploaded DataFrame for format errors,
    missing information, or impossible electrical readings before running ML.
    """
    is_valid = True
    error_messages = []
    
    # Check 1: Do the exact columns exist?
    required_columns = ["Feeder_ID", "DTR_ID", "Consumer_No", "Date", "Consumption_kWh"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        is_valid = False
        error_messages.append(f"Missing required columns: {missing_columns}. Please check your column headers.")
        return is_valid, error_messages 
        
    # Check 2: Are there blank or empty cells (NaNs)?
    total_nulls = df[required_columns].isnull().sum().sum()
    if total_nulls > 0:
        is_valid = False
        error_messages.append(f"Dataset contains {total_nulls} blank or missing values. Clean the data before uploading.")
        
    # Check 3: Are there negative numbers in consumption? 
    negative_values = (df["Consumption_kWh"] < 0).sum()
    if negative_values > 0:
        is_valid = False
        error_messages.append(f"Data Entry Error: Found {negative_values} rows with negative consumption values. This is physically impossible.")
        
    # Check 4: Is the consumption column actually full of numbers?
    if not pd.api.types.is_numeric_dtype(df["Consumption_kWh"]):
        is_valid = False
        error_messages.append("Data Type Error: The 'Consumption_kWh' column must contain purely numbers, not text or characters.")
        
    return is_valid, error_messages


@st.cache_data
def load_forecast_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    df["Date"] = pd.to_datetime(df["Date"])
    return df.sort_values("Date")

def run_forecasting():
    st.header("📈 CSPDCL Smart Power Demand Forecasting")

    uploaded_file = st.file_uploader("Upload Master Grid Dataset for Forecasting", type=["csv", "xlsx"])

    if uploaded_file is None:
        st.info("📂 Please upload the compiled grid distribution dataset.")
        return

    # --- DEFENSIVE ENTERPRISE GATEWAY START (Indentation Fixed) ---
    try:
        # Load the file using our cached function
        df = load_forecast_data(uploaded_file)
        
        # Pass the data to our security guard function
        is_valid, error_list = validate_cspdcl_schema(df)
        
        # If the security guard finds bugs, display them nicely and STOP execution
        if not is_valid:
            for error in error_list:
                st.error(f"❌ Dataset Validation Failed: {error}")
            return 
            
    except Exception as e:
        # If the file is completely broken or corrupt, catch the crash here
        st.error(f"💥 Critical File Corruption: Could not parse this file. Technical reason: {str(e)}")
        return
    # --- DEFENSIVE ENTERPRISE GATEWAY END ---

    # --- FRONTEND OVERHAUL: MAIN-PAGE FILTERS ---
    st.markdown("### 🌐 Distribution Grid Scope Selection")
    
    # Create two columns side-by-side for a clean web layout
    filter_col1, filter_col2 = st.columns(2)
    
    with filter_col1:
        selected_feeder = st.selectbox("Select Target Feeder Line", df["Feeder_ID"].unique())
    
    # Filter dataset based on the chosen feeder first
    filtered_df = df[df["Feeder_ID"] == selected_feeder]
    
    with filter_col2:
        selected_dtr = st.selectbox("Select Distribution Transformer (DTR)", ["Aggregate Feeder Demand"] + list(filtered_df["DTR_ID"].unique()))

    # Aggregate data based on selection
    if selected_dtr == "Aggregate Feeder Demand":
        forecast_target = filtered_df.groupby("Date")["Consumption_kWh"].sum().reset_index()
        scope_title = selected_feeder
    else:
        forecast_target = filtered_df[filtered_df["DTR_ID"] == selected_dtr].groupby("Date")["Consumption_kWh"].sum().reset_index()
        scope_title = selected_dtr

    forecast_target.columns = ["ds", "y"]

    if len(forecast_target) < 30:
        st.error("At least 30 distinct dates are required to establish a time-series forecast.")
        return

    # --- TRAIN / TEST SPLIT MANAGEMENT (80/20) ---
    train_size = int(len(forecast_target) * 0.8)
    train_df = forecast_target.iloc[:train_size]
    test_df = forecast_target.iloc[train_size:].copy()

    # Fit Model on Training Split
    m_eval = Prophet(yearly_seasonality=False, daily_seasonality=False)
    m_eval.fit(train_df)
    
    # Predict over the Test Set horizon
    future_test = test_df[['ds']].copy()
    forecast_test = m_eval.predict(future_test)

    # Compute Core Mathematical Validation Metrics
    mae = mean_absolute_error(test_df["y"], forecast_test["yhat"])
    rmse = np.sqrt(mean_squared_error(test_df["y"], forecast_test["yhat"]))
    mape = np.mean(np.abs((test_df["y"].values - forecast_test["yhat"].values) / test_df["y"].values)) * 100

    # PUSH METRICS TO GLOBAL SESSION STATE FOR EVALUATION MODULE
    st.session_state["metrics_available"] = True
    st.session_state["eval_test_df"] = test_df
    st.session_state["eval_forecast_test"] = forecast_test
    st.session_state["mae"] = mae
    st.session_state["rmse"] = rmse
    st.session_state["mape"] = mape
    st.session_state["scope_title"] = scope_title

    # --- FULL MODEL FOR FUTURE FORECASTING ---
    final_model = Prophet(yearly_seasonality=False, daily_seasonality=False)
    final_model.fit(forecast_target)
    future_dates = final_model.make_future_dataframe(periods=7)
    forecast_future = final_model.predict(future_dates)

    # Upgraded Metrics Display Card
    st.markdown(f"### 📊 Demand Analytics & 7-Day Outlook: {scope_title}")
    with st.container(border=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("<p style='color:#64748b; font-weight:600; font-size:12px; margin-bottom:-5px; letter-spacing:0.5px;'>CURRENT GRID LOAD</p>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='color:#0f172a; font-weight:800; font-size:36px; margin-top:0;'>{forecast_target['y'].iloc[-1]:,.1f} <span style='font-size:16px; font-weight:500; color:#64748b;'>kWh</span></h2>", unsafe_allow_html=True)
        with c2:
            st.markdown("<p style='color:#64748b; font-weight:600; font-size:12px; margin-bottom:-5px; letter-spacing:0.5px;'>HISTORICAL AVERAGE LOAD</p>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='color:#0f172a; font-weight:800; font-size:36px; margin-top:0;'>{forecast_target['y'].mean():,.1f} <span style='font-size:16px; font-weight:500; color:#64748b;'>kWh</span></h2>", unsafe_allow_html=True)
        with c3:
            st.markdown("<p style='color:#4f46e5; font-weight:700; font-size:12px; margin-bottom:-5px; letter-spacing:0.5px;'>🤖 PROJECTED NEXT-DAY LOAD</p>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='color:#4f46e5; font-weight:800; font-size:36px; margin-top:0;'>{forecast_future['yhat'].iloc[-7]:,.1f} <span style='font-size:16px; font-weight:500; color:#4f46e5;'>kWh</span></h2>", unsafe_allow_html=True)

    # Main Plotly Line Chart
    fig = px.line(forecast_target, x="ds", y="y", title=f"Historical Load Profile vs. AI Outlook")
    fig.add_scatter(x=forecast_future["ds"].tail(7), y=forecast_future["yhat"].tail(7), mode="lines+markers", name="7-Day AI Forecast")
    fig.update_layout(template="plotly_dark", xaxis_title="Timeline", yaxis_title="Consumption (kWh)")
    st.plotly_chart(fig, use_container_width=True)

    # Forecast Dataframe Display
    st.subheader("🔮 Projected Load Values")
    future_preview = forecast_future[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(7)
    future_preview.columns = ["Date", "Predicted Demand (kWh)", "Lower Bound (Safety)", "Upper Bound (Peak)"]
    st.dataframe(future_preview, use_container_width=True)