import streamlit as st

# --- 1. PAGE CONFIG & UI ---
st.set_page_config(page_title="INGEX Pricing", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for "Zero Scroll" and a polished Figma-style look
st.markdown("""
    <style>
    /* Prevent vertical and horizontal scrolling */
    .main .block-container {
        padding: 1rem 2.5rem !important;
        max-width: 100%;
        height: 100vh;
        overflow: hidden;
    }
    
    /* Product Header Styling */
    .ingex-header { font-size: 26px; font-weight: 800; color: #031D44; margin-bottom: 0.1rem; }
    h3 { color: #031D44; font-size: 0.95rem !important; margin-bottom: 4px !important; }

    /* Final Price Card */
    .pricing-card {
        background: #F8FAFC;
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    .big-price { font-size: 40px; font-weight: 900; color: #031D44; line-height: 1; margin: 6px 0; }
    .price-sub { font-size: 13px; color: #64748B; line-height: 1.5; }

    /* Checkbox Styling */
    div.stCheckbox > label {
        background: white;
        padding: 4px 8px !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 6px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. MODULE DATA & INDUSTRY FEATURES ---
MODULE_DATA = {
    "Plant Efficiency": {
        "price": 150000,
        "features": ["Dynamic Benchmarking", "Soft sensors/VirtualLab", "Fouling Prediction/forecast", "NOX Forecast", "Anomaly Detection", "Optimization", "Trending", "Prescriptive Recos", "KPI Monitoring", "Catalyst Health & Life Monitoring"]
    },
    "Energy Optimization": {
        "price": 180000,
        "features": ["Driver Switchability", "Reduction in Fuel/Steam/Elec losses", "Energy Optimizer", "Significant Energy users efficiency", "Steam Header Balancing"]
    },
    "Reliability": {
        "price": 170000,
        "features": ["Failure Mode (>100+)", "Time to Failure", "Bad Actor Identification", "Vibration Data Correlation"]
    },
    "Asset Metric Hub": {
        "price": 100000,
        "features": ["Asset Management", "Cost of Assets", "MTBF (Between Failure)", "MTTR (To Repair)", "Cost Ineffectiveness", "Preventive/Reactive Maintenance", "ISO 55000 Compliance Tracking"]
    },
    "Sustainability": {
        "price": 120000,
        "features": ["Emission Monitoring (Scope 1/2)", "Water and Waste Management", "Resource Efficiency", "Carbon Intensity per Product Ton"]
    },
    "ML OPS": {
        "price": 200000,
        "features": ["Predictive Accuracy Metrics", "Drift Detection", "Service Uptime", "Logs", "Dashboard Usage", "Inference Latency Tracking"]
    },
    "Workflows": {
        "price": 105000,
        "features": ["Alert Management & Statistics", "Email Alerts", "Automatic workorder creation", "End to End tracking of actions", "Digital Shift Handover Integration"]
    }
}

SCALES = {"Single Asset": 1.0, "System (8 Units)": 1.5, "Process Train": 2.0, "Full Plant": 2.5}

# --- 3. TOP BAR (Inputs) ---
st.markdown('<div class="ingex-header">INGEX <span style="font-weight:300; color:#64748B;">| Digital Investment Engine</span></div>', unsafe_allow_html=True)

t_col1, t_col2, t_col3 = st.columns([2, 1, 1])
with t_col1:
    selected_scale = st.select_slider("Deployment Scope", options=list(SCALES.keys()), value="Full Plant")
    scale_mult = SCALES[selected_scale]
with t_col2:
    user_count = st.number_input("User Licenses", min_value=1, max_value=100, value=10)
    u_mult = 1.0 if user_count <= 1 else 1.2 if user_count <= 3 else 1.4 if user_count <= 10 else 2.0
with t_col3:
    st.markdown(f"<div style='margin-top:22px; font-size:13px;'><b>Scale:</b> {scale_mult}x | <b>Users:</b> {u_mult}x</div>", unsafe_allow_html=True)

st.markdown("---")

# --- 4. MAIN LAYOUT ---
col_left, col_right = st.columns([1.7, 1], gap="large")

with col_left:
    st.markdown("### Select Platform Capabilities")
    selected_modules = []
    
    # Loop to display modules with Popover cards
    for name, data in MODULE_DATA.items():
        row_c1, row_c2 = st.columns([3, 1.2])
        with row_c1:
            if st.checkbox(f"**{name}**", value=True, key=f"cb_{name}"):
                selected_modules.append(name)
        with row_c2:
            with st.popover("View Features", use_container_width=True):
                st.markdown(f"**{name} Industry Specs**")
                for feature in data['features']:
                    st.markdown(f"• {feature}")

with col_right:
    # Logic Calculation
    PLATFORM_FEE = 200000
    base_sum = sum([MODULE_DATA[m]['price'] for m in selected_modules])
    scaled_modules = base_sum * scale_mult
    discount_rate = 0.25 if len(selected_modules) >= 5 else 0.0
    savings = scaled_modules * discount_rate
    final_ari = (PLATFORM_FEE + (scaled_modules - savings)) * u_mult

    # Summary Pricing Card
    st.markdown(f"""
        <div class="pricing-card">
            <p style="text-transform: uppercase; font-size: 11px; font-weight: 700; color: #64748B; margin:0;">Total Annual Investment (ARI)</p>
            <div class="big-price"><span style="font-size:20px; vertical-align:top; margin-right:2px;">$</span>{final_ari:,.0f}</div>
            <div style="font-size: 12px; color: #047857; font-weight: 600; margin-bottom:12px;">
                {f"✓ 25% Multi-Module Discount Active" if discount_rate > 0 else "Select 5+ modules to save 25%"}
            </div>
            <div class="price-sub" style="border-top: 1px solid #E2E8F0; padding-top: 8px;">
                <div style="display:flex; justify-content:space-between;"><span>Core Platform Fee</span><b>${PLATFORM_FEE:,}</b></div>
                <div style="display:flex; justify-content:space-between;"><span>Module Subtotal</span><b>${(scaled_modules - savings):,.0f}</b></div>
                <div style="display:flex; justify-content:space-between; margin-top:4px; padding-top:4px; border-top:1px dashed #CBD5E1; color:#031D44; font-weight:800; font-size:14px;">
                    <span>Final ARI Estimate</span><span>${final_ari:,.0f}</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Generate Official INGEX Quote", use_container_width=True):
        st.toast("Quote Drafted: ~$2.97M for Full Plant")

st.markdown(f"<div style='text-align: center; color: #94A3B8; font-size: 11px; margin-top:10px;'>INGEX by Ingenero | Trusted Digital Operations for Global Petrochemicals</div>", unsafe_allow_html=True)