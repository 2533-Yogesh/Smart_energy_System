CUSTOM_CSS = """
<style>

/* =========================
   MAIN APP
========================= */

.stApp {
    background-color: #f5f7fb;
    color: #111827;
    font-family: 'Segoe UI', sans-serif;
}

/* REMOVE STREAMLIT DEFAULT MENU */

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
    width: 100%;
    padding: 20px 35px;
    border-radius: 22px;
    background: linear-gradient(
        90deg,
        #4f46e5,
        #7c3aed
    );
    margin-bottom: 25px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.12);
}

.nav-left {
    color: white;
    font-size: 30px;
    font-weight: 700;
    letter-spacing: 1px;
}

/* =========================
   PAGE TITLES
========================= */

h1 {
    color: #111827;
    font-size: 42px !important;
    font-weight: 800;
}

h2, h3 {
    color: #1f2937;
    font-weight: 700;
}

/* =========================
   CAPTION
========================= */

.caption {
    color: #6b7280;
    font-size: 16px;
}

/* =========================
   HORIZONTAL RADIO MENU
========================= */

div[role="radiogroup"] {
    display: flex;
    justify-content: center;
    gap: 18px;
    margin-bottom: 25px;
}

/* RADIO BUTTONS */

.stRadio > div {
    flex-direction: row;
}

.stRadio label {
    background: white;
    padding: 12px 28px;
    border-radius: 14px;
    border: 2px solid #e5e7eb;
    font-weight: 600;
    font-size: 16px;
    transition: all 0.3s ease;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.04);
}

.stRadio label:hover {
    border-color: #6366f1;
    color: #6366f1;
    transform: translateY(-2px);
}

/* =========================
   METRIC CARDS
========================= */

.metric-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.08);
    transition: 0.3s ease;
    border-left: 8px solid #6366f1;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 10px 30px rgba(0,0,0,0.12);
}

.metric-title {
    font-size: 16px;
    color: #6b7280;
    margin-bottom: 10px;
    font-weight: 600;
}

.metric-value {
    font-size: 34px;
    font-weight: 800;
    color: #111827;
}

/* =========================
   STREAMLIT METRICS
========================= */

[data-testid="metric-container"] {
    background: white;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    border-left: 6px solid #6366f1;
}

/* =========================
   BUTTONS
========================= */

.stButton > button {
    background: linear-gradient(
        90deg,
        #6366f1,
        #8b5cf6
    );
    color: white;
    border: none;
    border-radius: 14px;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: 700;
    transition: 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0px 6px 15px rgba(99,102,241,0.3);
}

/* =========================
   DOWNLOAD BUTTON
========================= */

.stDownloadButton > button {
    background: linear-gradient(
        90deg,
        #06b6d4,
        #3b82f6
    );
    color: white;
    border-radius: 14px;
    border: none;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: 700;
    transition: 0.3s ease;
}

.stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0px 6px 15px rgba(59,130,246,0.3);
}

/* =========================
   FILE UPLOADER
========================= */

[data-testid="stFileUploader"] {
    background: white;
    border-radius: 18px;
    padding: 18px;
    border: 2px dashed #6366f1;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}

/* =========================
   DATAFRAME
========================= */

[data-testid="stDataFrame"] {
    background: white;
    border-radius: 18px;
    padding: 12px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}

/* =========================
   ALERT BOXES
========================= */

.stAlert {
    border-radius: 16px;
    border: none;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.05);
}

/* =========================
   PLOTLY CHART CONTAINER
========================= */

.element-container:has(.js-plotly-plot) {
    background: white;
    border-radius: 22px;
    padding: 18px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

/* =========================
   INPUT FIELDS
========================= */

.stTextInput > div > div > input {
    border-radius: 14px;
    border: 2px solid #e5e7eb;
    padding: 10px;
}

.stTextInput > div > div > input:focus {
    border-color: #6366f1;
}

/* =========================
   SELECT BOX
========================= */

.stSelectbox > div > div {
    border-radius: 14px;
}

/* =========================
   DATE INPUT
========================= */

.stDateInput > div {
    border-radius: 14px;
}

/* =========================
   SIDEBAR HIDE
========================= */

section[data-testid="stSidebar"] {
    display: none;
}

/* =========================
   SECTIONS
========================= */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

/* =========================
   SCROLLBAR
========================= */

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #f1f5f9;
}

::-webkit-scrollbar-thumb {
    background: #c4b5fd;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #8b5cf6;
}

</style>
"""
