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

# --- 3. THE "SKEW-DESTRUCTION" CSS (FORCE HORIZONTAL SCROLL) ---
st.markdown("""
    <style>
    /* 1. Global Reset */
    .main .block-container { padding: 1rem 2rem !important; background-color: #FDFDFD; }
    
    /* 2. FORCE HORIZONTAL SCROLLING ON MATRIX ROWS */
    /* This targets the container holding the columns */
    [data-testid="stHorizontalBlock"] {
        overflow-x: auto !important;
        display: flex !important;
        flex-wrap: nowrap !important;
        padding-bottom: 25px !important;
        border-bottom: 1px solid #F1F5F9;
    }

    /* 3. LOCK COLUMN WIDTHS */
    /* This prevents columns from squeezing/shrinking */
    [data-testid="column"] {
        min-width: 250px !important;
        flex-shrink: 0 !important;
        padding: 10px !important;
    }
    
    /* 4. STICKY FIRST COLUMN (Initiative Names) */
    /* This keeps the labels visible while scrolling plants */
    [data-testid="stHorizontalBlock"] > div:first-child {
        position: sticky !important;
        left: 0 !important;
        z-index: 100 !important;
        background-color: #FFFFFF !important;
        border-right: 3px solid #0F172A !important;
        min-width: 200px !important;
        max-width: 200px !important;
    }

    /* 5. UI Polishing */
    .nav-header {
        display: flex; align-items: center; justify-content: space-between;
        padding: 15px; background: white; border-radius: 12px;
        border: 1px solid #E2E8F0; margin-bottom: 20px;
    }
    .metric-card {
        background: white; padding: 20px; border-radius: 16px;
        border-top: 5px solid #0F172A; border: 1px solid #E2E8F0;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 20px;
    }
    [data-testid="stMetricValue"] { font-size: 32px !important; font-weight: 800 !important; color: #0F172A !important; }
    .stRadio > label { font-size: 11px !important; font-weight: 800 !important; color: #64748B !important; }
    </style>
""", unsafe_allow_html=True)

# --- 4. DATA REPOSITORY ---
PLANT_PORTFOLIO = {
    "🏭 Olefins": ["Furnace", "Quench", "CGC", "Acetylene Reactor", "Cold Section"],
    "🧪 Polymers": ["Reactor", "Extruder", "VCM Unit", "Pelletizer"],
    "💧 Methanol": ["Reformer", "Synthesis Reactor", "CO2 Removal"],
    "❄️ ASU": ["MAC", "Purification", "Cold Box", "Expander"],
    "🔧 Utility": ["Boiler", "Cooling Tower", "Air Compressor", "Flare"],
    "⛽ Refining": ["CDU", "VDU", "Delayed Coker", "FCCU", "Hydrocracker"]
}

INITIATIVE_INFO = {
    "📈 Efficiency": "Yield & Catalyst Optimization, Soft Sensors, Dynamic Benchmarking.",
    "⚡ Energy": "Steam Header Balancing, Fuel Loss Reduction, Switchability.",
    "🛠️ Reliability": "Failure Mode Prediction, RUL, Root Cause Analytics.",
    "🌱 Sustainability": "Scope 1/2 Monitoring, Carbon Intensity, Waste Management.",
    "🔄 Workflows": "Digital Shift Handover, Auto-Workorders, Alert Mgmt."
}

