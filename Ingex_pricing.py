import streamlit as st

# --- 1. GITHUB LOGO INTEGRATION ---
def get_raw_github_url(repo_url, filepath):
    parts = repo_url.split("/")
    if len(parts) > 4:
        username, repo_name = parts[3], parts[4]
        return f"https://raw.githubusercontent.com/{username}/{repo_name}/main/{filepath}"
    return ""

repo_url = "https://github.com/surendalvi/Ingex/blob/main/logo.png"
logo_url = get_raw_github_url(repo_url, "logo.png")

# --- 2. PAGE CONFIG & UI ---
st.set_page_config(page_title="INGERO360AI Pricing", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main .block-container { padding: 0.8rem 2rem !important; max-width: 100%; height: 100vh; overflow: hidden; }
    .header-text { font-size: 26px; font-weight: 800; color: #031D44; margin-left: 10px; }
    h3 { font-size: 0.85rem !important; margin: 4px 0 !important; color: #031D44; text-transform: uppercase; }
    .pricing-card { background: #F8FAFC; padding: 0.8rem 1.2rem; border-radius: 12px; border: 1px solid #E2E8F0; }
    .big-price { font-size: 32px; font-weight: 900; color: #031D44; line-height: 1; }
    .label-text { font-size: 10px; color: #64748B; text-transform: uppercase; font-weight: 700; }
    .breakup-table { width: 100%; font-size: 11px; border-collapse: collapse; }
    .breakup-table td { padding: 2px 0; border-bottom: 1px solid #F1F5F9; }
    .val { text-align: right; font-weight: 700; color: #031D44; }
    div.stCheckbox > label { background: white; padding: 2px 8px !important; border: 1px solid #E2E8F0 !important; border-radius: 5px !important; }
    hr { margin: 0.4rem 0 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. DATA CONSTANTS ---
PLATFORM_FEE = 45000
SETUP_FEE = 25000
SERVICE_MO = 5000
USER_SLOT_FEE = 5000

PLANT_PORTFOLIO = {
    "Olefins/Ethylene": ["Furnace", "Quench", "CGC", "Acetylene Reactor", "Cold Section"],
    "Polymers (HDPE/LDPE/LLDPE)": ["Reactor", "Extruder", "Degassing Bin", "Catalyst Prep"],
    "Polymers (PVC/PET/PP/PC)": ["VCM Reactor", "Pelletizer", "Centrifuge", "Drier"],
    "Intermediates (EOEG/MTBE)": ["EO Reactor", "Glycol Column", "Etherification Unit"],
    "Specialties (Phenols/Acetone)": ["Cumene Unit", "Oxidation Reactor", "Cleavage Unit"],
    "Ammonia/Urea": ["Reformer", "CO2 Removal", "Synthesis Conv", "Prilling Tower"],
    "Refining": ["CDU/VDU", "FCCU", "Hydrocracker", "Delayed Coker"]
}

INITIATIVE_DATA = {
    "Plant Efficiency": "Dynamic Yield Benchmarking", "Soft sensors/Virtual Lab", "Fouling Forecast (Exchangers)", 
        "NOX/Emission Forecast", "Catalyst Health & Life Monitoring", "Real-time Optimization (RTO)",
    "Energy Optimization": "Driver Switchability (Steam vs Elec)", "Fuel/Steam Loss Reduction", "Steam Header Balancing", 
        "Energy Intensity (SEC) Tracking", "Utility Cost Sensitivity Analysis",
    "Reliability": "Failure Mode Library (>100+)", "Time to Failure (Remaining Life)", "Bad Actor Identification", 
        "Root Cause Analysis (RCA) Integration", "Vibration/Temp Correlation",
    "Asset Metric Hub": "Asset Management (TCO)", "Mean Time Between Failure (MTBF)", "Mean Time to Repair (MTTR)", 
        "Maintenance Cost Ineffectiveness", "ISO 55000 Compliance Tracking",
    "Sustainability": "Scope 1 & 2 Emission Monitoring", "Water and Waste Management", "Resource Efficiency", 
        "Carbon Intensity per Product Ton", "ESG Reporting Automation",
    "MLOPS": "Model Drift Detection", "Predictive Accuracy Metrics", "Inference Latency Tracking", 
        "Service Uptime Monitoring", "Automated Model Re-training Logs",
    "Workflows": "Alert Management & Statistics", "Automatic Workorder (CMMS) Creation", "Action Item Audit Trail"
}

# --- 4. TOP BAR ---
h_col1, h_col2, h_col3, h_col4 = st.columns([2, 3.2, 2, 2])
with h_col1:
    if logo_url:  st.image(logo_url, width=600)  # Adjust width to fit
with h_col2:
    st.markdown('<span style="font-weight:500; font-size:30px; color:#64748B;"> Product Pricing Catalogue</span>', unsafe_allow_html=True)
with h_col3:
    sector = st.selectbox("Industry Sector", list(PLANT_PORTFOLIO.keys()))
with h_col4:
    user_count = st.select_slider("User Licenses", options=[5, 10, 15, 20], value=5)
    total_user_fee = (user_count / 5) * USER_SLOT_FEE

st.markdown("---")

# --- 5. MAIN CONFIGURATION ---
col_left, col_right = st.columns([1.8, 1], gap="medium")

with col_left:
    st.markdown("### 1. Initiative & Multi-Asset Configuration")
    selected_config = {}
    
    for name, tooltips in INITIATIVE_DATA.items():
        with st.container():
            c1, c2 = st.columns([2, 2])
            with c1:
                # Use 'help' parameter for the hover effect (fixes the HTML code error)
                active = st.checkbox(name, value=(name == "Plant Efficiency"), key=f"act_{name}", help=tooltips)
            with c2:
                if active:
                    scope_type = st.radio("Scope", ["Assets", "Overall Plant"], horizontal=True, key=f"sc_{name}")
            
            if active:
                if scope_type == "Assets":
                    chosen_assets = st.multiselect(f"Units for {name}", PLANT_PORTFOLIO[sector], key=f"units_{name}")
                    f_count = 1
                    if "Furnace" in chosen_assets and "Olefins" in sector:
                        f_count = st.number_input(f"No. of Furnaces ({name})", 1, 20, 1, key=f"f_{name}")
                    
                    # Logic: 1st asset is base, others are additional
                    asset_count = max(1, (len([u for u in chosen_assets if u != "Furnace"]) + f_count))
                    selected_config[name] = {"type": "assets", "count": asset_count}
                else:
                    selected_config[name] = {"type": "overall", "count": 8}
        st.markdown("<div style='margin-bottom:-12px;'></div>", unsafe_allow_html=True)

with col_right:
    # --- 6. COSTING ENGINE ---
    total_setup = 0
    total_min_service = 0
    total_module_ari = 0
    
    for name, cfg in selected_config.items():
        # Scaling: First asset 0% extra, subsequent +20% scaling factor
        scaling = 1.0 + (max(0, cfg['count'] - 1) * 0.2)
        
        # PILOT FIX: First asset/initiative ARI is $0 to hit $105,000 exactly
        base_ari = 0 if len(selected_config) == 1 and cfg['count'] == 1 else 15000
        
        ari = base_ari * scaling
        if cfg['type'] == "overall": ari *= 0.8
        
        total_module_ari += ari
        total_setup += (cfg['count'] * SETUP_FEE)
        total_min_service += (cfg['count'] * SERVICE_MO * 6)

    total_y1 = PLATFORM_FEE + total_user_fee + total_module_ari + total_setup + total_min_service
    recurring_yr2 = PLATFORM_FEE + total_user_fee + total_module_ari

    # --- 7. SUMMARY DISPLAY ---
    st.markdown(f"""
        <div class="pricing-card">
            <p class="label-text">Year 1 Total Investment</p>
            <div class="big-price">${total_y1:,.0f}</div>
            <div style="border-top: 1px solid #E2E8F0; margin-top: 10px; padding-top: 8px;">
                <p class="label-text">Breakup</p>
                <table class='breakup-table'>
                    <tr><td>Platform Fee + Users ({user_count})</td><td class="val">${(PLATFORM_FEE + total_user_fee):,.0f}</td></tr>
                    <tr><td>Module ARI (Pilot Scale)</td><td class="val">${total_module_ari:,.0f}</td></tr>
                    <tr><td>One-Time Setup Fee</td><td class="val">${total_setup:,.0f}</td></tr>
                    <tr><td>Min. Service (6 Months)</td><td class="val">${total_min_service:,.0f}</td></tr>
                    <tr style="border-top: 1.5px solid #031D44;">
                        <td><b>Year 2+ Recurring (ARI)</b></td>
                        <td class="val" style="color:#031D44;"><b>${recurring_yr2:,.0f}</b></td>
                    </tr>
                </table>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("Service Charge Benefits"):
        st.caption("Includes: Model Tuning, Technical Advisory, Interface Health Monitoring, and Quarterly Training.")

    if st.button("Finalize INGEX Quote", use_container_width=True):
        st.success("Investment Profile Generated!")

st.markdown(f"<div style='text-align: center; color: #94A3B8; font-size: 10px; margin-top:8px;'>INGERO360AI by Ingenero | Powered by Digital Operations Group</div>", unsafe_allow_html=True)
