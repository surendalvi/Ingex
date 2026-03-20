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

# --- 2. PAGE CONFIG ---
st.set_page_config(
    page_title="INGERO360AI Executive", 
    page_icon="🏗️",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- 3. THE "GLOBAL SCALE" CSS ---
st.markdown("""
    <style>
    .main .block-container { padding: 1rem 2rem !important; background-color: #F8FAFC; }
    
    .nav-header {
        display: flex; align-items: center; justify-content: space-between;
        padding: 12px 20px; background: white; border-radius: 12px;
        border: 1px solid #E2E8F0; margin-bottom: 10px;
    }

    .executive-card {
        background: white; padding: 24px; border-radius: 16px;
        border-top: 5px solid #0F172A; border: 1px solid #E2E8F0;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 20px;
    }

    /* PREVENT SKEWING & ENABLE SCROLL */
    [data-testid="column"] {
        min-width: 260px !important;
        flex: 0 0 auto !important;
    }
    
    /* STICKY INITIATIVE COLUMN */
    [data-testid="stHorizontalBlock"] > div:first-child {
        min-width: 220px !important;
        max-width: 220px !important;
        position: sticky !important;
        left: 0 !important;
        z-index: 100 !important;
        background-color: #F8FAFC !important;
        border-right: 3px solid #0F172A !important;
    }

    [data-testid="stMetricValue"] { font-size: 30px !important; font-weight: 800 !important; color: #0F172A !important; }
    .stRadio > label { font-size: 11px !important; font-weight: 800 !important; color: #475569 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 4. EXPANDED PORTFOLIO REPOSITORY ---
PLANT_PORTFOLIO = {
    "🏭 Olefins/Ethylene": ["Furnace", "Quench TLE", "CGC", "Acetylene Reactor", "Cold Box", "C2/C3 Splitters"],
    "💧 Methanol": ["Steam Reformer", "SynGas Compressor", "Methanol Converter", "Distillation Train"],
    "🌬️ Ammonia": ["Primary Reformer", "Shift Converter", "CO2 Stripper", "Ammonia Converter", "Refrigeration Unit"],
    "🧪 Polymers (PE/PP)": ["Polymerization Reactor", "Extruder", "Pelletizer", "Degassing Bin", "Cycle Gas Comp"],
    "🧬 EO/EG": ["EO Reactor", "EO Stripper", "Glycol Column", "Cycle Gas Compressor", "Re-run Column"],
    "⚗️ MTBE": ["Synthesis Reactor", "Catalyst Bed", "Methanol Recovery Column", "Debutanizer"],
    "💎 Phenols": ["Cumene Oxidation Reactor", "Cleavage Unit", "Fractionation Train", "Hydrogenation Unit"],
    "⛽ Refining (CDU/VDU)": ["Atmospheric Column", "Desalter", "Vacuum Tower", "Ejector System", "Pre-heat Train"],
    "🧱 Delayed Coker": ["Coker Furnace", "Coke Drums", "Fractionator", "Wet Gas Compressor"],
    "🔥 FCCU": ["Reactor", "Regenerator", "Main Column", "Air Blower", "Power Recovery Turbine"],
    "❄️ ASU": ["Main Air Compressor", "Cold Box", "Turbo-Expander", "PPU (Purification)"],
    "🔧 Utilities": ["HP/MP Boilers", "Cooling Tower Fans", "DM Water Plant", "Flare System", "Air Compressors"]
}

INITIATIVE_DETAILS = {
    "📈 Plant Efficiency": """
    • Yield Optimization: Real-time tracking of high-value product recovery.
    • Catalyst Health: Monitoring activity levels and deactivation rates.
    • Soft Sensors: Inferential quality predictors for lab-free monitoring.
    • Heat Integration: Tracking fouling in exchangers and TLEs.
    """,
    "⚡ Energy & Utilities": """
    • Steam Balancing: Optimization of high, medium, and low-pressure headers.
    • Fuel Management: Maximizing fuel gas efficiency and reducing flaring.
    • Furnace/Boiler Efficiency: Real-time excess air and stack loss control.
    • Specific Power: Optimization of large compressors and turbines.
    """,
    "🛠️ Asset Reliability": """
    • 100+ Failure Templates: Pre-built models for pumps, seals, and bearings.
    • RUL (Remaining Useful Life): Predicting time-to-failure for critical assets.
    • Bad Actor ID: Identifying recurring maintenance bottlenecks.
    • RCA (Root Cause): Data-driven diagnostics for trip events.
    """,
    "🌱 Sustainability": """
    • Scope 1 & 2 Emissions: Continuous tracking of CO2 equivalent footprints.
    • Carbon Intensity: Real-time monitoring of emissions per ton of product.
    • Flare Quantification: Automated tracking of hydrocarbon loss to flare.
    • Water Intensity: Monitoring efficiency of DM and cooling water circuits.
    """,
    "🔄 Digital Workflows": """
    • Shift Handover: Automated summary of KPIs and bypass events.
    • Auto-Workorders: Integration with CMMS (SAP/EAM) based on AI alerts.
    • Knowledge Base: Digital repository of historical operating incidents.
    • Alert Management: Intelligent filtering of DCS nuisance alarms.
    """
}

# --- 5. TOP BRANDING ---
st.markdown(f"""
    <div class="nav-header">
        <div style="display: flex; align-items: center;">
            <img src="{logo_url}" width="40">
            <div style="margin-left: 15px;">
                <div style="font-size:20px; font-weight:800; color:#0F172A;">INGERO360AI</div>
                <div style="font-size:10px; color:#64748B; font-weight:700;">STRATEGIC PORTFOLIO MATRIX V35</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 6. SIDEBAR ---
with st.sidebar:
    st.markdown("### 🏗️ Fleet Construction")
    sel_sectors = st.multiselect("Active Plant Sectors", list(PLANT_PORTFOLIO.keys()), default=["🏭 Olefins/Ethylene"])
    
    fleet_units = []
    for s in sel_sectors:
        qty = st.number_input(f"Qty: {s.split(' ')[1]}", 1, 15, 1, key=f"q_{s}")
        for i in range(qty):
            fleet_units.append({"name": f"{s.split(' ')[1]} #{i+1}", "sector": s, "id": f"{s}_{i}"})
    
    st.markdown("---")
    user_slots = st.selectbox("Global User Seats", [5, 10, 15, 20], index=0)

# --- 7. TOP INVESTMENT SUMMARY ---
summary_placeholder = st.container()

# --- 8. CONFIGURATION MATRIX ---
st.markdown("### 📋 Portfolio Configuration Matrix")
st.caption("👈 Initiative labels are locked. **Scroll Right** to map assets across the entire fleet.")

if not fleet_units:
    st.warning("Define your fleet in the sidebar to populate the matrix.")
    st.stop()

matrix_results = {}
for init_name, help_text in INITIATIVE_DETAILS.items():
    with st.container():
        cols = st.columns([1] + [1] * len(fleet_units))
        with cols[0]:
            is_active = st.checkbox(f"**{init_name}**", value=(init_name == "📈 Plant Efficiency"), key=f"en_{init_name}", help=help_text)
        
        if is_active:
            row_data = []
            for idx, plant in enumerate(fleet_units):
                with cols[idx + 1]:
                    st.markdown(f"<p style='font-size:11px; color:#94A3B8; font-weight:800; margin-bottom:0px;'>{plant['name']}</p>", unsafe_allow_html=True)
                    sc = st.radio("Scope", ["Assets", "Overall"], horizontal=True, key=f"sc_{init_name}_{plant['id']}")
                    
                    if sc == "Assets":
                        chosen = st.multiselect("Units", PLANT_PORTFOLIO[plant['sector']], key=f"u_{init_name}_{plant['id']}")
                        f_cnt = 0
                        if "Furnace" in chosen and "Olefins" in plant['sector']:
                            f_cnt = st.number_input("Furnaces", 1, 30, 1, key=f"f_{init_name}_{plant['id']}")
                        count = max(1, len([u for u in chosen if u != "Furnace"]) + f_cnt)
                        row_data.append({"type": "asset", "count": count})
                    else:
                        base_count = 8
                        if "Olefins" in plant['sector']:
                            f_ov = st.number_input("Furnaces", 1, 30, 1, key=f"fov_{init_name}_{plant['id']}")
                            base_count = 4 + f_ov
                        row_data.append({"type": "overall", "count": base_count})
            matrix_results[init_name] = row_data
        st.divider()

# --- 9. PRICING ENGINE ---
PLATFORM_FEE, SETUP_FEE, SERVICE_MO = 45000, 25000, 5000
user_fee = (user_slots / 5) * 5000
total_fleet = len(fleet_units)
total_setup, total_service, total_ari = 0, 0, 0
num_active_inits = len(matrix_results)

for init_name, plant_configs in matrix_results.items():
    for p in plant_configs:
        scaling = 1.0 + (max(0, p['count'] - 1) * 0.2)
        base_ari = 0 if (num_active_inits == 1 and total_fleet == 1 and p['count'] == 1) else 15000
        p_ari = (base_ari * scaling * (1.0 + (max(0, num_active_inits - 1) * 0.25)))
        p_setup = (p['count'] * SETUP_FEE)
        p_service = (p['count'] * SERVICE_MO * 6)
        if p['type'] == "overall":
            p_ari *= 0.8; p_setup *= 0.8; p_service *= 0.8
        total_ari += p_ari; total_setup += p_setup; total_service += p_service

total_y1 = PLATFORM_FEE + user_fee + total_ari + total_setup + total_service
total_y2 = PLATFORM_FEE + user_fee + total_ari

# --- 10. EXECUTIVE SUMMARY TOOLTIPS ---
with summary_placeholder:
    st.markdown('<div class="executive-card">', unsafe_allow_html=True)
    m_col1, m_col2 = st.columns([1.5, 2.5])
    
    with m_col1:
        st.metric("Total Year 1 Investment", f"${total_y1:,.0f}", help="Sum of core platform, seat licenses, scaled module ARI, one-time setup, and advisory services.")
        st.success(f"**Annual Recurring (Year 2+): ${total_y2:,.0f}**")
    
    with m_col2:
        st.markdown("<p style='font-size:11px; font-weight:800; color:#94A3B8; letter-spacing:1px;'>INVESTMENT BREAKUP</p>", unsafe_allow_html=True)
        b1, b2, b3 = st.columns(3)
        b1.metric("Capability ARI", f"${total_ari:,.0f}", help="Software subscription fee for AI modules, scaled by asset complexity and initiative synergy.")
        b2.metric("Setup Fees", f"${total_setup:,.0f}", help="One-time cost for data mapping, sensor integration, and digital twin model construction.")
        b3.metric("Service (6mo)", f"${total_service:,.0f}", help="Human-in-the-loop technical advisory and algorithmic tuning for the first 6 months.")
        st.caption(f"Platform + {user_slots} Seats: ${(PLATFORM_FEE + user_fee):,.0f}")
    st.markdown('</div>', unsafe_allow_html=True)
