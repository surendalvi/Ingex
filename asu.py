import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. SETTINGS & TITLE ---
st.set_page_config(page_title="Jubail ASU Command Center", layout="wide")
st.title("🚀 Jubail Regional ASU Command Center")
st.markdown("### Regional Strategy, Demand Tracking & Gap Identification")

# --- 2. SIDEBAR: GLOBAL INPUTS ---
with st.sidebar:
    st.header("📊 Regional Demand Settings")
    # Using 'pwr_cost' consistently to avoid NameErrors
    pwr_cost = st.number_input("Power Price (SAR/MWh)", value=220)
    
    st.header("📍 System Demand")
    # Sliders for real-time demand simulation
    curr_gan_demand = st.slider("Current GAN Demand (Nm3/h)", 100000, 300000, 185000)
    curr_gox_demand = st.slider("Current GOX Demand (Nm3/h)", 20000, 100000, 45000)
    total_demand = curr_gan_demand + curr_gox_demand

# --- 3. THE DATA MODEL (ALL ASU VIEW) ---
asu_list = ["ASU-41", "ASU-51", "ASU-71", "ASU-81", "ASU-91"]
asu_data = pd.DataFrame({
    "ASU": asu_list,
    "Health_Index": [88, 82, 96, 62, 90],
    "Current_Flow": [45000, 48000, 55000, 42000, 50000],
    "Optimized_Target": [48000, 43000, 62000, 27000, 50000], # Sums to meet demand
    "Current_MPC_HL": [52000, 55000, 60000, 48000, 65000],
    "New_MPC_HL": [55000, 50000, 65000, 35000, 66000],
    "SEC_Actual": [0.60, 0.62, 0.58, 0.74, 0.59],
    "Status": ["Stable", "Stable", "Pushing Limits", "Gap Identified", "Stable"]
})

# --- 4. TOP LEVEL: REGIONAL OPPORTUNITY ---
st.header("🌍 Regional Strategy Summary")
total_opt_supply = asu_data["Optimized_Target"].sum()
# Energy gap calculation relative to a 0.575 benchmark
energy_gap_mw = (asu_data["SEC_Actual"].mean() - 0.575) * total_opt_supply / 1000 

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Total Regional Demand", f"{total_demand:,.0f} Nm3/h")
with c2:
    st.metric("Optimized Supply", f"{total_opt_supply:,.0f} Nm3/h", 
              delta=f"{total_opt_supply - total_demand:,.0f} Balance")
with c3:
    st.metric("Energy Gap", f"{energy_gap_mw:.2f} MW", delta="-8.1%", delta_color="normal")
with c4:
    daily_saving = energy_gap_mw * 24 * (pwr_cost / 1000)
    st.metric("Potential Saving", f"{daily_saving:,.0f} SAR/Day")

# --- 5. THE SINGLE VIEW: ALL ASU OPTIMIZER RESULTS ---
st.divider()
st.subheader("📋 Consolidated ASU Strategy Table")
st.write("Prescribed production targets and MPC limit adjustments for all units.")

# Highlight limits: Green for increase, Red for decrease
def highlight_limits(row):
    color = ''
    if row['New_MPC_HL'] > row['Current_MPC_HL']:
        color = 'background-color: #d4edda' # Light Green
    elif row['New_MPC_HL'] < row['Current_MPC_HL']:
        color = 'background-color: #f8d7da' # Light Red
    return [color] * len(row)

st.dataframe(
    asu_data.style.apply(highlight_limits, axis=1)
    .format({"Current_Flow": "{:,}", "Optimized_Target": "{:,}", "Current_MPC_HL": "{:,}", "New_MPC_HL": "{:,}"})
)

# --- 6. REGIONAL HEALTH HEAT MAP ---
st.divider()
st.subheader("🗺️ Regional Health Heat Map")
fig_heat = px.bar(asu_data, x="ASU", y="Health_Index", color="Health_Index", 
                 hover_data=["SEC_Actual", "Status"],
                 color_continuous_scale='RdYlGn', text="Status")
st.plotly_chart(fig_heat, use_container_width=True)

# Selector for individual ASU analysis
selected_asu = st.selectbox("Select ASU to investigate Equipment Performance:", asu_list, index=3)

# --- 7. EQUIPMENT PERFORMANCE DRILL-DOWN ---
# Define specific data for the selected ASU
if selected_asu == "ASU-81":
    h_scores = [82, 55, 90, 45, 85, 92, 70, 65]
    penalties = [0.02, 0.08, 0.01, 0.12, 0.01, 0.01, 0.03, 0.04]
else:
    h_scores = [95, 94, 98, 92, 96, 99, 94, 95]
    penalties = [0.002] * 8

# Consistent column names to avoid KeyError
equip_df = pd.DataFrame({
    "Equipment": ["MAC", "Main HX", "Mol Sieves", "Expander", "Booster Comp", "Cold Box", "LP Column", "HP Column"],
    "Health_Score": h_scores,
    "SEC_Penalty": penalties
})

d1, d2 = st.columns([2, 1])
with d1:
    st.write(f"#### {selected_asu} Component Health Status")
    fig_diag = px.bar(equip_df, x="Equipment", y="Health_Score", color="Health_Score",
                     range_y=[0, 100], color_continuous_scale='RdYlGn')
    st.plotly_chart(fig_diag, use_container_width=True)
with d2:
    st.write(f"#### {selected_asu} Loss Attribution")
    # Identify the biggest contributors to the energy gap
    top_gaps = equip_df.sort_values("SEC_Penalty", ascending=False).head(3)
    for index, row in top_gaps.iterrows():
        st.warning(f"**{row['Equipment']}**: +{row['SEC_Penalty']:.3f} Penalty")
    
    total_penalty = equip_df['SEC_Penalty'].sum()
    st.error(f"**Total Gap Identified:** {total_penalty:.3f} kWh/Nm3")

# --- 8. GAN COMPRESSOR ADVISORY ---
st.divider()
st.subheader("💨 Regional GAN Compressor Advisory (10 Units)")
comp_cols = st.columns(10)
for i in range(1, 11):
    with comp_cols[i-1]:
        label = "MP" if i <= 4 else "LP"
        load = "100%" if i <= 4 else "85%" if i <= 6 else "OFF"
        color = "🟢" if load != "OFF" else "⚪"
        st.write(f"**{label}-{i}**\n\n{color}\n\n{load}")
