import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

def run_forecasting():

    st.header("📈 Power Demand Forecasting")

    uploaded_file = st.file_uploader(
        "Upload Demand Data File",
        type=["csv", "xlsx"]
    )

    if uploaded_file:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        if "Date" not in df.columns or "Demand_MW" not in df.columns:
            st.error("File must contain 'Date' and 'Demand_MW' columns")
            return

        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values("Date")

        # Date Filter
        st.sidebar.subheader("Filter by Date")
        start_date = st.sidebar.date_input("Start Date", df["Date"].min())
        end_date = st.sidebar.date_input("End Date", df["Date"].max())

        df = df[(df["Date"] >= pd.to_datetime(start_date)) &
                (df["Date"] <= pd.to_datetime(end_date))]

        st.dataframe(df)

        # Chart Selector
        chart_type = st.selectbox(
            "Select Visualization",
            ["Line Chart", "Bar Chart", "Area Chart", "Scatter Plot"]
        )

        if chart_type == "Line Chart":
            fig = px.line(df, x="Date", y="Demand_MW")
        elif chart_type == "Bar Chart":
            fig = px.bar(df, x="Date", y="Demand_MW")
        elif chart_type == "Area Chart":
            fig = px.area(df, x="Date", y="Demand_MW")
        else:
            fig = px.scatter(df, x="Date", y="Demand_MW")

        st.plotly_chart(fig, use_container_width=True)

        # Forecast
        st.subheader("🔮 7-Day Forecast")

        df["Day"] = np.arange(len(df))
        model = LinearRegression()
        model.fit(df[["Day"]], df["Demand_MW"])

        future_days = np.arange(len(df), len(df) + 7).reshape(-1, 1)
        predictions = model.predict(future_days)

        future_dates = pd.date_range(df["Date"].max() + pd.Timedelta(days=1), periods=7)

        forecast_df = pd.DataFrame({
            "Date": future_dates,
            "Predicted_Demand_MW": predictions
        })

        st.dataframe(forecast_df)

        fig2 = px.line(df, x="Date", y="Demand_MW")
        fig2.add_scatter(
            x=forecast_df["Date"],
            y=forecast_df["Predicted_Demand_MW"],
            mode="lines",
            name="Forecast"
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.download_button(
            "Download Forecast Results",
            forecast_df.to_csv(index=False),
            file_name="forecast_results.csv",
            mime="text/csv"
        )