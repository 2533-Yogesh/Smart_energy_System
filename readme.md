⚡ Energy Demand Forecasting & Theft Detection System

An AI-powered web application that performs:

📈 Energy Demand Forecasting

🚨 Energy Theft (Anomaly) Detection

📊 Interactive Data Visualization

Built using Streamlit, Scikit-learn, Pandas, and Matplotlib.

🚀 Project Overview

This application allows users to:

Upload electricity consumption data (CSV or Excel)

Forecast future energy demand

Detect suspicious consumption patterns (possible theft)

Visualize trends using multiple chart options

The system integrates both forecasting and anomaly detection into a single interactive web application.

🏗️ Project Structure
energy-demand-system/
│
├── app.py                # Main Streamlit app
├── forecasting.py        # Demand forecasting module
├── theft_detection.py    # Energy theft detection module
├── requirements.txt      # Project dependencies
└── README.md
📦 Technologies Used

Python

Streamlit

Pandas

NumPy

Scikit-learn

Matplotlib

OpenPyXL (for Excel support)

📊 Features
📈 Demand Forecasting

Time-series based forecasting

Predicts future energy demand

Displays forecast results with visual comparison

Supports CSV and XLSX files

Required columns:

Date
Demand_MW
🚨 Energy Theft Detection

Uses anomaly detection (Isolation Forest)

Identifies abnormal consumption patterns

Highlights suspicious readings

Visual flags for easy identification

Required columns:

Date
Consumption
📊 Visualization Options

Users can switch between:

Line Chart

Bar Chart

Scatter Plot

⚙️ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/your-username/energy-demand-theft-system.git
cd energy-demand-theft-system
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Running the Application
streamlit run app.py

Then open in browser:

http://localhost:8501
🌐 Deployment

This project can be deployed using:

Streamlit Community Cloud

Render

Local Server

Make sure requirements.txt is included before deployment.

🧠 How It Works
Forecasting Module

Reads time-series data

Processes date column

Applies ML-based forecasting

Generates future demand predictions

Theft Detection Module

Trains Isolation Forest model

Detects statistical anomalies

Flags suspicious consumption values

🎯 Use Cases

Electricity Boards

Smart Meter Monitoring

Utility Companies

Energy Analytics Research

Academic Projects

📌 Future Improvements

Add user authentication

Add database storage

Model persistence (.pkl)

Advanced forecasting (LSTM / ARIMA)

Dashboard enhancements

Multi-consumer support

👨‍💻 Author

Developed as an AI-based Energy Analytics project integrating forecasting and anomaly detection.

📜 License

This project is open-source and available for educational and research purposes.