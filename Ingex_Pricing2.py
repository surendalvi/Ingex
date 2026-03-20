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
    page_icon="💎",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- 3. PREMIUM CSS (FIXES SKEWING, ADDS SCROLLING & STICKY COLUMN) ---
st.markdown("""
    <style>
    .main .block-container { padding: 1rem 2rem !important; background-color: #F8FAFC; }
    
    .nav-header {
        display: flex; align-items: center; justify-content: space-between;
        padding: 12px 20px; background: white; border-radius: 12px;
        border: 1px solid #E2E8F0; margin-bottom: 10px;
    }

    /* THE FINANCIAL COMMAND CENTER */
    .executive-card {
        background: white; padding: 24px; border-radius: 16px;
        border-top: 5px solid #0F172A; border-left: 1px solid #E2E8F0;
        border-right: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 20px;
    }

    /* FIXING THE SKEW: Force Minimum Width on Columns */
    [data-testid="column"] {
        min-width: 250px !important;
        flex: 0 0 auto !important;
    }
    
    /* STICKY FIRST COLUMN (Initiative Labels) */
    [data-testid="stHorizontalBlock"] > div:first-child {
        min-width: 200px !important;
        max-width: 200px !important;
        position: sticky !important;
        left: 0 !important;
        z-index: 100 !important;
        background-color: #F8FAFC !important;
        border-right: 2px solid #E2E8F0 !important;
    }

    /* Metric Styling */
    [data-testid="stMetricValue"] { font-size: 32px !important; font-weight: 800 !important; color: #0F172A !important; }
    .stRadio > label { font-size: 11px !important; font-weight: 700 !important; color: #64748B !important; }
    </style>
""", unsafe_allow_html=True)

# --- 4. DETAILED DATA REPOSITORY ---
PLANT_PORTFOLIO = {
    "🏭 Olefins/Ethylene": ["Furnace", "Quench", "CGC", "Acetylene Reactor", "Cold Section"],
    "🧪 Polymers (PE/PP/PVC)": ["Reactor", "Extruder", "Degassing & Purge Bins", "VCM Recovery Unit", "Pelletizer"],
    "💧 Methanol/Ammonia": ["Reformer", "Synthesis Reactor", "CO2 Removal", "Distillaion Unit"],
    "🧩 Intermediates (EO/EG)": ["EO Reactor", "Glycol Column", "Etherification Unit"],
    "🧩 Intermediates (MTBE)": ["Butamer", "Catofin", "Synthesis"],
    "🧩 Intermediates (PHENOL)": ["Oxidation Reactors", "Cleavage Units", "Fractionation"],
    "🔧 Utility & Offsites": ["Boiler/Steam", "Cooling Tower", "Air Compressor", "Water Treatment", "Flare System"],
    "❄️ Air Separation (ASU)": ["Main Air Compressor (MAC)", "Purification Unit", "Cryogenic Cold Box", "Turbo-Expander",
        "Product Storage & Backup"],
    "⛽ Refining": ["CDU/VDU", "FCCU", "Hydrocracker", "Delayed Coker"]
}

INITIATIVE_HELP = {
    "📈 Efficiency": "Yield & Catalyst Optimization, Soft Sensors, Dynamic Benchmarking.",
    "⚡ Energy": "Steam Header Balancing, Fuel Loss Reduction, Furnace Excess Air Control.",
    "🛠️ Reliability": "100+ Failure Modes, Remaining Useful Life (RUL), Bad Actor Identification.",
    "🌱 Sustainability": "Scope 1/2 Monitoring, Carbon Intensity, Flare Loss Quantification.",
    "🔄 Workflows": "Digital Shift Handover, Automated Work-Orders, Alert Management."
}

# COST DEFINITION STRINGS
DESC_PLATFORM = "Annual digital foundation fee. Covers Cloud hosting, Cybersecurity, and Core SW updates."
DESC_SETUP = "One-time fee for implementation: Data ingestion, sensor tag mapping, and building the Digital Twin models."
DESC_ARI = "Subscription for AI Intelligence. Pays for the proprietary algorithms that predict failures and optimize yields 24/7."
DESC_SERVICE = "Human-in-the-loop support. Monthly performance reviews, SME advisory, and operator training/adoption."
DESC_ARI_VS_SERVICE = "ARI is for the 'Software Brain' (Automated Value); Service is for 'Human Expertise' (Advisory & Tuning)."

