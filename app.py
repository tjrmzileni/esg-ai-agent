import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

st.set_page_config(page_title="ESG Agent Dashboard", layout="centered")

# Title and Description
st.title("🌍 ESG Agent Dashboard")
st.markdown("""
Upload your ESG data to visualize key metrics (Emissions, Energy, Waste) and get AI-powered insights.
""")

# File Upload
uploaded_file = st.file_uploader("📂 Upload your ESG CSV file", type=["csv"])

if uploaded_file is not None:
    # Load Data
    df = pd.read_csv(uploaded_file)

    # Show data preview
    st.subheader("📊 Raw Data Preview")
    st.dataframe(df)

    # Visualizations
    st.subheader("📈 ESG Visualizations")

    fig, ax = plt.subplots(figsize=(10, 4))
    df.plot(kind="bar", ax=ax)
    st.pyplot(fig)

    # AI Insights
    st.subheader("🧠 AI-Powered Insights")
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    text_data = df.describe().to_string()
    summary = summarizer(text_data, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    st.success(summary)

else:
    st.info("Please upload a CSV file to get started.")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="ESG AI Agent", layout="wide")

st.title("🌍 ESG AI Agent")
st.markdown("""
Welcome to the ESG AI Agent — your smart assistant for analyzing sustainability metrics.

Upload your company's ESG data (CSV), and the agent will visualize emissions, energy use, and waste trends.
""")
uploaded_file = st.file_uploader("Upload your ESG CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.info("No file uploaded. Using sample data.")
    sample_csv = """Emissions_tCO2,Energy_kWh,Waste_kg
1200,15000,320
980,12200,280
1100,13800,300"""
    df = pd.read_csv(pd.compat.StringIO(sample_csv))
st.subheader("📊 Key ESG Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Avg Emissions (tCO2)", round(df["Emissions_tCO2"].mean(), 2))
col2.metric("Avg Energy (kWh)", round(df["Energy_kWh"].mean(), 2))
col3.metric("Avg Waste (kg)", round(df["Waste_kg"].mean(), 2))
st.subheader("📈 ESG Trends")

st.line_chart(df)
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
