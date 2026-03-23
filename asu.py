import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="Jubail Regional Optimizer", layout="wide")
st.title("🛡️ Jubail Regional ASU Optimizer & Gap Analysis")

# --- 2. DATA GENERATION (Simulated Real-Time Data) ---
# This dictionary maps ASUs to their specific equipment health
# In a real app, this data would come from your SQL/Historian
asu_list = ["ASU-41", "ASU-51", "ASU-71", "ASU-81", "ASU-91"]

regional_summary = pd.DataFrame({
    "ASU": asu_list,
    "Health_Index": [88, 82, 96, 62, 90],
    "SEC_Actual": [0.605, 0.622, 0.581, 0.745, 0.598], # kWh/Nm3
    "Current_Target": [45000, 48000, 55000, 42000, 50000],
    "Optimized_Target": [48000, 43000, 62000, 28000, 54000],
    "Current_MPC_HL": [52000, 55000, 60000, 48000, 65000],
    "New_MPC_HL": [55000, 50000, 65000, 35000, 66000]
})

# --- 3. TOP SECTION: THE PRIZE (OPPORTUNITY) ---
st.header("📈 Regional Opportunity & Strategy")
c1, c2, c3 = st.columns(3)
total_flow = regional_summary["Optimized_Target"].sum()
energy_gap = (regional_summary["SEC_Actual"].mean() - 0.580) * total_flow / 1000 # MW

c1.metric("Total Regional Flow", f"{total_flow:,.0f} Nm3/h")
c2.metric("Energy Opportunity Gap", f"{energy_gap:.2f} MW", delta="-7.4%", delta_color="normal")
c3.metric("Venting Status", "0.0 Nm3/h", delta="Eliminated", delta_color="normal")

# --- 4. REGIONAL HEATMAP (ASU SELECTION) ---
st.divider()
st.subheader("🗺️ ASU Efficiency Heat Map")
st.write("Click an ASU below to drill down into specific equipment failures.")

# Create a heatmap-style bar chart
fig_heat = px.bar(regional_summary, x="ASU", y="Health_Index", color="Health_Index",
                 text="SEC_Actual", color_continuous_scale='RdYlGn',
                 labels={'Health_Index': 'Health %', 'SEC_Actual': 'SEC (kWh/Nm3)'})
fig_heat.update_traces(texttemplate='%{text} kWh/Nm3', textposition='outside')
st.plotly_chart(fig_heat, use_container_width=True)

# Selection Logic
selected_asu = st.selectbox("Detailed Analysis for:", asu_list, index=3) # Default to ASU-81

# --- 5. DRILL-DOWN: EQUIPMENT PERFORMANCE & GAP ---
st.divider()
st.subheader(f"🔍 {selected_asu} Component Drill-Down")

# Mock equipment data - specific problems for the "Problematic One" (ASU-81)
if selected_asu == "ASU-81":
    h_scores = [85, 52, 90, 48, 88, 92, 72, 68] # Low health for HX and Expander
    penalties = [0.015, 0.092, 0.005, 0.115, 0.002, 0.004, 0.025, 0.032]
else:
    h_scores = [95, 92, 98, 91, 96, 99, 94, 93]
    penalties = [0.002, 0.005, 0.001, 0.004, 0.001, 0.001, 0.003, 0.004]

equip_df = pd.DataFrame({
    "Equipment": ["MAC", "Heat Exchangers", "Mol Sieves", "Expander", "Booster Comp", "Cold Box", "LP Column", "HP Column"],
    "Health_Score": h_scores,
    "SEC_Penalty": penalties
})

col_a, col_b = st.columns([2, 1])

with col_a:
    fig_equip = px.bar(equip_df, x="Equipment", y="Health_Score", color="Health_Score",
                      range_y=[0, 100], color_continuous_scale='RdYlGn',
                      title="Asset Performance vs. Design (%)")
    st.plotly_chart(fig_equip, use_container_width=True)

with col_b:
    st.write("**Top Gap Contributors (kWh/Nm3)**")
    top_gaps = equip_df.sort_values("SEC_Penalty", ascending=False).head(3)
    for i, row in top_gaps.iterrows():
        st.warning(f"⚠️ **{row['Equipment']}**: +{row['SEC_Penalty']:.3f} Penalty")
    
    total_penalty = equip_df["SEC_Penalty"].sum()
    st.error(f"**Total Efficiency Gap:** {total_penalty:.3f} kWh/Nm3")

# --- 6. OPTIMIZER OUTPUTS (TARGETS & MPC) ---
st.divider()
st.subheader("📥 New Production Targets & MPC Limits")
# Filtering to show only the selected ASU's new targets
asu_row = regional_summary[regional_summary["ASU"] == selected_asu].iloc[0]

res1, res2, res3 = st.columns(3)
res1.metric("Optimized Target", f"{asu_row['Optimized_Target']:,} Nm3/h")
res2.metric("Current MPC HL", f"{asu_row['Current_MPC_HL']:,} Nm3/h")
res3.metric("New Recommended MPC HL", f"{asu_row['New_MPC_HL']:,}", 
           delta=int(asu_row['New_MPC_HL'] - asu_row['Current_MPC_HL']))

# --- 7. GAN COMPRESSOR LOADING ---
st.divider()
st.subheader("💨 Regional GAN Compressor Loading (Top 10)")
comp_data = pd.DataFrame({
    "Unit": [f"MP-0{i}" for i in range(1, 5)] + [f"LP-0{i}" for i in range(1, 7)],
    "Priority": ["Primary (High Eff)"]*4 + ["Secondary"]*6,
    "Target Load %": [100, 100, 100, 100, 85, 70, 0, 0, 0, 0],
    "Mode": ["Base Load"]*4 + ["Swing"]*2 + ["Standby"]*4
})
st.table(comp_data)
