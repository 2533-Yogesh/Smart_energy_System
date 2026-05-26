import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet


def run_forecasting():

    st.header("📈 Smart Power Demand Forecasting")

    # =========================
    # FILE UPLOAD
    # =========================

    uploaded_file = st.file_uploader(
        "Upload Demand Dataset",
        type=["csv", "xlsx"]
    )

    # REQUIRE FILE
    if uploaded_file is None:
        st.info("📂 Please upload a demand dataset.")
        return

    # READ FILE
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # =========================
    # VALIDATE DATA
    # =========================

    if "Date" not in df.columns or "Demand_MW" not in df.columns:

        st.error(
            "Dataset must contain Date and Demand_MW columns"
        )

        return

    # =========================
    # PROCESS DATA
    # =========================

    df["Date"] = pd.to_datetime(df["Date"])

    df = df.sort_values("Date")

    # =========================
    # SIDEBAR FILTERS
    # =========================

    st.sidebar.subheader("📅 Filter Data")

    start_date = st.sidebar.date_input(
        "Start Date",
        df["Date"].min()
    )

    end_date = st.sidebar.date_input(
        "End Date",
        df["Date"].max()
    )

    df = df[
        (df["Date"] >= pd.to_datetime(start_date)) &
        (df["Date"] <= pd.to_datetime(end_date))
    ]

    # =========================
    # KPI CARDS
    # =========================

    st.subheader("⚡ Demand Analytics")

    current_demand = df["Demand_MW"].iloc[-1]

    average_demand = df["Demand_MW"].mean()

    peak_demand = df["Demand_MW"].max()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Current Demand",
            f"{current_demand:.2f} MW"
        )

    with col2:

        st.metric(
            "Average Demand",
            f"{average_demand:.2f} MW"
        )

    with col3:

        st.metric(
            "Peak Demand",
            f"{peak_demand:.2f} MW"
        )

    st.markdown("---")

    # =========================
    # DEMAND TREND CHART
    # =========================

    st.subheader("📊 Demand Trend Analysis")

    fig = px.line(
        df,
        x="Date",
        y="Demand_MW",
        title="Power Demand Over Time"
    )

    fig.update_traces(
        line=dict(width=4)
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font=dict(color="white"),
        title_font_size=22,
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =========================
    # PREPARE DATA FOR PROPHET
    # =========================

    prophet_df = df.rename(
        columns={
            "Date": "ds",
            "Demand_MW": "y"
        }
    )

    # =========================
    # TRAIN PROPHET MODEL
    # =========================

    model = Prophet()

    model.fit(prophet_df)

    # =========================
    # CREATE FUTURE DATES
    # =========================

    future = model.make_future_dataframe(
        periods=7
    )

    # =========================
    # GENERATE FORECAST
    # =========================

    forecast = model.predict(future)

    # =========================
    # EXTRACT FORECAST DATA
    # =========================

    forecast_df = forecast[
        ["ds", "yhat"]
    ].tail(7)

    forecast_df.columns = [
        "Date",
        "Predicted_Demand_MW"
    ]

    # =========================
    # FORECAST TABLE
    # =========================

    st.subheader("🔮 7-Day AI Forecast")

    st.dataframe(
        forecast_df,
        use_container_width=True
    )

    # =========================
    # FORECAST VISUALIZATION
    # =========================

    fig2 = px.line(
        df,
        x="Date",
        y="Demand_MW",
        title="Forecast Visualization"
    )

    fig2.add_scatter(
        x=forecast_df["Date"],
        y=forecast_df["Predicted_Demand_MW"],
        mode="lines+markers",
        name="AI Forecast",
        line=dict(width=4)
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font=dict(color="white"),
        title_font_size=22,
        height=500
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # =========================
    # FORECAST COMPONENTS
    # =========================

    st.subheader("📈 Forecast Components")

    fig3 = model.plot_components(
        forecast
    )

    st.pyplot(fig3)

    # =========================
    # AI INSIGHTS
    # =========================

    st.subheader("🤖 AI Energy Insights")

    demand_growth = (
        (
            df["Demand_MW"].iloc[-1]
            - df["Demand_MW"].iloc[0]
        )
        / df["Demand_MW"].iloc[0]
    ) * 100

    forecast_avg = forecast_df[
        "Predicted_Demand_MW"
    ].mean()

    if demand_growth > 0:

        st.success(
            f"Energy demand increased by "
            f"{demand_growth:.2f}% during "
            f"the selected period."
        )

    else:

        st.warning(
            f"Energy demand decreased by "
            f"{abs(demand_growth):.2f}% "
            f"during the selected period."
        )

    st.info(
        f"Predicted average demand for "
        f"next 7 days: "
        f"{forecast_avg:.2f} MW"
    )

    # =========================
    # DOWNLOAD RESULTS
    # =========================

    st.download_button(
        "⬇ Download Forecast Results",
        forecast_df.to_csv(index=False),
        file_name="forecast_results.csv",
        mime="text/csv"
    )