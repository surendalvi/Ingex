import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# --- 1. SETTINGS & STYLING ---
st.set_page_config(page_title="Jubail Regional Optimizer", layout="wide")
st.title("🏗️ Jubail ASU Regional Optimizer & Gap Analysis")

# --- 2. GLOBAL INPUTS (SIDEBAR) ---
with st.sidebar:
    st.header("📍 Regional Demand")
    gan_demand = st.slider("Total GAN Demand (Nm3/h)", 100000, 300000, 185000)
    gox_demand = st.slider("Total GOX Demand (Nm3/h)", 20000, 100000, 45000)
    st.header("⚡ Energy Market")
    pwr_cost = st.number_input("Power Price (SAR/MWh)", value=220)

# --- 3. THE OPPORTUNITY (BEFORE vs AFTER) ---
st.header("📈 Regional Opportunity Assessment")
# Mock logic for Opportunity
current_venting = 5200  # Nm3/h
opt_venting = 0
current_sec = 0.620     # kWh/Nm3
opt_sec = 0.585         # kWh/Nm3
total_flow = gan_demand + gox_demand

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Venting Reduction", f"{current_venting} → {opt_venting} Nm3/h", delta="-100%")
with col2:
    energy_saving = (current_sec - opt_sec) * total_flow / 1000 # MW
    st.metric("Energy Opportunity", f"{energy_saving:.2f} MW", delta=f"{(current_sec-opt_sec):.3f} SEC Improvement")
with col3:
    daily_saving = energy_saving * 24 * (pwr_cost/1000)
    st.metric("Daily Cost Saving", f"{daily_saving:,.0f} SAR/Day", delta="Potential")

st.divider()

# --- 4. COMPRESSOR LOADING (10 UNITS) ---
st.subheader("💨 GAN Compressor Loading Strategy")
st.caption("Strategy: Priority loading for MP Compressors (Higher Efficiency).")
comp_data = pd.DataFrame({
    "Compressor": [f"MP-0{i}" for i in range(1, 5)] + [f"LP-0{i}" for i in range(1, 7)],
    "Type": ["MP"]*4 + ["LP"]*6,
    "Status": ["Running"]*6 + ["Standby"]*4,
    "Current Load %": [100, 100, 95, 100, 80, 75, 0, 0, 0, 0],
    "Efficiency (Design)": [92, 91, 90, 92, 84, 83, 85, 84, 82, 83]
})
# Highlight based on efficiency/load
st.dataframe(comp_data.style.background_gradient(subset=['Current Load %'], cmap='YlGn'))

# --- 5. ASU RANKING & DRILL-DOWN (GAP IDENTIFICATION) ---
st.divider()
st.header("🎯 ASU Performance & Equipment Gap")

# ASU Leaderboard based on SEC
asu_summary = pd.DataFrame({
    "ASU": ["ASU-41", "ASU-51", "ASU-71", "ASU-81", "ASU-91"],
    "Rank": [2, 3, 1, 5, 4],
    "Current SEC": [0.59, 0.61, 0.57, 0.68, 0.63],
    "Problematic": [False, False, False, True, False]
}).sort_values("Rank")

st.write("### 🏆 ASU Efficiency Leaderboard")
rank_cols = st.columns(5)
for i, row in asu_summary.iterrows():
    with rank_cols[int(row['Rank'])-1]:
        st.metric(f"Rank {row['Rank']}", row['ASU'], delta=f"{row['Current SEC']} kWh/Nm3")

st.subheader("🔍 Equipment-Level Problem Identification")
selected_asu = st.selectbox("Select ASU to Drill-Down:", asu_summary["ASU"])

# Equipment data for drill down
# Penalty values represent increase in SEC due to poor health
equip_performance = pd.DataFrame({
    "Equipment": ["MAC", "Main Heat Exchanger", "Molecular Sieves", "Expander", "Booster Compressor", "Cold Box", "LP Column", "HP Column"],
    "Health %": [92, 78, 95, 72, 98, 94, 88, 85],
    "Design Efficiency": [90, 100, 100, 88, 92, 100, 95, 95],
    "SEC Impact (Penalty)": [0.012, 0.045, 0.005, 0.062, 0.002, 0.008, 0.015, 0.022]
})

c1, c2 = st.columns([2, 1])
with c1:
    st.write(f"**Diagnostic Summary for {selected_asu}**")
    # Show health as a bar chart
    fig = px.bar(equip_performance, x='Equipment', y='Health %', color='Health %', 
                 color_continuous_scale='RdYlGn', range_color=[70, 100])
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.write("**Top Gap Contributors**")
    sorted_gap = equip_performance.sort_values("SEC Impact (Penalty)", ascending=False)
    for i, row in sorted_gap.head(3).iterrows():
        st.warning(f"**{row['Equipment']}**: +{row['SEC Impact (Penalty)']} kWh/Nm3 penalty")

st.info(f"💡 **Gap Identification:** In {selected_asu}, the **Expander** and **Heat Exchanger** are the primary drivers of the energy gap. Fixing these would reduce specific energy by {sorted_gap['SEC Impact (Penalty)'].iloc[0:2].sum():.3f} kWh/Nm3.")
