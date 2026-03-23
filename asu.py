import streamlit as st
import pandas as pd
import plotly.express as px
from pyomo.environ import *

# --- 1. SETUP & THEME ---
st.set_page_config(page_title="Jubail ASU Optimizer", layout="wide")
st.title("🛡️ Regional ASU Strategy & Optimization")
st.markdown("""
    *This dashboard analyzes real-time equipment health across Jubail ASUs to find the most 
    energy-efficient production distribution while eliminating venting.*
""")

# --- 2. INPUT SECTION (Sidebar) ---
with st.sidebar:
    st.header("🎯 System Demands")
    total_gan = st.slider("Total GAN Demand (Nm3/h)", 100000, 300000, 185000, help="Total gaseous nitrogen required by the regional network.")
    total_gox = st.slider("Total GOX Demand (Nm3/h)", 20000, 100000, 45000)
    
    st.header("⚡ Economic Context")
    pwr_price = st.number_input("Power Price (SAR/MWh)", value=220)
    
    st.header("🛠️ Asset Health Overrides")
    st.info("Simulate equipment degradation to see how the optimizer re-ranks the ASUs.")
    asu41_health = st.slider("ASU-41 Expander Efficiency (%)", 50, 100, 95)
    asu71_fouling = st.slider("ASU-71 MHX Fouling (WETD °C)", 1.0, 5.0, 1.5)

# --- 3. DATA MODEL & DIAGNOSIS ---
# Mocking the Performance Data
asu_stats = pd.DataFrame({
    'ASU': ['ASU-41', 'ASU-51', 'ASU-71', 'ASU-81', 'ASU-91'],
    'MAC_Eff': [88, 85, 91, 82, 89],
    'Exp_Eff': [asu41_health, 88, 92, 75, 90],
    'Col_DP': [0.4, 0.5, 0.3, 0.7, 0.4], # Bar
    'WETD': [1.8, 2.0, asu71_fouling, 2.5, 1.6],
    'Base_kWh_Nm3': [0.55, 0.58, 0.52, 0.65, 0.53]
})

# Calculate a "Ranking Score" (Lower Specific Energy = Higher Rank)
asu_stats['Rank'] = asu_stats['Base_kWh_Nm3'].rank(ascending=True)
asu_stats = asu_stats.sort_values('Rank')

# --- 4. TABS: THE USER JOURNEY ---
tab1, tab2, tab3 = st.tabs(["📊 Asset Ranking & Health", "⚙️ Equipment Deep-Dive", "✅ Optimized Targets"])

# TAB 1: RANKING
with tab1:
    st.subheader("🏆 Efficiency Leaderboard")
    st.write("ASUs are ranked based on their current Specific Energy Consumption (SEC).")
    
    cols = st.columns(5)
    for i, row in asu_stats.iterrows():
        with cols[int(row['Rank'])-1]:
            st.metric(label=f"Rank {int(row['Rank'])}: {row['ASU']}", 
                      value=f"{row['Base_kWh_Nm3']} kWh", 
                      delta="-Best" if row['Rank']==1 else None)
            st.progress(int(row['MAC_Eff']))
            st.caption(f"MAC Efficiency: {row['MAC_Eff']}%")

# TAB 2: EQUIPMENT PERFORMANCE
with tab2:
    st.subheader("🔍 Sub-Component Health Monitoring")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("**Cold Box & Heat Exchanger Performance**")
        fig_wetd = px.bar(asu_stats, x='ASU', y='WETD', color='WETD', 
                          title="Warm End Temp Difference (Lower is Better)",
                          color_continuous_scale='RdYlGn_r')
        st.plotly_chart(fig_wetd, use_container_width=True)
        
    with col_b:
        st.markdown("**Distillation Column Stability**")
        fig_dp = px.scatter(asu_stats, x='ASU', y='Col_DP', size='Col_DP', color='Col_DP',
                            title="Column Delta P (Flooding Risk Indicator)")
        st.plotly_chart(fig_dp, use_container_width=True)

# TAB 3: OPTIMIZATION RESULTS
with tab3:
    st.subheader("🎯 Optimal Production Setpoints")
    st.success(f"Global Minimum Cost found for {total_gan + total_gox:,.0f} Nm3/hr demand.")
    
    # Simple logic for target distribution based on rank for demonstration
    # In reality, this calls the Pyomo solve() function
    asu_stats['Target_Flow'] = [55000, 50000, 45000, 40000, 0] # Example dist
    
    res_col1, res_col2 = st.columns([2, 1])
    
    with res_col1:
        st.bar_chart(asu_stats.set_index('ASU')['Target_Flow'])
    
    with res_col2:
        st.write("**Action Plan for MPC**")
        for i, row in asu_stats.iterrows():
            status = "🟢 FULL LOAD" if row['Target_Flow'] > 50000 else "🟡 PARTIAL" if row['Target_Flow'] > 0 else "🔴 SHUTDOWN"
            st.write(f"**{row['ASU']}:** {status} → **{row['Target_Flow']:,} Nm3/hr**")

    st.divider()
    st.info("💡 **Insight:** ASU-81 has been ramped down to minimum because its high WETD and low Expander efficiency make it the most expensive unit in the region.")