# --- 5. TOP BRANDING ---
st.markdown(f"""
    <div class="nav-header">
        <div style="display: flex; align-items: center;">
            <img src="{logo_url}" width="200">
            <div style="margin-left: 15px;">
                <div style="font-size:40px; font-weight:800; color:#0F172A;">PRODUCT PRICING CATALOGUE</div>
                <div style="font-size:10px; color:#64748B; font-weight:700; letter-spacing:1.5px;">ENTERPRISE FLEET MATRIX</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 6. SIDEBAR FLEET CONSTRUCTION ---
with st.sidebar:
    st.markdown("### 🏗️ Fleet Construction")
    sel_sectors = st.multiselect("Select Plant Sectors", list(PLANT_PORTFOLIO.keys()), default=["🏭 Olefins"])
    
    fleet_units = []
    for s in sel_sectors:
        qty = st.number_input(f"Qty: {s.split(' ')[1]}", 1, 15, 1, key=f"q_{s}")
        for i in range(qty):
            fleet_units.append({"name": f"{s.split(' ')[1]} #{i+1}", "sector": s, "id": f"{s}_{i}"})
    
    st.markdown("---")
    user_slots = st.selectbox("User Licenses", [5, 10, 15, 20], index=0)

# --- 7. TOP INVESTMENT SUMMARY ---
summary_placeholder = st.container()

# --- 8. THE CONFIGURATION MATRIX ---
st.markdown("### 📋 Strategy Configuration Matrix")
st.caption("👈 **Scroll Right** to view more plants. Initiative labels are locked on the left.")

if not fleet_units:
    st.warning("Define your fleet in the sidebar.")
    st.stop()

matrix_results = {}

for init_name, help_text in INITIATIVE_INFO.items():
    # Creating row
    cols = st.columns([1] + [1] * len(fleet_units))
    
    with cols[0]:
        is_active = st.checkbox(f"**{init_name}**", value=(init_name == "📈 Efficiency"), 
                                key=f"en_{init_name}", help=help_text)
    
    if is_active:
        row_configs = []
        for idx, plant in enumerate(fleet_units):
            with cols[idx + 1]:
                st.markdown(f"<p style='font-size:11px; color:#94A3B8; font-weight:800; margin-bottom:0px;'>{plant['name']}</p>", unsafe_allow_html=True)
                sc = st.radio("Scope", ["Assets", "Overall"], horizontal=True, key=f"sc_{init_name}_{plant['id']}")
                
                if sc == "Assets":
                    chosen = st.multiselect("Select Units", PLANT_PORTFOLIO[plant['sector']], key=f"u_{init_name}_{plant['id']}")
                    f_cnt = 0
                    if "Furnace" in chosen and "Olefins" in plant['sector']:
                        f_cnt = st.number_input("Furnaces", 1, 30, 1, key=f"f_{init_name}_{plant['id']}")
                    count = max(1, len([u for u in chosen if u != "Furnace"]) + f_cnt)
                    row_configs.append({"type": "asset", "count": count})
                else:
                    base_count = 8
                    if "Olefins" in plant['sector']:
                        f_ov = st.number_input("Furnaces", 1, 30, 1, key=f"fov_{init_name}_{plant['id']}")
                        base_count = 4 + f_ov
                    row_configs.append({"type": "overall", "count": base_count})
        matrix_results[init_name] = row_configs
    st.divider()

# --- 9. PRICING CALCULATION ---
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

# --- 10. RENDER TOP SUMMARY ---
with summary_placeholder:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    m_col1, m_col2 = st.columns([1.5, 2.5])
    
    with m_col1:
        st.metric("Total Year 1 Investment", f"${total_y1:,.0f}", help="Sum of core fees, implementaton, and service.")
        st.success(f"**Annual Recurring (Year 2+): ${total_y2:,.0f}**")
        if st.button("Download Final Proposal", use_container_width=True):
            st.toast("Proposal Generated!")

    with m_col2:
        st.markdown("<p style='font-size:11px; font-weight:800; color:#94A3B8; letter-spacing:1px;'>INVESTMENT BREAKUP</p>", unsafe_allow_html=True)
        b1, b2, b3 = st.columns(3)
        b1.metric("Capability ARI", f"${total_ari:,.0f}", help="Scaled subscription fee.")
        b2.metric("Setup Fees", f"${total_setup:,.0f}", help="One-time configuration.")
        b3.metric("Service (6mo)", f"${total_service:,.0f}", help="Human advisory period.")
        st.caption(f"Platform + {user_slots} Seats: ${(PLATFORM_FEE + user_fee):,.0f}")
    st.markdown('</div>', unsafe_allow_html=True)
