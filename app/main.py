import streamlit as st
from tabs.run import run_tab
from tabs.replay import replay_tab

st.set_page_config(layout="wide", page_title="N-body Simulator")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap');

/* Background principal */
.stApp {
    background-color: #0a0e1a;
}

/* Sidebar et panels */
section[data-testid="stSidebar"] {
    background-color: #0d1221;
}

/* Texte général */
html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
    color: #c8facc;
}

/* Titres */
h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600;
    letter-spacing: -0.5px;
    color: #eafff2 !important;
}

/* Subheader spécifique */
[data-testid="stHeadingWithActionElements"] {
    color: #eafff2 !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background-color: #0d1221;
}

.stTabs [data-baseweb="tab"] {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 500;
    color: #7eb8c9;
}

.stTabs [aria-selected="true"] {
    color: #00d47a;
    border-bottom-color: #00d47a;
}

/* Labels des inputs */
.stSelectbox label, .stNumberInput label,
.stTextInput label, .stSlider label {
    color: #7eb8c9 !important;
    font-family: 'Space Grotesk', sans-serif;
}

/* Selectbox */
.stSelectbox > div > div {
    background-color: #131929 !important;
    color: #eafff2 !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
}

.stSelectbox > div > div > div {
    color: #eafff2 !important;
}

/* Number input — container complet */
.stNumberInput > div {
    background-color: #131929 !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 4px;
}

.stNumberInput > div > div {
    background-color: #131929 !important;
}

.stNumberInput > div > div > input {
    background-color: #131929 !important;
    color: #eafff2 !important;
    font-family: 'Space Mono', monospace !important;
}

/* Boutons +/- du number input */
.stNumberInput button {
    background-color: #1e2d45 !important;
    color: #eafff2 !important;
    border: none !important;
}

.stNumberInput button:hover {
    background-color: #00d47a !important;
}

/* Text input */
.stTextInput > div > div > input {
    background-color: #131929 !important;
    color: #eafff2 !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
}

/* Dropdown menu ouvert */
[data-baseweb="popover"] {
    background-color: #131929 !important;
}

[data-baseweb="menu"] {
    background-color: #131929 !important;
}

[data-baseweb="option"] {
    background-color: #131929 !important;
    color: #eafff2 !important;
}

[data-baseweb="option"]:hover {
    background-color: #1e2d45 !important;
}

/* Boutons principaux */
.stButton button {
    background-color: rgba(0, 180, 90, 0.6) !important;
    border: 1px solid rgba(0, 255, 150, 0.6) !important;
    color: #eafff2 !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

.stButton button:hover {
    background-color: rgba(0, 220, 120, 0.8) !important;
}

/* Progress bar */
.stProgress > div > div {
    background-color: #00d47a;
}

/* Table metadata */
[data-testid="stTable"] {
    background-color: #131929 !important;
    color: #eafff2 !important;
}

[data-testid="stTable"] th {
    background-color: #1e2d45 !important;
    color: #7eb8c9 !important;
}

[data-testid="stTable"] td {
    color: #eafff2 !important;
    border-color: rgba(255,255,255,0.1) !important;
}

/* Divider */
hr {
    border-color: rgba(255,255,255,0.1);
}

/* Expander */
.streamlit-expanderHeader {
    background-color: #131929 !important;
    color: #eafff2 !important;
}

.streamlit-expanderContent {
    background-color: #0d1221 !important;
}

/* Info / warning boxes */
.stAlert {
    background-color: #131929 !important;
    color: #eafff2 !important;
}
/* Number input fond blanc — ciblage plus précis */
[data-testid="stNumberInput"] > div {
    background-color: #131929 !important;
}

[data-testid="stNumberInput"] input {
    background-color: #131929 !important;
    color: #eafff2 !important;
}

[data-testid="stNumberInput"] > div > div {
    background-color: #131929 !important;
}

/* Barre supérieure Deploy */
[data-testid="stToolbar"] {
    background-color: #0d1221 !important;
}

[data-testid="stDecoration"] {
    background-color: #0d1221 !important;
}

header[data-testid="stHeader"] {
    background-color: #0d1221 !important;
}

/* Bouton Deploy */
[data-testid="stToolbarActions"] button {
    background-color: #131929 !important;
    color: #7eb8c9 !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
}
</style>
""", unsafe_allow_html=True)

st.subheader("N-body Simulator")

tab_run, tab_replay = st.tabs(["Run", "Replay"])

with tab_run:
    run_tab()

with tab_replay:
    replay_tab()
