import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

st.set_page_config(page_title="ESG AI Agent", layout="wide")  # ✅ Must come FIRST after imports

# Title and Description
st.title("🌍 ESG AI Agent")
st.markdown("""
Welcome to the ESG AI Agent — your smart assistant for analyzing sustainability metrics.

Upload your company's ESG data (CSV), and the agent will visualize emissions, energy use, and waste trends.
""")

# File Upload
uploaded_file = st.file_uploader("📂 Upload your ESG CSV file", type=["csv"])

# Load and handle data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.info("No file uploaded. Using sample data.")
    sample_csv = """Emissions_tCO2,Energy_kWh,Waste_kg
1200,15000,320
980,12200,280
1100,13800,300"""
    from io import StringIO
    df = pd.read_csv(StringIO(sample_csv))

# ESG Metrics
st.subheader("📊 Key ESG Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Emissions (tCO2)", round(df["Emissions_tCO2"].mean(), 2))
col2.metric("Avg Energy (kWh)", round(df["Energy_kWh"].mean(), 2))
col3.metric("Avg Waste (kg)", round(df["Waste_kg"].mean(), 2))

# ESG Trends
st.subheader("📈 ESG Trends")
st.line_chart(df)

# AI-Powered Insights
st.subheader("🧠 AI-Powered Insights")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
text_data = df.describe().to_string()
summary = summarizer(text_data, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
st.success(summary)

# Optional: Custom styling
st.markdown("""
<style>
    .css-1d391kg {
        padding-top: 0rem;
    }
    .css-1kyxreq {
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)
