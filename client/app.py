import streamlit as st
import pandas as pd

from pages.page_executive import render_executive_center
from pages.page_supply_chain import render_supply_chain
from pages.page_forecast import render_forecast_engine
from pages.page_custom_scenario import render_custom_scenario

from data_engine import generate_synthetic_data
from ml_engine import optimize_price

st.set_page_config(
    page_title="Retail Intelligence Orchestrator PRO",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium Retail Dark/Light Theme Support
# Defaulting to Dark Navy/Black theme as requested
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide top header bar in streamlit */
    header {visibility: hidden;}
    
    .metric-card {
        background-color: #1A1F2B;
        border: 1px solid #2A303C;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    .themeable-text {
        color: #E2E8F0;
    }
    
    .status-healthy { color: #10B981; font-weight: bold; }
    .status-fast { color: #3B82F6; font-weight: bold; }
    .status-critical { color: #EF4444; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = generate_synthetic_data(num_skus=100)
    df = optimize_price(df)
    return df

df = load_data()

# --- SIDEBAR NAV ---
st.sidebar.image("https://img.icons8.com/color/96/000000/artificial-intelligence.png", width=64)
st.sidebar.title("Orchestrator PRO")
st.sidebar.caption("Enterprise Retail Intelligence")
st.sidebar.divider()

page = st.sidebar.radio("Navigation", [
    "📊 Executive Center", 
    "📦 Supply Chain Intelligence", 
    "📈 Forecast Engine",
    "🛠️ Custom Scenario Builder"
])

st.sidebar.divider()
theme = st.sidebar.select_slider("Theme", options=["Dark", "Light"], value="Dark")

if theme == "Light":
    st.markdown("""
        <style>
        .stApp { background-color: #F8FAFC; color: #0F172A; }
        .metric-card { background-color: #FFFFFF; border: 1px solid #E2E8F0; }
        .themeable-text { color: #0F172A; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp { background-color: #0B0E14; color: #F8FAFC; }
        </style>
    """, unsafe_allow_html=True)

# --- ROUTING ---
if page == "📊 Executive Center":
    render_executive_center(df)
elif page == "📦 Supply Chain Intelligence":
    render_supply_chain(df)
elif page == "📈 Forecast Engine":
    render_forecast_engine(df)
elif page == "🛠️ Custom Scenario Builder":
    render_custom_scenario()

