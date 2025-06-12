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
