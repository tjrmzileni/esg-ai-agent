import streamlit as st
import pandas as pd
import json
import io
from transformers import pipeline


st.set_page_config(page_title="ESG AI Agent", layout="wide")

st.title("🌍 ESG AI Agent")
st.markdown("""
Upload your ESG data as CSV, Excel, or JSON and get powerful AI-driven insights on emissions, energy, and waste.
""")

# File upload
uploaded_file = st.file_uploader("📂 Upload ESG file", type=["csv", "xlsx", "xls", "json"])

# Load data
if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1]

    try:
        if file_type == "csv":
            df = pd.read_csv(uploaded_file)
        elif file_type in ["xlsx", "xls"]:
            df = pd.read_excel(uploaded_file)
        elif file_type == "json":
            stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
            data = json.load(stringio)
            df = pd.DataFrame(data)
        else:
            st.error("Unsupported file type.")
    except Exception as e:
        st.error(f"Error loading file: {e}")
        st.stop()
else:
    st.info("No file uploaded. Using sample data.")
    sample_csv = """Emissions_tCO2,Energy_kWh,Waste_kg
1200,15000,320
980,12200,280
1100,13800,300"""
df = pd.read_csv(io.StringIO(sample_csv))


required_columns = ['Emissions_tCO2', 'Energy_kWh', 'Waste_kg']
if not all(col in df.columns for col in required_columns):
    st.error(f"Missing required columns. Make sure your file includes: {', '.join(required_columns)}")
    st.stop()


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
# History Section
if st.session_state.upload_history:
    st.subheader("📂 Upload History (This Session)")
    for idx, item in enumerate(reversed(st.session_state.upload_history)):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"- **{item['filename']}** uploaded at *{item['timestamp']}*")
        with col2:
            if st.button(f"📄 View {item['filename']}", key=f"view_{idx}"):
                active_df = item['data']
                st.experimental_rerun()