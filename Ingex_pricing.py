import streamlit as st
import pandas as pd

# --- 1. PAGE CONFIG & UI HACKS FOR "SINGLE SCREEN" ---
st.set_page_config(page_title="INGEX Pricing", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS to eliminate scrolling, reduce padding, and match Ingenero's clean aesthetic
st.markdown("""
    <style>
    /* Force the app to fit the screen height and hide scrollbars */
    .main .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 0rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
        max-width: 100%;
    }
    div[data-testid="stVerticalBlock"] { gap: 0.5rem; }
    
    /* Typography & Colors */
    h1, h2, h3 { color: #031D44; font-family: 'Inter', sans-serif; margin-bottom: 0.5rem !important; }
    .ingex-header { font-size: 28px; font-weight: 800; color: #031D44; letter-spacing: -1px; margin-bottom: 1rem; }
    
    /* Card Styling */
    .stat-card {
        background: white;
        padding: 1.2rem;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        height: 100%;
    }
    .big-price { font-size: 48px; font-weight: 900; color: #031D44; line-height: 1; }
    .unit { font-size: 16px; color: #64748B; font-weight: 400; }
    
    /* Compact Checkbox Tiles */
    div.stCheckbox > label {
        padding: 8px 12px !important;
        border-radius: 6px !important;
        border: 1px solid #E2E8F0 !important;
        margin-bottom: 2px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. PRICING DATA ---
PLATFORM_FEE = 200000
MODULES = {
    "Plant Efficiency": 150000, "Energy Optimization": 180000,
    "Reliability": 170000, "Asset Metric Hub": 100000,
    "Sustainability": 120000, "ML OPS": 200000, "Workflows": 105000
}
SCALES = {
    "Single Asset": 1.0, "System (8 Units)": 1.5,
    "Process Train": 2.0, "Full Plant": 2.5
}

# --- 3. TOP BAR (Header & Basic Inputs) ---
st.markdown('<div class="ingex-header">INGEX <span style="font-weight:300; color:#64748B;">| Digital Pricing Module</span></div>', unsafe_allow_html=True)

top_c1, top_c2, top_c3 = st.columns([2, 1, 1])
with top_c1:
    selected_scale = st.select_slider("Select Deployment Scope", options=list(SCALES.keys()), value="Full Plant")
    scale_mult = SCALES[selected_scale]
with top_c2:
    user_count = st.number_input("User Licenses", min_value=1, max_value=100, value=10)
    # Tiered Logic
    if user_count <= 1: u_mult = 1.0
    elif user_count <= 3: u_mult = 1.2
    elif user_count <= 10: u_mult = 1.4
    else: u_mult = 2.0
with top_c3:
    st.write("") # Spacer
    st.write(f"**Scope Multiplier:** {scale_mult}x")
    st.write(f"**User Tier:** {u_mult}x")

st.markdown("---")

# --- 4. MAIN CONTENT (Two Columns) ---
col_left, col_right = st.columns([1.5, 1], gap="large")

with col_left:
    st.markdown("### Select Modules")
    selected_modules = []
    # Displaying in 2 compact columns to save vertical space
    m_col1, m_col2 = st.columns(2)
    for i, (name, price) in enumerate(MODULES.items()):
        target = m_col1 if i % 2 == 0 else m_col2
        if target.checkbox(f"{name} (${price:,})", value=True):
            selected_modules.append(name)

with col_right:
    # Calculation Logic
    base_sum = sum([MODULES[m] for m in selected_modules])
    scaled_modules = base_sum * scale_mult
    discount_rate = 0.25 if len(selected_modules) >= 5 else 0.0
    savings = scaled_modules * discount_rate
    final_ari = (PLATFORM_FEE + (scaled_modules - savings)) * u_mult

    # Result Card
    st.markdown(f"""
        <div class="stat-card">
            <p style="text-transform: uppercase; font-size: 12px; font-weight: 600; color: #64748B; margin:0;">Total Annual Recurring Investment (ARI)</p>
            <div class="big-price"><span style="font-size:24px;">$</span>{final_ari:,.0f} <span class="unit">/ year</span></div>
            <hr style="margin: 15px 0;">
            <div style="font-size: 14px; line-height: 1.8;">
                <div style="display:flex; justify-content:space-between;"><span>Base Platform</span><b>${PLATFORM_FEE:,}</b></div>
                <div style="display:flex; justify-content:space-between;"><span>Modules (Scaled)</span><b>${scaled_modules:,.0f}</b></div>
                <div style="display:flex; justify-content:space-between; color: #047857;"><span>Bundle Discount (25%)</span><b>-${savings:,.0f}</b></div>
                <div style="display:flex; justify-content:space-between; border-top: 1px solid #EEE; margin-top: 5px; padding-top: 5px;"><span>Subtotal</span><b>${(PLATFORM_FEE + (scaled_modules - savings)):,.0f}</b></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Generate Official Quote"):
        st.success(f"Quote Prepared for {selected_scale}")

# --- 5. COMPACT FOOTER ---
st.markdown("---")
st.markdown(f"<div style='text-align: center; color: #94A3B8; font-size: 12px;'>INGEX by Ingenero. All configurations are annual estimates based on standard petrochemical plant benchmarks.</div>", unsafe_allow_html=True)