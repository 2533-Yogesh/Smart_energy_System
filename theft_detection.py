import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

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

# OPTIMIZATION: Cache file loading to prevent disk reading bottlenecks
@st.cache_data
def load_grid_data(uploaded_file):
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    df["Date"] = pd.to_datetime(df["Date"])
    return df.sort_values("Date")

# OPTIMIZATION: Cache heavy unsupervised learning execution
@st.cache_resource
def execute_anomaly_detection(data_matrix, contamination=0.1):
    model = IsolationForest(n_estimators=200, contamination=contamination, random_state=42)
    predictions = model.fit_predict(data_matrix)
    return predictions

def run_theft_detection():
    st.header("🚨 CSPDCL Smart Grid Theft & Non-Technical Loss Analytics")

    uploaded_file = st.file_uploader("Upload Master Grid Dataset", type=["csv", "xlsx"])

    if uploaded_file is None:
        st.info("📂 Please upload the compiled Feeder/DTR distribution dataset.")
        return

    # --- DEFENSIVE ENTERPRISE GATEWAY START ---
    try:
        # Load the file using our cached function
        df = load_grid_data(uploaded_file)
        
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

    # --- FRONTEND OVERHAUL: INLINE MAIN-PAGE FILTERS ---
    st.markdown("### 🌐 Distribution Grid Scope Selection")
    
    # Create two even columns side-by-side on the main screen
    filter_col1, filter_col2 = st.columns(2)
    
    with filter_col1:
        selected_feeder = st.selectbox("Select Feeder Line", ["All Feeders"] + list(df["Feeder_ID"].unique()))
    
    # Filter dataset based on selected feeder first
    if selected_feeder != "All Feeders":
        filtered_df = df[df["Feeder_ID"] == selected_feeder]
    else:
        filtered_df = df.copy()

    with filter_col2:
        selected_dtr = st.selectbox("Select Distribution Transformer (DTR)", ["All DTRs"] + list(filtered_df["DTR_ID"].unique()))
    
    if selected_dtr != "All DTRs":
        filtered_df = filtered_df[filtered_df["DTR_ID"] == selected_dtr]

    # --- MACHINE LEARNING EXECUTION ---
    consumption_features = filtered_df[["Consumption_kWh"]].values
    
    # Run cached isolation forest
    filtered_df["Anomaly"] = execute_anomaly_detection(consumption_features)
    
    # Standard LOF Comparison Run
    lof = LocalOutlierFactor(n_neighbors=min(20, len(filtered_df)), contamination=0.1)
    filtered_df["LOF_Anomaly"] = lof.fit_predict(consumption_features)

    # --- ADVANCED HIERARCHICAL CO-RELATION HYBRID SCORE ---
    # Step 1: Compute peer baseline average grouped by DTR and Date
    filtered_df["DTR_Baseline_Avg"] = filtered_df.groupby(["DTR_ID", "Date"])["Consumption_kWh"].transform("mean")
    
    # Step 2: Compute deviation from local DTR neighborhood standard deviation
    filtered_df["DTR_Deviation_Pct"] = (abs(filtered_df["Consumption_kWh"] - filtered_df["DTR_Baseline_Avg"]) / filtered_df["DTR_Baseline_Avg"]) * 100

    # Step 3: Compute localized Hybrid Risk Score
    filtered_df["Anomaly_Factor"] = filtered_df["Anomaly"].apply(lambda x: 100 if x == -1 else 15)
    filtered_df["Risk_Score"] = (0.6 * filtered_df["Anomaly_Factor"]) + (0.4 * filtered_df["DTR_Deviation_Pct"])
    filtered_df["Risk_Score"] = filtered_df["Risk_Score"].clip(0, 100)

    # Classify Risk Levels explicitly
    filtered_df["Risk_Level"] = filtered_df["Risk_Score"].apply(
        lambda x: "High Risk 🔴" if x >= 75 else ("Medium Risk 🟠" if x >= 45 else "Low Risk 🟢")
    )
    filtered_df["Status"] = filtered_df["Anomaly"].apply(lambda x: "Suspicious 🚩" if x == -1 else "Normal ✅")

    # --- RENDER DASHBOARD INTERACTIVE STATS ---
    st.subheader(f"⚡ Analytics Overview: {selected_dtr if selected_dtr != 'All DTRs' else 'All Monitored Regions'}")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Active Nodes", len(filtered_df["Consumer_No"].unique()))
    c2.metric("Flagged Suspects (Isolation Forest)", len(filtered_df[filtered_df["Status"] == "Suspicious 🚩"]))
    c3.metric("Peak System Load (kWh)", f"{filtered_df['Consumption_kWh'].max():,.1f}")

    # Visualizations
    st.subheader("📊 Consumption Profile Slices")
    fig = px.line(filtered_df, x="Date", y="Consumption_kWh", color="Consumer_No", 
                  title="Multi-Tenant Load Monitoring Profile", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🚩 Identified Theft Profile Clusters")
    fig2 = px.scatter(filtered_df, x="Date", y="Consumption_kWh", color="Risk_Level", size="Risk_Score",
                      hover_data=["Consumer_No", "DTR_ID"], title="Peer Group Anomaly Multi-Dimensional Grid Mapping")
    st.plotly_chart(fig2, use_container_width=True)

    # Table View
    st.subheader("📋 Actionable Vigilance Report Logs")
    suspicious_table = filtered_df[filtered_df["Risk_Level"] == "High Risk 🔴"].sort_values(by="Risk_Score", ascending=False)
    st.dataframe(suspicious_table[["Date", "Feeder_ID", "DTR_ID", "Consumer_No", "Consumption_kWh", "Risk_Score", "Risk_Level"]], use_container_width=True)