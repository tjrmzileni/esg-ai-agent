import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your ESG data
df = pd.read_csv("ESG.csv")

# Title
st.title("📊 ESG Dashboard")

# Show data table
st.subheader("Raw ESG Data")
st.dataframe(df)

# Show simple metrics
st.subheader("Summary")
st.metric("Total Emissions (tCO₂)", df['Emissions_tCO2'].sum())
st.metric("Total Energy (kWh)", df['Energy_kWh'].sum())
st.metric("Total Waste (kg)", df['Waste_kg'].sum())

# Plotting
st.subheader("Visualizations")

fig, ax = plt.subplots(1, 3, figsize=(15, 4))

df['Emissions_tCO2'].plot(kind='bar', ax=ax[0], title='Emissions')
df['Energy_kWh'].plot(kind='bar', ax=ax[1], title='Energy Use')
df['Waste_kg'].plot(kind='bar', ax=ax[2], title='Waste Generated')

st.pyplot(fig)
