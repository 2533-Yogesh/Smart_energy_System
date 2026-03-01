import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest

def run_theft_detection():

    st.header("🚨 Electricity Theft Detection")

    uploaded_file = st.file_uploader(
        "Upload Consumer Data File",
        type=["csv", "xlsx"]
    )

    if uploaded_file:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        if "Date" not in df.columns or "Consumption" not in df.columns:
            st.error("File must contain 'Date' and 'Consumption' columns")
            return

        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values("Date")

        model = IsolationForest(contamination=0.1, random_state=42)
        df["Anomaly"] = model.fit_predict(df[["Consumption"]])

        df["Status"] = df["Anomaly"].apply(
            lambda x: "Suspicious 🚩" if x == -1 else "Normal ✅"
        )

        st.dataframe(df)

        chart_type = st.selectbox(
            "Select Visualization",
            ["Line Chart", "Scatter Plot", "Bar Chart"]
        )

        if chart_type == "Line Chart":
            fig = px.line(df, x="Date", y="Consumption", color="Status")
        elif chart_type == "Bar Chart":
            fig = px.bar(df, x="Date", y="Consumption", color="Status")
        else:
            fig = px.scatter(df, x="Date", y="Consumption", color="Status")

        st.plotly_chart(fig, use_container_width=True)

        st.download_button(
            "Download Detection Results",
            df.to_csv(index=False),
            file_name="theft_detection_results.csv",
            mime="text/csv"
        )