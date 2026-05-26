CUSTOM_CSS = """
<style>

/* =========================
   GLOBAL
========================= */

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #F8FAFC;
    color: #111827;
}

/* Hide Streamlit UI */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* =========================
   NAVBAR
========================= */

.navbar {
    background: linear-gradient(
        90deg,
        #4F46E5,
        #06B6D4
    );
    padding: 18px 30px;
    border-radius: 18px;
    margin-bottom: 30px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
}

.nav-left {
    color: white;
    font-size: 28px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

/* =========================
   RADIO NAVIGATION
========================= */

div[role="radiogroup"] {
    display: flex;
    gap: 16px;
    margin-bottom: 30px;
}

.stRadio > div {
    flex-direction: row;
}

.stRadio label {
    background: white;
    padding: 12px 24px;
    border-radius: 12px;
    border: 1px solid #E5E7EB;
    font-size: 15px;
    font-weight: 600;
    color: #111827 !important;
    transition: 0.2s ease;
}

.stRadio label:hover {
    border-color: #4F46E5;
    color: #4F46E5 !important;
}

/* =========================
   TITLES
========================= */

h1 {
    color: #111827 !important;
    font-size: 42px !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #111827 !important;
    font-weight: 700 !important;
}

/* =========================
   TEXT
========================= */

p, li, label, span {
    color: #374151 !important;
}

/* =========================
   METRIC CARDS
========================= */

.metric-card {
    background: white;
    border-radius: 18px;
    padding: 24px;
    border: 1px solid #E5E7EB;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    transition: 0.2s ease;
}

.metric-card:hover {
    transform: translateY(-3px);
    box-shadow: 0px 10px 24px rgba(0,0,0,0.08);
}

.metric-title {
    font-size: 14px;
    color: #6B7280 !important;
    margin-bottom: 10px;
    font-weight: 600;
}

.metric-value {
    font-size: 34px;
    color: #111827 !important;
    font-weight: 800;
}

/* =========================
   STREAMLIT METRICS
========================= */

[data-testid="metric-container"] {
    background: white;
    border-radius: 18px;
    padding: 18px;
    border: 1px solid #E5E7EB;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}

/* =========================
   BUTTONS
========================= */

.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(
        90deg,
        #4F46E5,
        #06B6D4
    );
    color: white !important;
    border: none;
    border-radius: 12px;
    padding: 12px 22px;
    font-size: 15px;
    font-weight: 600;
    transition: 0.2s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0px 6px 14px rgba(79,70,229,0.25);
}

/* =========================
   FILE UPLOADER
========================= */

[data-testid="stFileUploader"] {
    background: white;
    border-radius: 18px;
    border: 2px dashed #4F46E5;
    padding: 18px;
}

/* =========================
   DATAFRAME
========================= */

[data-testid="stDataFrame"] {
    background: white;
    border-radius: 16px;
    border: 1px solid #E5E7EB;
    padding: 10px;
}

/* =========================
   ALERTS
========================= */

.stAlert {
    border-radius: 14px;
    border: none;
}

/* =========================
   CHARTS
========================= */

.element-container:has(.js-plotly-plot) {
    background: white;
    border-radius: 18px;
    padding: 18px;
    border: 1px solid #E5E7EB;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}

/* =========================
   INPUTS
========================= */

.stTextInput input,
.stSelectbox div,
.stDateInput div {
    border-radius: 12px !important;
}

/* =========================
   SIDEBAR REMOVE
========================= */

section[data-testid="stSidebar"] {
    display: none;
}

/* =========================
   PAGE PADDING
========================= */

.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
    padding-bottom: 2rem;
}

</style>
"""
