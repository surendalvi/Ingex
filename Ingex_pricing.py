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
    page_title="INGERO360AI Pricing", 
    page_icon="🏭",
    layout="wide", 
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main .block-container { padding: 1rem 2rem !important; background-color: #F8FAFC; }
    .nav-header {
        display: flex; align-items: center; justify-content: space-between;
        padding: 15px; background: white; border-radius: 12px;
        border: 1px solid #E2E8F0; margin-bottom: 20px;
    }
    .header-text { font-size: 26px; font-weight: 800; color: #0F172A; }
    
    /* Hover effect for expanders */
    .stExpander:hover { border-color: #38BDF8 !important; }
    
    /* Style metrics for clarity */
    [data-testid="stMetricValue"] { font-size: 32px !important; font-weight: 800 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. DATA REPOSITORY WITH ICONS ---
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

INITIATIVES = {
    "📈 Plant Efficiency": "Yield Optimization, Catalyst Health, Fouling Prediction.",
    "⚡ Energy Optimization": "Steam Header Balancing, Fuel Loss Reduction.",
    "🛠️ Reliability": "Failure Modes, Remaining Life Prediction, Bad Actor ID.",
    "🌱 Sustainability": "Carbon Intensity, Emission Monitoring.",
    "🔄 Workflows": "Auto-Workorders, Audit trail."
}

# --- 4. TOP BRANDING ---
st.markdown(f"""
    <div class="nav-header">
        <div style="display: flex; align-items: center;">
            <img src="{logo_url}" width="300">
            <div style="margin-left: 18px;">
                <div class="header-text">PRODUCT PRICING CATALOGUE</div>
                <div style="font-size: 11px; color: #64748B; font-weight: 700;">🚀 ENTERPRISE PORTFOLIO COMMAND</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR: FLEET DEFINITION ---
with st.sidebar:
    st.markdown("### 🏗️ CHEMICAL PLANTS TYPE")
    sel_sectors = st.multiselect("Select Plant Sectors", list(PLANT_PORTFOLIO.keys()), default=["🏭 Olefins/Ethylene"])
    
    fleet_def = {}
    for s in sel_sectors:
        # Removing emoji for calculation key
        clean_name = s.split(" ")[1]
        fleet_def[s] = st.number_input(f"Qty: {clean_name}", 1, 10, 1, key=f"s_qty_{s}")
    
    st.markdown("---")
    st.markdown("### 👥 User Access")
    user_slots = st.selectbox("Active Licenses", [5, 10, 15, 20], index=0)

# --- 6. MAIN CONFIGURATION ---
col_main, col_summary = st.columns([2, 1], gap="large")

with col_main:
    st.markdown("### 🛠️ Capability & Asset Mapping")
    
    initiative_configs = {}
    for init_name, help_text in INITIATIVES.items():
        with st.expander(f"**{init_name}**", expanded=(init_name == "📈 Plant Efficiency")):
            active = st.checkbox(f"Activate {init_name.split(' ')[1]}", value=(init_name=="📈 Plant Efficiency"), key=f"en_{init_name}", help=help_text)
            
            if active:
                mode = st.radio("Configuration Mode", ["📂 Sector-Wise", "🎯 Plant-Wise (Granular)"], 
                                horizontal=True, key=f"m_{init_name}")
                
                instances = []
                for sector, qty in fleet_def.items():
                    loop_range = range(qty) if "Granular" in mode else range(1)
                    
                    for i in loop_range:
                        if "Granular" in mode:
                            st.markdown(f"**{sector} Unit #{i+1}**")
                        else:
                            st.markdown(f"**{sector} Fleet Rule** (x{qty} Units)")
                        
                        sc = st.radio(f"Scope Strategy", ["📦 Assets", "🌐 Overall Plant"], horizontal=True, key=f"sc_{init_name}_{sector}_{i}")
                        
                        if "Assets" in sc:
                            chosen = st.multiselect("Select High-Value Units", PLANT_PORTFOLIO[sector], key=f"u_{init_name}_{sector}_{i}")
                            f_cnt = 0
                            if "Furnace" in chosen and "Olefins" in sector:
                                f_cnt = st.number_input("Furnace Quantity", 1, 30, 1, key=f"f_ast_{init_name}_{sector}_{i}")
                            count = max(1, len([u for u in chosen if u != "Furnace"]) + f_cnt)
                            instances.append({"type": "asset", "count": count, "qty": 1 if "Granular" in mode else qty})
                        else:
                            base_count = 8
                            if "Olefins" in sector:
                                f_cnt_ov = st.number_input("Furnace Count for Overall Scale", 1, 30, 1, key=f"f_ov_{init_name}_{sector}_{i}")
                                base_count = 4 + f_cnt_ov
                            instances.append({"type": "overall", "count": base_count, "qty": 1 if "Granular" in mode else qty})
                
                initiative_configs[init_name] = instances

with col_summary:
    # --- 7. PRICING ENGINE ---
    PLATFORM_FEE, SETUP_FEE, SERVICE_MO = 45000, 25000, 5000
    user_fee = (user_slots / 5) * 5000
    total_fleet_plants = sum(fleet_def.values())
    
    total_setup, total_service, total_ari = 0, 0, 0
    num_active_inits = len(initiative_configs)

    for init_name, plants in initiative_configs.items():
        for p in plants:
            mult = p['qty']
            scaling = 1.0 + (max(0, p['count'] - 1) * 0.2)
            base_ari = 0 if (num_active_inits == 1 and total_fleet_plants == 1 and p['count'] == 1) else 15000
            
            p_ari = (base_ari * scaling * (1.0 + (max(0, num_active_inits - 1) * 0.25))) * mult
            p_setup = (p['count'] * SETUP_FEE) * mult
            p_service = (p['count'] * SERVICE_MO * 6) * mult
            
            if p['type'] == "overall":
                p_ari *= 0.8; p_setup *= 0.8; p_service *= 0.8
            
            total_ari += p_ari; total_setup += p_setup; total_service += p_service

    total_y1 = PLATFORM_FEE + user_fee + total_ari + total_setup + total_service
    total_y2 = PLATFORM_FEE + user_fee + total_ari

    # --- 8. THE SUMMARY (ICON ENHANCED) ---
    st.subheader("💰 Investment Summary")
    st.metric("Total Year 1", f"${total_y1:,.0f}")
    
    st.divider()
    
    # Financial Breakup with Icons
    c1, c2 = st.columns([2, 1])
    c1.write("👥 Platform & Users")
    c2.write(f"**${(PLATFORM_FEE + user_fee):,.0f}**")
    
    c1, c2 = st.columns([2, 1])
    c1.write("🛰️ Scaled Capability ARI")
    c2.write(f"**${total_ari:,.0f}**")
    
    c1, c2 = st.columns([2, 1])
    c1.write("🚀 Implementation (One-time)")
    c2.write(f"**${total_setup:,.0f}**")
    
    c1, c2 = st.columns([2, 1])
    c1.write("📞 Technical Service (6mo)")
    c2.write(f"**${total_service:,.0f}**")
    
    st.write("---")
    st.info(f"**🔄 Recurring ARI (Year 2+): ${total_y2:,.0f}**")
    
    st.write(" ")
    if st.button("📄 Generate Final Proposal", use_container_width=True):
        st.success("Enterprise Portfolio Finalized")

st.markdown("<div style='text-align: center; color: #94A3B8; font-size: 10px; margin-top:30px;'>INGERO360AI | Trusted Digital Partner for Petrochemicals</div>", unsafe_allow_html=True)
