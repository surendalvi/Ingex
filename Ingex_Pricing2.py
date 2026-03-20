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
st.set_page_config(page_title="INGERO360AI Executive", page_icon="🏗️", layout="wide")

# --- 3. THE "STICKY RESULTS" CSS ---
st.markdown("""
    <style>
    .main .block-container { padding: 1rem 2rem !important; background-color: #F8FAFC; }
    
    /* Branding Header - Not Sticky */
    .nav-header {
        display: flex; align-items: center; padding: 12px 20px; 
        background: white; border-radius: 12px; border: 1px solid #E2E8F0;
        margin-bottom: 10px;
    }

    /* THE FIX: PINNED FINANCIAL CARD */
    /* This targets the container holding the summary and pins it to the top */
    div:has(> .executive-card) {
        position: sticky !important;
        top: 0 !important;
        z-index: 1000 !important;
        background-color: #F8FAFC !important;
        padding-top: 5px;
        padding-bottom: 15px;
    }

    .executive-card {
        background: white; padding: 20px; border-radius: 16px;
        border-top: 5px solid #0F172A; border: 1px solid #E2E8F0;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);
    }

    /* STICKY LEFT COLUMN (Plant Names) */
    [data-testid="column"]:first-child {
        position: sticky !important;
        left: 0 !important;
        z-index: 99 !important;
        background-color: #F8FAFC !important;
        border-right: 3px solid #0F172A !important;
        padding-right: 15px !important;
    }

    /* PREVENT SKEWING: Force columns to stay wide */
    [data-testid="column"] {
        min-width: 280px !important;
        flex: 0 0 auto !important;
    }

    /* UI Polishing */
    [data-testid="stMetricValue"] { font-size: 28px !important; font-weight: 800 !important; color: #0F172A !important; }
    .stRadio > label { font-size: 11px !important; font-weight: 800 !important; color: #475569 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 4. EXPANDED PORTFOLIO REPOSITORY ---
PLANT_PORTFOLIO = {
    "🏭 Olefins/Ethylene": ["Furnace", "Quench TLE", "CGC", "Acetylene Reactor", "Cold Box", "C2/C3 Splitters"],
    "💧 Methanol": ["Steam Reformer", "SynGas Compressor", "Methanol Converter", "Distillation Train"],
    "🌬️ Ammonia": ["Primary Reformer", "Shift Converter", "CO2 Stripper", "Synthesis Loop", "Refrigeration Unit"],
    "🧬 EO/EG": ["EO Reactor", "EO Stripper", "Glycol Column", "Cycle Gas Compressor", "Re-run Column"],
    "⚗️ MTBE": ["Synthesis Reactor", "Catalyst Bed", "Methanol Recovery Column", "Debutanizer"],
    "💎 Phenols": ["Oxidation Reactor", "Cleavage Unit", "Fractionation Train", "Hydrogenation Unit"],
    "🧪 Polymers": ["Polymerization Reactor", "Extruder", "Pelletizer", "Degassing Bin"],
    "⛽ Refining": ["CDU", "VDU", "Delayed Coker", "FCCU", "Hydrocracker"],
    "❄️ ASU": ["Main Air Compressor", "Cold Box", "Turbo-Expander", "PPU"],
    "🔧 Utilities": ["HP/MP Boilers", "Cooling Tower Fans", "DM Water Plant", "Flare System", "Air Compressors"]
}

INITIATIVE_DETAILS = {
    "📈 Efficiency": "Yield Optimization, Catalyst Health, Soft Sensors, Heat Integration.",
    "⚡ Energy": "Steam Balancing, Fuel Gas Optimization, Boiler Efficiency, Specific Power.",
    "🛠️ Reliability": "100+ Failure Templates, RUL Prediction, Bad Actor ID, RCA Diagnostics.",
    "🌱 Sustainability": "Scope 1/2 Tracking, Carbon Intensity Index, Flare Loss, Water Intensity.",
    "🔄 Workflows": "Digital Shift Handover, Auto-Workorders, Alert Mgmt, Knowledge Repository"
}

# COST TOOLTIPS
COST_HELP = {
    "Setup": "One-time cost for data mapping, sensor integration, and Digital Twin construction.",
    "Platform": "Annual license for Cloud hosting, Cyber-security, and Software updates.",
    "Service": "Human expertise: Monthly SME advisory, AI tuning, and operator training.",
    "ARI": "Algorithmic Subscription: Pays for the 24/7 automated intelligence and ROI generation."
}

# --- 5. TOP BRANDING ---
st.markdown(f"""
    <div class="nav-header">
        <img src="{logo_url}" width="38">
        <div style="margin-left: 15px;">
            <div style="font-size:18px; font-weight:800; color:#0F172A;">INGERO360AI</div>
            <div style="font-size:9px; color:#64748B; font-weight:700; letter-spacing:1px;">EXECUTIVE PORTFOLIO MATRIX</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 6. SIDEBAR ---
with st.sidebar:
    st.markdown("### 🏗️ Fleet Construction")
    sel_sectors = st.multiselect("Select Plant Sectors", list(PLANT_PORTFOLIO.keys()), default=["🏭 Olefins/Ethylene"])
    fleet_units = []
    for s in sel_sectors:
        qty = st.number_input(f"Qty: {s.split(' ')[1]}", 1, 15, 1, key=f"q_{s}")
        for i in range(qty):
            fleet_units.append({"name": f"{s.split(' ')[1]} #{i+1}", "sector": s, "id": f"{s}_{i}"})
    st.markdown("---")
    user_slots = st.selectbox("Global User Seats", [5, 10, 15, 20], index=0)

# --- 7. STICKY INVESTMENT SUMMARY ---
# We use a container to wrap the calculation and the card
summary_placeholder = st.container()

# --- 8. CONFIGURATION MATRIX (PLANTS IN ROWS) ---
st.markdown("### 📋 Configuration Matrix")

if not fleet_units:
    st.warning("Define your fleet in the sidebar.")
    st.stop()

# Build Header Row
header_cols = st.columns([1] + [1] * len(INITIATIVE_DETAILS))
with header_cols[0]:
    st.markdown("**Unit Name**")
for i, init_name in enumerate(INITIATIVE_DETAILS.keys()):
    with header_cols[i+1]:
        st.markdown(f"**{init_name}**")
        st.caption("Hover for features", help=INITIATIVE_DETAILS[init_name])

st.divider()

# Logic and Matrix Rendering
matrix_results = {init: [] for init in INITIATIVE_DETAILS.keys()}
for plant in fleet_units:
    with st.container():
        cols = st.columns([1] + [1] * len(INITIATIVE_DETAILS))
        with cols[0]:
            st.markdown(f"#### {plant['name']}")
            st.caption(f"{plant['sector'].split(' ')[1]}")
        
        for i, init_name in enumerate(INITIATIVE_DETAILS.keys()):
            with cols[i+1]:
                active = st.checkbox(f"Activate", key=f"en_{plant['id']}_{init_name}")
                if active:
                    sc = st.radio("Scope", ["Assets", "Overall"], horizontal=True, key=f"sc_{plant['id']}_{init_name}")
                    if sc == "Assets":
                        chosen = st.multiselect("Select", PLANT_PORTFOLIO[plant['sector']], key=f"u_{plant['id']}_{init_name}")
                        f_cnt = 0
                        if "Furnace" in chosen and "Olefins" in plant['sector']:
                            f_cnt = st.number_input("Furnaces", 1, 30, 1, key=f"f_{plant['id']}_{init_name}")
                        count = max(1, len([u for u in chosen if u != "Furnace"]) + f_cnt)
                        matrix_results[init_name].append({"type": "asset", "count": count})
                    else:
                        base_count = 8
                        if "Olefins" in plant['sector']:
                            f_ov = st.number_input("Furnaces", 1, 30, 1, key=f"fov_{plant['id']}_{init_name}")
                            base_count = 4 + f_ov
                        matrix_results[init_name].append({"type": "overall", "count": base_count})
    st.divider()

# --- 9. PRICING ENGINE ---
PLATFORM_FEE, SETUP_FEE, SERVICE_MO = 45000, 25000, 5000
user_fee = (user_slots / 5) * 5000
total_fleet_size = len(fleet_units)
total_setup, total_service, total_ari = 0, 0, 0
active_inits_count = sum(1 for init in matrix_results if len(matrix_results[init]) > 0)

for init_name, plant_configs in matrix_results.items():
    for p in plant_configs:
        scaling = 1.0 + (max(0, p['count'] - 1) * 0.2)
        base_ari = 0 if (active_inits_count == 1 and total_fleet_size == 1 and p['count'] == 1) else 15000
        p_ari = (base_ari * scaling * (1.0 + (max(0, active_inits_count - 1) * 0.25)))
        p_setup = (p['count'] * SETUP_FEE)
        p_service = (p['count'] * SERVICE_MO * 6)
        if p['type'] == "overall":
            p_ari *= 0.8; p_setup *= 0.8; p_service *= 0.8
        total_ari += p_ari; total_setup += p_setup; total_service += p_service

total_y1 = PLATFORM_FEE + user_fee + total_ari + total_setup + total_service
total_y2 = PLATFORM_FEE + user_fee + total_ari

# --- 10. INJECT RESULTS INTO STICKY SUMMARY ---
with summary_placeholder:
    st.markdown('<div class="executive-card">', unsafe_allow_html=True)
    m_col1, m_col2 = st.columns([1.5, 2.5])
    with m_col1:
        st.metric("Total Year 1 Investment", f"${total_y1:,.0f}", help="Sum of core fees, implementation, and service.")
        st.success(f"**Annual Recurring (Year 2+): ${total_y2:,.0f}**")
        if st.button("Download Enterprise Proposal", use_container_width=True):
            st.toast("Proposal Generated!")
    with m_col2:
        st.markdown("<p style='font-size:11px; font-weight:800; color:#94A3B8; letter-spacing:1px;'>INVESTMENT BREAKUP</p>", unsafe_allow_html=True)
        b1, b2, b3 = st.columns(3)
        b1.metric("Capability ARI", f"${total_ari:,.0f}", help=COST_HELP["ARI"])
        b2.metric("Setup Fees", f"${total_setup:,.0f}", help=COST_HELP["Setup"])
        b3.metric("Service (6mo)", f"${total_service:,.0f}", help=COST_HELP["Service"])
        st.caption(f"Platform + {user_slots} Seats: ${(PLATFORM_FEE + user_fee):,.0f} ({COST_HELP['Platform']})")
    st.markdown('</div>', unsafe_allow_html=True)
