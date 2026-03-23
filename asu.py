import streamlit as st
import pandas as pd
import numpy as np
from pyomo.environ import *

# --- 1. Dashboard Configuration ---
st.set_page_config(page_title="Jubail ASU Regional Optimizer", layout="wide")
st.title("🏭 Jubail Regional ASU Network Optimizer")
st.markdown("Optimization of ASUs 41, 51, 71, 81, & 91 to minimize venting and energy.")

# --- 2. Sidebar: Inputs & Demand ---
st.sidebar.header("Global Demand Inputs")
gan_demand = st.sidebar.slider("GAN Demand (Nm3/hr)", 100000, 250000, 180000)
gox_demand = st.sidebar.slider("GOX Demand (Nm3/hr)", 20000, 80000, 45000)
power_cost = st.sidebar.number_input("Power Cost (SAR/MWh)", value=220)

st.sidebar.header("Economic Penalties")
vent_penalty = st.sidebar.number_input("Venting Penalty (High)", value=5000)
makeup_penalty = st.sidebar.number_input("Liquid Makeup Penalty", value=8000)

# --- 3. Asset Data (The Data Model) ---
# In a real app, this comes from your SQL/Historian Data Model
asu_data = {
    'ASU-41': {'min': 25000, 'max': 52000, 'coeff': 0.0006, 'fixed': 1200},
    'ASU-51': {'min': 28000, 'max': 55000, 'coeff': 0.0005, 'fixed': 1100},
    'ASU-71': {'min': 30000, 'max': 60000, 'coeff': 0.0004, 'fixed': 1400},
    'ASU-81': {'min': 20000, 'max': 48000, 'coeff': 0.0007, 'fixed': 1000},
    'ASU-91': {'min': 35000, 'max': 65000, 'coeff': 0.0004, 'fixed': 1300},
}

# --- 4. Optimization Engine (Pyomo) ---
def run_optimization(gan_req, gox_req):
    model = ConcreteModel()
    model.ASUS = Set(initialize=asu_data.keys())
    
    # Variables
    model.flow = Var(model.ASUS, domain=NonNegativeReals)
    model.is_on = Var(model.ASUS, domain=Binary)
    
    # Objective: Minimize Sum of (Power Consumption)
    def obj_rule(model):
        return sum((asu_data[i]['coeff'] * model.flow[i]**2 + asu_data[i]['fixed']) * model.is_on[i] for i in model.ASUS)
    model.obj = Objective(rule=obj_rule, sense=minimize)
    
    # Constraint: Total Flow = GAN + GOX Demand
    model.demand_con = Constraint(expr=sum(model.flow[i] for i in model.ASUS) == (gan_req + gox_req))
    
    # Constraints: Capacity & Status
    def cap_min_rule(model, i):
        return model.flow[i] >= asu_data[i]['min'] * model.is_on[i]
    model.c1 = Constraint(model.ASUS, rule=cap_min_rule)
    
    def cap_max_rule(model, i):
        return model.flow[i] <= asu_data[i]['max'] * model.is_on[i]
    model.c2 = Constraint(model.ASUS, rule=cap_max_rule)
    
    # Solve (Requires local solver like 'ipopt' or 'glpk')
    try:
        opt = SolverFactory('mindtpy')
        opt.solve(model, strategy='OA', mip_solver='glpk', nlp_solver='ipopt')
        
        results = []
        for i in model.ASUS:
            results.append({
                "ASU": i,
                "Status": "ON" if value(model.is_on[i]) > 0.5 else "OFF",
                "Target Flow (Nm3/hr)": round(value(model.flow[i]), 0),
                "Est. Power (kW)": round((asu_data[i]['coeff'] * value(model.flow[i])**2 + asu_data[i]['fixed']) if value(model.is_on[i]) > 0.5 else 0, 2)
            })
        return pd.DataFrame(results)
    except:
        # Fallback if solver isn't installed for demo purposes
        st.warning("Solver not found. Displaying heuristic-based approximation.")
        return pd.DataFrame([{"ASU": i, "Status": "Demo", "Target Flow (Nm3/hr)": (gan_req+gox_req)/5, "Est. Power (kW)": 5000} for i in asu_data.keys()])

# --- 5. Main Dashboard Display ---
if st.button('🚀 Run Regional Optimizer'):
    df_results = run_optimization(gan_demand, gox_demand)
    
    # Top Row Metrics
    col1, col2, col3 = st.columns(3)
    total_power = df_results['Est. Power (kW)'].sum()
    col1.metric("Total Power Consumption", f"{total_power:,.0f} kW")
    col2.metric("Total Regional Flow", f"{(gan_demand + gox_demand):,.0f} Nm3/hr")
    col3.metric("Avg Specific Energy", f"{(total_power/(gan_demand+gox_demand)):.3f} kWh/Nm3")

    st.divider()

    # Visualization
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader("Optimal Production Distribution")
        st.bar_chart(df_results.set_index('ASU')['Target Flow (Nm3/hr)'])
    
    with c2:
        st.subheader("Asset Status")
        st.table(df_results[['ASU', 'Status', 'Target Flow (Nm3/hr)']])

    # MPC Setpoint Recommendations
    st.subheader("📥 Recommended MPC Targets")
    st.dataframe(df_results.style.highlight_max(axis=0, subset=['Target Flow (Nm3/hr)'], color='#2E7D32'))

else:
    st.info("Adjust the sliders in the sidebar and click 'Run Regional Optimizer' to calculate the best load distribution.")
