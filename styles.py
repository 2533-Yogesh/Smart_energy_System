CUSTOM_CSS = """
<style>

/* =========================
   GLOBAL
========================= */

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* MAIN BACKGROUND */

.stApp {

    background:
    linear-gradient(
        rgba(248,250,252,0.92),
        rgba(248,250,252,0.92)
    ),
    url("https://images.unsplash.com/photo-1516321318423-f06f85e504b3");

    background-size: cover;
    background-attachment: fixed;
    background-position: center;

    color: #111827;
}

/* REMOVE STREAMLIT DEFAULTS */

#MainMenu,
footer,
header {
    visibility: hidden;
}

/* =========================
   NAVBAR
========================= */

.navbar {

    padding: 10px 5px 20px 5px;

    margin-bottom: 10px;
}

.nav-left {

    color: #111827;

    font-size: 34px;

    font-weight: 800;

    letter-spacing: -1px;
}

/* =========================
   REMOVE EMPTY BAR
========================= */

.stRadio > label {
    display: none;
}

/* =========================
   TOP NAVIGATION
========================= */

div[role="radiogroup"] {

    display: flex;

    gap: 14px;

    margin-top: -10px;

    margin-bottom: 35px;
}

.stRadio > div {
    flex-direction: row;
}

/* NAV BUTTONS */

.stRadio label {

    background: rgba(255,255,255,0.8);

    backdrop-filter: blur(10px);

    padding: 12px 24px;

    border-radius: 14px;

    border: 1px solid rgba(255,255,255,0.4);

    font-size: 15px;

    font-weight: 600;

    color: #111827 !important;

    transition: 0.2s ease;

    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}

.stRadio label:hover {

    transform: translateY(-2px);

    border-color: #4F46E5;
}

/* =========================
   TITLES
========================= */

h1 {

    color: #111827 !important;

    font-size: 56px !important;

    font-weight: 800 !important;

    line-height: 1.1;
}

h2, h3 {

    color: #111827 !important;

    font-weight: 700 !important;
}

/* =========================
   TEXT
========================= */

p, li, span {

    color: #4B5563 !important;

    font-size: 16px;
}

/* =========================
   METRIC CARDS
========================= */

.metric-card {

    background: rgba(255,255,255,0.82);

    backdrop-filter: blur(14px);

    border-radius: 20px;

    padding: 28px;

    border: 1px solid rgba(255,255,255,0.4);

    box-shadow: 0px 8px 24px rgba(0,0,0,0.06);

    transition: 0.25s ease;
}

.metric-card:hover {

    transform: translateY(-4px);

    box-shadow: 0px 14px 32px rgba(0,0,0,0.08);
}

.metric-title {

    font-size: 15px;

    color: #6B7280 !important;

    margin-bottom: 12px;

    font-weight: 600;
}

.metric-value {

    font-size: 38px;

    color: #111827 !important;

    font-weight: 800;
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

    border-radius: 14px;

    padding: 12px 24px;

    font-size: 15px;

    font-weight: 600;

    transition: 0.2s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover {

    transform: translateY(-2px);

    box-shadow: 0px 8px 20px rgba(79,70,229,0.25);
}

/* =========================
   UPLOAD SECTION
========================= */

[data-testid="stFileUploader"] {

    background: rgba(255,255,255,0.82) !important;

    backdrop-filter: blur(10px);

    border-radius: 20px;

    border: 2px dashed #4F46E5;

    padding: 22px;
}

/* UPLOAD TEXT */

[data-testid="stFileUploader"] * {

    color: #111827 !important;

    font-weight: 500 !important;
}

/* =========================
   TABLES
========================= */

[data-testid="stDataFrame"] {

    background: rgba(255,255,255,0.85);

    border-radius: 18px;

    padding: 12px;

    border: 1px solid rgba(255,255,255,0.5);
}

/* =========================
   ALERTS
========================= */

.stAlert {

    border-radius: 16px;

    border: none;

    backdrop-filter: blur(8px);
}

/* =========================
   CHARTS
========================= */

.element-container:has(.js-plotly-plot) {

    background: rgba(255,255,255,0.82);

    backdrop-filter: blur(14px);

    border-radius: 22px;

    padding: 18px;

    border: 1px solid rgba(255,255,255,0.5);

    box-shadow: 0px 8px 24px rgba(0,0,0,0.06);

    margin-bottom: 24px;
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
   PAGE SPACING
========================= */

.block-container {

    padding-top: 1.5rem;

    padding-left: 4rem;

    padding-right: 4rem;

    padding-bottom: 2rem;
}

</style>
"""
