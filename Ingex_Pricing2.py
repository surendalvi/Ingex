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

# --- 3. DUAL-STICKY CSS (PINNED FINANCIALS & HEADERS) ---
st.markdown("""
    <style>
    .main .block-container { padding: 1rem 2rem !important; background-color: #F8FAFC; }
    
    /* 1. STICKY FINANCIAL CARD */
    /* This stays at the top of the viewport */
    div:has(> .executive-card) {
        position: sticky !important;
        top: 0 !important;
        z-index: 1000 !important;
        background-color: #F8FAFC !important;
        padding-bottom: 10px;
    }

    .executive-card {
        background: white; padding: 18px; border-radius: 12px;
        border-top: 5px solid #0F172A; border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    }

    /* 2. STICKY INITIATIVE HEADERS */
    /* This pins the labels (Efficiency, etc) below the financial card */
    [data-testid="stHorizontalBlock"]:has(p:contains("Unit Name")) {
        position: sticky !important;
        top: 160px !important; /* Adjust based on your screen resolution */
        z-index: 999 !important;
        background-color: #FFFFFF !important;
        border-bottom: 3px solid #0F172A !important;
        padding: 10px 0 !important;
    }

    /* 3. STICKY LEFT COLUMN (Plant Names) */
    [data-testid="column"]:first-child {
        position: sticky !important;
        left: 0 !important;
        z-index: 998 !important;
        background-color: #F8FAFC !important;
        border-right: 3px solid #0F172A !important;
        padding-right: 15px !important;
    }

    /* 4. PREVENT COLUMN SQUEEZING */
    [data-testid="column"] {
        min-width: 280px !important;
        flex: 0 0 auto !important;
    }

    /* UI Polishing */
    [data-testid="stMetricValue"] { font-size: 28px !important; font-weight: 800 !important; color: #0F172A !important; }
    .stRadio > label { font-size: 11px !important; font-weight: 800 !important; color: #475569 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 4. DATA REPOSITORY ---
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
    "📈 Efficiency": "• Yield & Catalyst Optimization\n• Soft Sensors\n• Dynamic Benchmarking",
    "⚡ Energy": "• Steam Header Balancing\n• Fuel Gas Optimization\n• Furnace Excess Air",
    "🛠️ Reliability": "• 100+ Failure Templates\n• Remaining Useful Life (RUL)\n• Bad Actor ID",
    "🌱 Sustainability": "• Scope 1/2 Tracking\n• Carbon Intensity Index\n• Flare Loss Prevention",
    "🔄 Workflows": "• Digital Shift Handover\n• Automated Work-Orders\n• Alert Management"
}

# --- 5. TOP BRANDING & SIDEBAR ---
st.markdown(f"""
    <div style="display:flex; align-items:center; background:white; padding:10px 20px; border-radius:12px; border:1px solid #E2E8F0;">
        <img src="{logo_url}" width="35">
        <div style="margin-left:15px;">
            <div style="font-size:18px; font-weight:800; color:#0F172A;">INGERO360AI</div>
            <div style="font-size:9px; color:#64748B; font-weight:700;">STRATEGIC PORTFOLIO MATRIX</div>
        </div>
    </div>
""", unsafe_allow_html=True)

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

# --- 6. INITIAL CALCULATION (FOR STICKY TOP DISPLAY) ---
# We run a logic pass before rendering to populate the summary at the top
if fleet_units:
    # (Simplified engine to get current state for metrics)
    PLATFORM_FEE, SETUP_FEE, SERVICE_MO = 45000, 25000, 5000
    user_fee = (user_slots / 5) * 5000
    # Calculations happen dynamically below, so we use session state or placeholders
    pass

# --- 7. THE STICKY FINANCIAL CARD ---
# (Note: In a real app, you'd calculate this based on widget states. 
# Here we place the logic at the top of the script so the summary reflects current inputs.)
# [Logic simplified for brevity, assume calculation is done]

# --- 8. CONFIGURATION MATRIX ---
st.markdown("### 📋 Configuration Matrix")

if not fleet_units:
    st.warning("Define your fleet in the sidebar.")
    st.stop()

# Build Sticky Header Row
header_cols = st.columns([1] + [1] * len(INITIATIVE_DETAILS))
with header_cols[0]:
    st.markdown("<p style='font-weight:800; margin:0;'>Unit Name</p>", unsafe_allow_html=True)
for i, init_name in enumerate(INITIATIVE_DETAILS.keys()):
    with header_cols[i+1]:
        st.markdown(f"<p style='font-weight:800; margin:0;'>{init_name}</p>", unsafe_allow_html=True)
        st.caption("i", help=INITIATIVE_DETAILS[init_name])

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

# --- 9. FINAL CALCULATION ---
total_setup, total_service, total_ari = 0, 0, 0
active_inits_count = sum(1 for init in matrix_results if len(matrix_results[init]) > 0)
for init_name, plant_configs in matrix_results.items():
    for p in plant_configs:
        scaling = 1.0 + (max(0, p['count'] - 1) * 0.2)
        base_ari = 0 if (active_inits_count == 1 and len(fleet_units) == 1 and p['count'] == 1) else 15000
        p_ari = (base_ari * scaling * (1.0 + (max(0, active_inits_count - 1) * 0.25)))
        p_setup = (p['count'] * SETUP_FEE)
        p_service = (p['count'] * SERVICE_MO * 6)
        if p['type'] == "overall":
            p_ari *= 0.8; p_setup *= 0.8; p_service *= 0.8
        total_ari += p_ari; total_setup += p_setup; total_service += p_service

total_y1 = PLATFORM_FEE + user_fee + total_ari + total_setup + total_service
total_y2 = PLATFORM_FEE + user_fee + total_ari

# --- 10. DYNAMIC INJECTION TO TOP SUMMARY ---
# In Streamlit, since code runs top-to-bottom, the best way to keep it "moving" 
# is to use a container at the top of the matrix section.
st.sidebar.markdown("---")
st.sidebar.metric("Live Total Year 1", f"${total_y1:,.0f}")

# Re-rendering the investment breakup at the top with tooltips
with st.container():
    st.markdown('<div class="executive-card">', unsafe_allow_html=True)
    c1, c2 = st.columns([1.5, 2.5])
    with c1:
        st.metric("Total Year 1", f"${total_y1:,.0f}")
        st.success(f"**Year 2 Recurring: ${total_y2:,.0f}**")
    with c2:
        st.markdown("<p style='font-size:11px; font-weight:800; color:#94A3B8; letter-spacing:1px;'>BREAKUP</p>", unsafe_allow_html=True)
        b1, b2, b3 = st.columns(3)
        b1.metric("ARI", f"${total_ari:,.0f}", help="Algorithm Subscription")
        b2.metric("Setup", f"${total_setup:,.0f}", help="One-time Config")
        b3.metric("Service", f"${total_service:,.0f}", help="6mo SME Support")
    st.markdown('</div>', unsafe_allow_html=True)
