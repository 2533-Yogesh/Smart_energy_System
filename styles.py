CUSTOM_CSS = """
<style>

/* Main App */
.stApp {
    background-color: #0f172a;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #1f2937;
}

/* Titles */
h1, h2, h3 {
    color: white;
    font-weight: bold;
}

/* Metric Cards */
.metric-card {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #334155;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    margin-bottom: 15px;
}

/* Metric Title */
.metric-title {
    font-size: 15px;
    color: #94a3b8;
}

/* Metric Value */
.metric-value {
    font-size: 30px;
    font-weight: bold;
    color: #38bdf8;
}

/* File Uploader */
[data-testid="stFileUploader"] {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 15px;
    border: 1px dashed #475569;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #2563eb, #38bdf8);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 20px;
    font-weight: bold;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 15px;
    overflow: hidden;
}

</style>
"""