# --- 5. TOP BRANDING ---
st.markdown(f"""
    <div class="nav-header">
        <div style="display: flex; align-items: center;">
            <img src="{logo_url}" width="40">
            <div style="margin-left: 15px;">
                <div style="font-size:22px; font-weight:800; color:#0F172A;">INGERO360AI</div>
                <div style="font-size:10px; color:#64748B; font-weight:700;">TRANSPARENT ENTERPRISE MATRIX</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 6. SIDEBAR FLEET CONSTRUCTION ---
with st.sidebar:
    st.markdown("### 🏗️ Fleet Construction")
    sel_sectors = st.multiselect("Select Industry Sectors", list(PLANT_PORTFOLIO.keys()), default=["🏭 Olefins"])
    
    fleet_units = []
    for s in sel_sectors:
        qty = st.number_input(f"Qty: {s.split(' ')[1]}", 1, 10, 1, key=f"q_{s}")
        for i in range(qty):
            fleet_units.append({"name": f"{s.split(' ')[1]} #{i+1}", "sector": s, "id": f"{s}_{i}"})
    
    st.markdown("---")
    user_slots = st.selectbox("Global User Licenses", [5, 10, 15, 20], index=0)

# --- 7. PLACEHOLDER FOR CALCULATED SUMMARY ---
summary_container = st.container()

# --- 8. THE CONFIGURATION MATRIX ---
st.markdown("### 📋 Portfolio Configuration Matrix")
st.caption("👈 Initiative labels are locked. **Scroll Right** to configure all plants.")

matrix_configs = {}
for init_name, help_text in INITIATIVE_HELP.items():
    with st.container():
        cols = st.columns([1] + [1] * len(fleet_units))
        with cols[0]:
            is_active = st.checkbox(f"**{init_name}**", value=(init_name == "📈 Efficiency"), key=f"en_{init_name}", help=help_text)
        
        if is_active:
            row_data = []
            for idx, plant in enumerate(fleet_units):
                with cols[idx + 1]:
                    st.markdown(f"<p style='font-size:11px; color:#94A3B8; font-weight:700; margin-bottom:0px;'>{plant['name']}</p>", unsafe_allow_html=True)
                    sc = st.radio("Scope", ["Assets", "Overall"], horizontal=True, key=f"sc_{init_name}_{plant['id']}")
                    
                    if sc == "Assets":
                        chosen = st.multiselect("Select", PLANT_PORTFOLIO[plant['sector']], key=f"u_{init_name}_{plant['id']}")
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
            matrix_configs[init_name] = row_data
        st.divider()

# --- 9. CALCULATION ENGINE ---
PLATFORM_FEE, SETUP_FEE, SERVICE_MO = 45000, 25000, 5000
user_fee = (user_slots / 5) * 5000
total_fleet_size = len(fleet_units)
total_setup, total_service, total_ari = 0, 0, 0
num_active_inits = len(matrix_configs)

for init_name, plant_configs in matrix_configs.items():
    for p in plant_configs:
        scaling = 1.0 + (max(0, p['count'] - 1) * 0.2)
        base_ari = 0 if (num_active_inits == 1 and total_fleet_size == 1 and p['count'] == 1) else 15000
        p_ari = (base_ari * scaling * (1.0 + (max(0, num_active_inits - 1) * 0.25)))
        p_setup = (p['count'] * SETUP_FEE)
        p_service = (p['count'] * SERVICE_MO * 6)
        if p['type'] == "overall":
            p_ari *= 0.8; p_setup *= 0.8; p_service *= 0.8
        total_ari += p_ari; total_setup += p_setup; total_service += p_service

total_y1 = PLATFORM_FEE + user_fee + total_ari + total_setup + total_service
total_y2 = PLATFORM_FEE + user_fee + total_ari

# --- 10. RENDER TOP SUMMARY WITH DETAILED TOOLTIPS ---
with summary_container:
    st.markdown('<div class="executive-card">', unsafe_allow_html=True)
    m_col1, m_col2 = st.columns([1.5, 2.5])
    
    with m_col1:
        st.metric("Total Year 1 Investment", f"${total_y1:,.0f}", help=f"{DESC_PLATFORM} + {DESC_SETUP} + {DESC_ARI} + {DESC_SERVICE}")
        st.success(f"**Annual Recurring (Year 2+): ${total_y2:,.0f}**")
        st.caption(DESC_ARI_VS_SERVICE)
    
    with m_col2:
        st.markdown("<p style='font-size:11px; font-weight:800; color:#94A3B8; letter-spacing:1px;'>INVESTMENT BREAKUP</p>", unsafe_allow_html=True)
        b_col1, b_col2, b_col3 = st.columns(3)
        b_col1.metric("Capability ARI", f"${total_ari:,.0f}", help=DESC_ARI)
        b_col2.metric("Setup Fees", f"${total_setup:,.0f}", help=DESC_SETUP)
        b_col3.metric("Service (6mo)", f"${total_service:,.0f}", help=DESC_SERVICE)
        
        st.caption(f"Platform Fee + {user_slots} Seats: ${(PLATFORM_FEE + user_fee):,.0f} ( {DESC_PLATFORM} )")
    st.markdown('</div>', unsafe_allow_html=True)
