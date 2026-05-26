import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest


def run_theft_detection():

    st.header("🚨 Smart Electricity Theft Detection")

    # FILE UPLOAD
    uploaded_file = st.file_uploader(
        "Upload Consumer Consumption Dataset",
        type=["csv", "xlsx"]
    )

    # REQUIRE FILE
    if uploaded_file is None:
        st.info("📂 Please upload a consumer dataset.")
        return

    # READ FILE
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # VALIDATE COLUMNS
    if "Date" not in df.columns or "Consumption" not in df.columns:
        st.error(
            "Dataset must contain Date and Consumption columns"
        )
        return

    # PROCESS DATA
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    # ISOLATION FOREST MODEL
    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    df["Anomaly"] = model.fit_predict(
        df[["Consumption"]]
    )

    # STATUS LABELS
    df["Status"] = df["Anomaly"].apply(
        lambda x: "Suspicious 🚩" if x == -1 else "Normal ✅"
    )

    # =========================
    # HYBRID RISK SCORE SYSTEM
    # =========================

    # Average Consumption
    avg_consumption = df["Consumption"].mean()

    # Deviation Percentage
    df["Deviation"] = (
        abs(df["Consumption"] - avg_consumption)
        / avg_consumption
    ) * 100

    # Consumption Factor
    max_consumption = df["Consumption"].max()

    df["Consumption_Factor"] = (
        df["Consumption"] / max_consumption
    ) * 100

    # Anomaly Factor
    df["Anomaly_Factor"] = df["Anomaly"].apply(
        lambda x: 100 if x == -1 else 20
    )

    # Final Hybrid Risk Score
    df["Risk_Score"] = (
        0.5 * df["Anomaly_Factor"]
        + 0.3 * df["Deviation"]
        + 0.2 * df["Consumption_Factor"]
    )

    # RISK CLASSIFICATION
    def classify_risk(score):

        if score >= 70:
            return "High Risk 🔴"

        elif score >= 40:
            return "Medium Risk 🟠"

        else:
            return "Low Risk 🟢"

    df["Risk_Level"] = df["Risk_Score"].apply(
        classify_risk
    )

    # =========================
    # KPI SECTION
    # =========================

    st.subheader("⚡ Theft Detection Analytics")

    suspicious_count = len(
        df[df["Status"] == "Suspicious 🚩"]
    )

    normal_count = len(
        df[df["Status"] == "Normal ✅"]
    )

    avg_consumption_display = df["Consumption"].mean()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Normal Consumers",
            normal_count
        )

    with col2:
        st.metric(
            "Suspicious Consumers",
            suspicious_count
        )

    with col3:
        st.metric(
            "Average Consumption",
            f"{avg_consumption_display:.2f}"
        )

    st.markdown("---")

    # =========================
    # MAIN CONSUMPTION CHART
    # =========================

    st.subheader("📊 Consumption Pattern Analysis")

    fig = px.line(
        df,
        x="Date",
        y="Consumption",
        color="Status",
        title="Electricity Consumption Monitoring"
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
    # ANOMALY SCATTER CHART
    # =========================

    st.subheader("🚩 Suspicious Consumption Detection")

    fig2 = px.scatter(
        df,
        x="Date",
        y="Consumption",
        color="Risk_Level",
        size="Risk_Score",
        hover_data=[
            "Consumption",
            "Risk_Score",
            "Risk_Level"
        ],
        title="AI-Based Anomaly Detection"
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
    # RISK DISTRIBUTION CHART
    # =========================

    st.subheader("⚠ Risk Level Distribution")

    risk_chart = px.histogram(
        df,
        x="Risk_Level",
        color="Risk_Level",
        title="Consumer Risk Classification"
    )

    risk_chart.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font=dict(color="white"),
        title_font_size=22,
        height=450
    )

    st.plotly_chart(
        risk_chart,
        use_container_width=True
    )

    # =========================
    # SUSPICIOUS USERS TABLE
    # =========================

    st.subheader("🚨 Suspicious Consumers")

    suspicious_df = df[
        df["Status"] == "Suspicious 🚩"
    ]

    st.dataframe(
        suspicious_df[
            [
                "Date",
                "Consumption",
                "Risk_Score",
                "Risk_Level",
                "Status"
            ]
        ],
        use_container_width=True
    )

    # =========================
    # AI INSIGHTS SECTION
    # =========================

    st.subheader("🤖 AI Theft Analysis")

    high_risk = len(
        df[df["Risk_Level"] == "High Risk 🔴"]
    )

    medium_risk = len(
        df[df["Risk_Level"] == "Medium Risk 🟠"]
    )

    if high_risk > 0:

        st.error(
            f"{high_risk} high-risk consumers detected. "
            "Possible electricity theft or abnormal meter activity identified."
        )

    elif medium_risk > 0:

        st.warning(
            f"{medium_risk} medium-risk consumers detected. "
            "Further monitoring recommended."
        )

    else:

        st.success(
            "No suspicious activity detected in uploaded dataset."
        )

    # =========================
    # DOWNLOAD BUTTON
    # =========================

    st.download_button(
        "⬇ Download Detection Results",
        df.to_csv(index=False),
        file_name="theft_detection_results.csv",
        mime="text/csv"
    )