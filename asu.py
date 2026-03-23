import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="Jubail Regional Command Center", layout="wide")
st.title("🚀 Jubail Regional ASU Command Center")
st.markdown("### Integrated Optimizer Results, Demand Tracking & Gap Analysis")

# --- 2. GLOBAL DEMAND (SIDEBAR INPUTS) ---
with st.sidebar:
    st.header("📊 Regional Demand Settings")
    curr_gan_demand = st.slider("Current GAN Demand (Nm3/h)", 100000, 250000, 185000)
    curr_gox_demand = st.slider("Current GOX Demand (Nm3/h)", 20000, 80000, 45000)
    total_demand = curr_gan_demand + curr_gox_demand
    
    st.header("⚡ Economic Context")
    pwr_price = st.number_input("Power Price (SAR/MWh)", value=220)

# --- 3. REGIONAL DATA MODEL (Consolidated) ---
# This table represents the 'Single View' of the Optimizer's decisions
asu_data = pd.DataFrame({
    "ASU": ["ASU-41", "ASU-51", "ASU-71", "ASU-81", "ASU-91"],
    "Health_Index": [88, 82, 96, 62, 90],
    "Current_Flow": [45000, 48000, 55000, 42000, 50000],
    "Optimized_Target": [48000, 43000, 62000, 27000, 50000], # Sums to ~230k to meet demand
    "Current_MPC_HL": [52000, 55000, 60000, 48000, 65000],
    "New_MPC_HL": [55000, 50000, 65000, 35000, 66000],
    "SEC_Actual": [0.60, 0.62, 0.58, 0.74, 0.59],
    "Status": ["Stable", "Stable", "Pushing Limits", "Gap Identified", "Stable"]
})

# --- 4. TOP LEVEL: THE PRIZE & DEMAND TRACKING ---
st.header("🌍 Regional Strategy Summary")
total_opt_supply = asu_data["Optimized_Target"].sum()
energy_gap = (asu_data["SEC_Actual"].mean() - 0.575) * total_opt_supply / 1000 # MW

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Current Total Demand", f"{total_demand:,.0f} Nm3/h")
with c2:
    st.metric("Optimized Supply", f"{total_opt_supply:,.0f} Nm3/h", 
              delta=f"{total_opt_supply - total_demand:,.0f} Balance")
with c3:
    st.metric("Energy Opportunity Gap", f"{energy_gap:.2f} MW", delta="-8.1%", delta_color="normal")
with c4:
    daily_saving = energy_gap * 24 * (pwr_cost/1000)
    st.metric("Potential Saving", f"{daily_saving:,.0f} SAR/Day")

# --- 5. THE SINGLE VIEW: ALL ASU OPTIMIZER RESULTS ---
st.divider()
st.subheader("📋 Consolidated ASU Strategy Table")
st.write("Prescribed production targets and MPC limit adjustments to meet the current demand.")

# Color-coding logic for MPC adjustments
def highlight_limits(row):
    color = ''
    if row['New_MPC_HL'] > row['Current_MPC_HL']:
        color = 'background-color: #d4edda' # Green for pushing capacity
    elif row['New_MPC_HL'] < row['Current_MPC_HL']:
        color = 'background-color: #f8d7da' # Red for pulling back due to failure
    return [color] * len(row)

st.dataframe(
    asu_data.style.apply(highlight_limits, axis=1)
    .format({"Current_Flow": "{:,}", "Optimized_Target": "{:,}", "Current_MPC_HL": "{:,}", "New_MPC_HL": "{:,}"})
)

# --- 6. REGIONAL HEAT MAP & DRILL-DOWN ---
st.divider()
st.subheader("🗺️ Regional Health Heat Map")
fig_heat = px.bar(asu_data, x="ASU", y="Health_Index", color="Health_Index", 
                 hover_data=["SEC_Actual", "Status"],
                 color_continuous_scale='RdYlGn', text="Status")
st.plotly_chart(fig_heat, use_container_width=True)

selected_asu = st.selectbox("Select ASU for Equipment-Level Gap Identification:", asu_data["ASU"], index=3)

# --- 7. EQUIPMENT PERFORMANCE DRILL-DOWN ---
if selected_asu == "ASU-81":
    scores = [82, 55, 90, 45, 85, 92, 70, 65]
    impacts = [0.02, 0.08, 0.01, 0.12, 0.01, 0.01, 0.03, 0.04]
else:
    scores = [95, 94, 98, 92, 96, 99, 94, 95]
    impacts = [0.002] * 8

equip_df = pd.DataFrame({
    "Component": ["MAC", "Main HX", "Mol Sieves", "Expander", "Booster Comp", "Cold Box", "LP Column", "HP Column"],
    "Health Score (%)": scores,
    "SEC Penalty (kWh/Nm3)": impacts
})

d1, d2 = st.columns([2, 1])
with d1:
    fig_diag = px.bar(equip_df, x="Component", y="Health Score (%)", color="Health Score (%)",
                     range_y=[0, 100], color_continuous_scale='RdYlGn', title=f"{selected_asu} Component Health")
    st.plotly_chart(fig_diag, use_container_width=True)
with d2:
    st.write(f"**{selected_asu} Loss Attribution**")
    top_3 = equip_df.sort_values("SEC Penalty (kWh/Nm3)", ascending=False).head(3)
    for i, row in top_3.iterrows():
        st.warning(f"**{row['Component']}**: +{row['SEC_Penalty (kWh/Nm3)']:.3f} Penalty")
    
    total_penalty = equip_df['SEC Penalty (kWh/Nm3)'].sum()
    st.error(f"**Total Identifiable Gap:** {total_penalty:.3f} kWh/Nm3")

# --- 8. GAN COMPRESSOR LOADING ---
st.divider()
st.subheader("💨 Regional GAN Compressor Advisory (10 Units)")
c_cols = st.columns(10)
for i in range(1, 11):
    with c_cols[i-1]:
        label = "MP" if i <= 4 else "LP"
        # Load logic: MP always 100% if healthy
        load = "100%" if i <= 4 else "85%" if i <= 6 else "OFF"
        color = "🟢" if load != "OFF" else "⚪"
        st.write(f"**{label}-{i}**\n\n{color}\n\n{load}")
