import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Jubail ASU Regional Optimizer", layout="wide")
st.title("🛡️ Regional ASU Optimizer: Strategy & Gap Identification")

# --- 2. DATA MODEL (Mocked for 5 ASUs) ---
# In production, this would be a live SQL/Historian query
if 'selected_asu' not in st.session_state:
    st.session_state.selected_asu = "ASU-71" # Default selection

asu_list = ["ASU-41", "ASU-51", "ASU-71", "ASU-81", "ASU-91"]

# High-level ASU Status Data
regional_data = pd.DataFrame({
    "ASU": asu_list,
    "Health_Index": [85, 80, 95, 65, 88], # % Health
    "Current_SEC": [0.61, 0.63, 0.58, 0.72, 0.60], # kWh/Nm3
    "Target_Flow": [48000, 42000, 58000, 25000, 52000],
    "Current_Limit_High": [52000, 55000, 60000, 48000, 65000],
    "New_MPC_Limit_High": [53500, 54000, 62000, 35000, 66500], # Suggested based on health
    "Status": ["Stable", "Stable", "Optimized", "Gap Identified", "Stable"]
})

# --- 3. TOP LEVEL: OPPORTUNITY & REGIONAL HEAT MAP ---
st.header("🌍 Regional Performance Overview")

col1, col2 = st.columns([1, 2])

with col1:
    st.write("### Total Regional Opportunity")
    total_flow = regional_data['Target_Flow'].sum()
    avg_sec = regional_data['Current_SEC'].mean()
    # Simple opportunity calc
    potential_saving = (avg_sec - 0.575) * total_flow / 1000 # MW
    st.metric("Total Energy Gap", f"{potential_saving:.2f} MW", delta="-6.2%", delta_color="normal")
    st.info("💡 **Insight:** ASU-81 is currently the primary driver of regional inefficiency due to high Specific Energy.")

with col2:
    st.write("### ASU Health Heat Map")
    # Heat map showing Health vs SEC
    fig_heat = px.parallel_categories(regional_data, dimensions=['ASU', 'Status'],
                                    color="Health_Index", color_continuous_scale='RdYlGn')
    # Using a colored bar chart as a 'Heat Map' selector
    fig_status = px.bar(regional_data, x="ASU", y="Health_Index", color="Health_Index",
                       text="Current_SEC", color_continuous_scale='RdYlGn',
                       title="ASU Health vs Specific Energy (SEC labeled on bars)")
    st.plotly_chart(fig_status, use_container_width=True)

# --- 4. OPTIMIZER RESULTS: TARGETS & MPC LIMITS ---
st.divider()
st.header("🎯 Optimizer Prescriptions: Targets & MPC Limits")
st.write("Current vs. Optimized setpoints for the next 1-hour cycle.")

# Formatting the output table
display_df = regional_data[["ASU", "Target_Flow", "Current_Limit_High", "New_MPC_Limit_High", "Status"]]
st.table(display_df.style.apply(lambda x: ['background-color: #ffcccc' if x.ASU == 'ASU-81' else '' for i in x], axis=1))

# --- 5. DRILL-DOWN: EQUIPMENT PERFORMANCE ---
st.divider()
st.header("🔍 Component Drill-Down & Gap Analysis")
selected = st.selectbox("Select ASU to investigate Equipment Performance:", asu_list, index=2)

# Specific Equipment Performance Mock Data
equip_data = pd.DataFrame({
    "Equipment": ["MAC", "Main HX", "Mol Sieves", "Expander", "Booster Comp", "Cold Box", "LP Column", "HP Column"],
    "Health_Score": [92, 75, 96, 70, 94, 98, 85, 82], # % Performance vs Design
    "SEC_Penalty": [0.008, 0.042, 0.002, 0.055, 0.001, 0.003, 0.012, 0.018] # kWh/Nm3 added
})

# Filter equipment data based on 'selected' ASU (Simulating different issues for ASU-81)
if selected == "ASU-81":
    equip_data["Health_Score"] = [80, 55, 90, 45, 85, 92, 70, 65]
    equip_data["SEC_Penalty"] = [0.025, 0.085, 0.010, 0.120, 0.005, 0.008, 0.035, 0.045]

c1, c2 = st.columns([2, 1])

with c1:
    st.write(f"#### {selected} Equipment Health Status")
    fig_equip = px.bar(equip_performance, x='Equipment', y='Health_Score', color='Health_Score',
                      range_y=[0, 100], color_continuous_scale='RdYlGn',
                      title="Performance vs. Design Curve (%)")
    st.plotly_chart(fig_equip, use_container_width=True)

with c2:
    st.write("#### Energy Loss Attribution")
    # Identify top 2 gaps
    top_gaps = equip_data.sort_values("SEC_Penalty", ascending=False).head(3)
    for i, row in top_gaps.iterrows():
        st.warning(f"**{row['Equipment']}**: +{row['SEC_Penalty']:.3f} kWh/Nm3 Penalty")
    
    total_penalty = equip_data['SEC_Penalty'].sum()
    st.error(f"**Total Gap for {selected}:** {total_penalty:.3f} kWh/Nm3 above Design.")

# --- 6. 10-COMPRESSOR LOADING ADVISORY ---
st.divider()
st.subheader("💨 GAN Compressor Network Strategy")
comp_cols = st.columns(10)
for i in range(1, 11):
    with comp_cols[i-1]:
        ctype = "MP" if i <= 4 else "LP"
        is_running = True if (i <= 4 or i <= 7) else False
        st.write(f"**{ctype}-{i}**")
        st.write("🟢" if is_running else "⚪")
        st.caption("100%" if i <= 4 else "75%" if is_running else "OFF")
