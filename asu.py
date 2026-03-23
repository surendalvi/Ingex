import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. OVERALL OPPORTUNITY & GAP ---
st.header("💰 Regional Energy Gap & Opportunity")
col1, col2, col3 = st.columns(3)

# Mock Calculation
current_pwr = 145.5 # MW
opt_pwr = 138.2    # MW
gap = current_pwr - opt_pwr

col1.metric("Current Power", f"{current_pwr} MW", delta="High", delta_color="inverse")
col2.metric("Optimized Power", f"{opt_pwr} MW")
col3.metric("Opportunity (The Gap)", f"{gap:.1f} MW", delta="Saving Potential", delta_color="normal")

# --- 2. COMPRESSOR LOADING STRATEGY ---
st.subheader("💨 GAN Compressor Loading Strategy")
# Logic: MP first, then LP
comp_data = pd.DataFrame({
    'Compressor': [f'MP-{i}' for i in range(1,5)] + [f'LP-{i}' for i in range(1,7)],
    'Type': ['MP']*4 + ['LP']*6,
    'Efficiency': [92, 91, 89, 90, 82, 81, 80, 83, 79, 81],
    'Rec_Load': [100, 100, 100, 100, 85, 80, 0, 0, 0, 0] # Optimizer Output
})
st.dataframe(comp_data.style.background_gradient(subset=['Rec_Load'], cmap='Greens'))

# --- 3. ASU DRILL-DOWN (THE GAP IDENTIFIER) ---
st.divider()
st.subheader("🎯 ASU Health Drill-Down")
selected_asu = st.selectbox("Select ASU to investigate Gap:", ["ASU-41", "ASU-51", "ASU-71", "ASU-81", "ASU-91"])

# Equipment Health Data Model
# Values represent % deviation from 'Design' Performance (Negative is bad)
equip_health = {
    "MAC": -2.5,          # Fouled filters/intercoolers
    "Heat Exchanger": -5.0, # High WETD
    "Mol Sieves": -1.2,    # High Delta P
    "Expander": -8.0,      # Seal wear
    "Booster Comp": -0.5,
    "HP Column": -4.0,     # Tray fouling
    "LP Column": -0.2,
    "Cold Box": -1.5       # Insulation vacuum loss
}

st.write(f"### Diagnostic for {selected_asu}")
cols = st.columns(4)

# Loop through equipment to show performance vs impact
for i, (equip, health) in enumerate(equip_health.items()):
    with cols[i % 4]:
        color = "normal" if health > -2 else "inverse"
        impact = abs(health) * 0.05 # Simple heuristic: 1% health loss = 0.05 kWh/Nm3 penalty
        st.metric(equip, f"{health}%", delta=f"+{impact:.3f} SEC Impact", delta_color=color)

# Gap Summary Text
st.error(f"**Gap Analysis:** {selected_asu} is underperforming by **{sum(equip_health.values())/8:.1f}%** vs Design. "
         f"The primary bottleneck is the **Expander (-8.0%)**, which is forcing higher MAC power to maintain liquid levels.")
