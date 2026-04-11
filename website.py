import streamlit as st
import streamlit.components.v1 as components

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Ingenero360AI | Sovereign Strategic Brain", 
    page_icon="🖥️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. PREMIUM BRANDED THEME (CSS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=JetBrains+Mono:wght@500&display=swap');
    
    .main { background-color: #0F172A; font-family: 'Inter', sans-serif; color: white; }
    
    /* CLEAN PROMINENT HEADER */
    .nav-header {
        display: flex; align-items: center; justify-content: space-between;
        padding: 30px 80px; background: #0F172A; 
        border-bottom: 4px solid #F97316; 
        position: sticky; top: 0; z-index: 1000;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    }

    /* HERO SECTION */
    .hero { text-align: center; padding: 120px 80px; background: radial-gradient(circle at top right, #1E293B, #0F172A); }
    .hero h1 { font-size: 82px; font-weight: 800; letter-spacing: -4px; color: white; margin-bottom: 0px; line-height: 1.1; }
    .hero-tag { font-size: 16px; color: #F97316; font-weight: 800; text-transform: uppercase; letter-spacing: 6px; margin-bottom: 25px; }

    /* DATA ALCHEMY SECTION */
    .alchemy-box {
        background: rgba(30, 41, 59, 0.5); border-left: 6px solid #38BDF8;
        padding: 50px 80px; margin: 40px 0; line-height: 1.7;
    }

    /* AGENTIC FLOW (HORIZONTAL) */
    .horizon-container { display: flex; align-items: center; gap: 15px; padding: 40px 0; overflow-x: auto; justify-content: center; }
    .agent-node {
        min-width: 210px; padding: 25px; border-radius: 14px; border: 1.5px solid rgba(255,255,255,0.1);
        background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(12px);
    }
    .role-tag { font-size: 9px; font-weight: 900; color: #38BDF8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; }
    .agent-title { font-size: 16px; font-weight: 700; color: white; margin-bottom: 8px; }
    .agent-desc { font-size: 11px; color: #94A3B8; line-height: 1.5; }

    /* HIGHLIGHTS */
    .u-brain { border-color: #F97316; box-shadow: 0 0 25px rgba(249, 115, 22, 0.2); }
    .u-brain .role-tag { color: #F97316; }
    .u-result { border-color: #10B981; }
    .u-result .role-tag { color: #10B981; }

    /* THE MATRIX */
    .matrix-wrapper { background: rgba(15, 23, 42, 0.4); padding: 40px; border-radius: 20px; }
    table { width: 100%; border-collapse: separate; border-spacing: 12px; }
    th { background: #1E293B; color: #94A3B8; font-size: 12px; padding: 20px; border-radius: 10px; text-transform: uppercase; text-align: left; }
    td { background: rgba(30, 41, 59, 0.4); border-radius: 12px; padding: 25px; vertical-align: top; border: 1px solid rgba(255,255,255,0.05); }
    .bullet-item { border-left: 3px solid #F97316; padding-left: 15px; margin-bottom: 15px; font-size: 13px; color: #CBD5E1; }
</style>
""", unsafe_allow_html=True)

# --- 3. HEADER & HERO ---
st.markdown(f"""
    <div class="nav-header">
        <div style="display:flex; align-items:center;">
            <div style="font-size:32px; font-weight:800; color:white; letter-spacing:-1.5px;">INGERO360AI</div>
            <div style="margin-left:30px; font-size:11px; color:#F97316; font-weight:700; text-transform:uppercase; letter-spacing:4px;">Sovereign Strategic Brain</div>
        </div>
        <div style="font-size:12px; color:#94A3B8; font-weight:800; text-transform:uppercase; letter-spacing:1px;">Technology DNA ➔ Strategic Autonomy</div>
    </div>
    
    <div class="hero">
        <div class="hero-tag">The Alchemy of Industrial Data</div>
        <h1>Noise into <span style="color:#F97316">Knowledge</span></h1>
        <p style="font-size:24px; color:#94A3B8; max-width:950px; margin:25px auto;">
            Ingenero360AI is the only autonomous ecosystem that deciphers industrial chaos, 
            applies engineering DNA, and executes strategic executive intent.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- 4. THE DATA ALCHEMY STORY ---
st.markdown("""
<div class="alchemy-box">
    <h2 style="color:white; margin-bottom:20px; font-size:32px; font-weight:800;">The Alchemy of Inference</h2>
    <p style="font-size:19px; color:#CBD5E1; max-width:1100px;">
        Raw data is an industrial liability—a chaotic ocean of sensor readings that obscures the truth. 
        <b>Analytics is the catalyst</b> that turns this noise into magic. By applying deep-tier physics 
        and Agentic-AI, we don't just see what is happening; we <b>infer what is possible</b>.<br><br>
        Raw data says "Pressure is 40 bar." Ingenero360AI infers "You can increase throughput by 4.2% while 
        staying 10% below your carbon ceiling." That is the magic of a Strategic Brain.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 5. THE AGENTIC ECOSYSTEM (HORIZONTAL) ---
st.write("### The Coordinated Brain: Sub-Agent Workflow")
st.markdown("""
<div class="horizon-container">
    <div class="agent-node">
        <div class="role-tag">The Conductor</div>
        <div class="agent-title">Master Orchestrator</div>
        <div class="agent-desc">Governance Sub-Agent. Synchronizes fleet-wide intent using <b>GenAI</b>.</div>
    </div>
    <div style="color:#475569;">➔</div>
    <div class="agent-node">
        <div class="role-tag">The Seer</div>
        <div class="agent-title">Sensing Agent</div>
        <div class="agent-desc">DNA Sub-Agent. Calculates hidden process variables via <b>Soft Sensors</b>.</div>
    </div>
    <div style="color:#475569;">➔</div>
    <div class="agent-node" style="border-color:#38BDF8;">
        <div class="role-tag" style="color:#38BDF8;">The Time-Traveler</div>
        <div class="agent-title">Trend Sentinel</div>
        <div class="agent-desc">Predicts future process drifts and <b>Anomalies</b> before they occur.</div>
    </div>
    <div style="color:#475569;">➔</div>
    <div class="agent-node">
        <div class="role-tag">The Sentinel</div>
        <div class="agent-title">Guardrail Agent</div>
        <div class="agent-desc">Safety Sub-Agent. Enforces metallurgical and design limits 24/7.</div>
    </div>
    <div style="color:#F97316;">★</div>
    <div class="agent-node u-brain">
        <div class="role-tag">The Alchemist</div>
        <div class="agent-title">Optimizer Agent</div>
        <div class="agent-desc">Strategic Brain. Solves complex <b>MINLP</b> math for the global optimum.</div>
    </div>
    <div style="color:#10B981;">➔</div>
    <div class="agent-node u-result">
        <div class="role-tag">The Oracle</div>
        <div class="agent-title">Result Bus Agent</div>
        <div class="agent-desc">Strategic Outcome. Forecasts ROI via real-time <b>What-If</b> simulations.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. ROI METRICS ---
st.markdown("""
<div style="display: flex; justify-content: space-around; padding: 70px 0; background: #0F172A; border-radius: 20px; margin: 40px 80px; border: 1px solid rgba(255,255,255,0.05);">
    <div style="text-align: center;">
        <div style="font-size: 72px; font-weight: 800; color: #10B981;">$100M+</div>
        <div style="font-size: 15px; color: #94A3B8; text-transform: uppercase; font-weight: 800;">Realized Client ROI</div>
    </div>
    <div style="text-align: center;">
        <div style="font-size: 72px; font-weight: 800; color: #38BDF8;">$500M+</div>
        <div style="font-size: 15px; color: #94A3B8; text-transform: uppercase; font-weight: 800;">Identified Potential</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 7. STRATEGIC MATRIX (INDUSTRIES & PRODUCTS) ---
st.write("### Strategic Solution Matrix")
INDUSTRIES = ["Olefins", "Refining", "Ammonia/Urea", "Methanol", "EO/EG", "MTBE", "Aromatics", "Polymers", "Phenols", "ASU", "Utilities"]
PRODUCTS = ["Production Efficiency", "Energy Optimization", "Reliability", "Sustainability Hub", "Workflows"]

row_nav, col_nav = st.columns(2)
with row_nav: sel_ind = st.multiselect("Select Target Industries", INDUSTRIES, default=["Olefins", "Refining"])
with col_nav: sel_prod = st.multiselect("Select Strategic Products", PRODUCTS, default=["Production Efficiency"])

DNA_MAP = { 
    "Olefins": "Furnace Kinetics / TMT Safety", "Refining": "Fractionation / ASTM Specs", "Ammonia/Urea": "Synthesis Loop / Conv. Temp",
    "Methanol": "SMR Kinetics / S/C Ratio", "EO/EG": "Selectivity / Vapor Guard", "MTBE": "Etherification / Reflux",
    "Aromatics": "Hydro-Separation / Purity", "Polymers": "Reaction Rate / Melt Index", "Phenols": "Oxidation Rate / Peroxide Guard", 
    "ASU": "Cryo-Sep / O2 Purity", "Utilities": "Steam Header / HP-LP Balance" 
}

PRODUCT_MAP = { 
    "Production Efficiency": ["Yield Maximizer", "Throughput Advisory", "MINLP"], 
    "Energy Optimization": ["SEC Optimizer", "Energy Intensity", "LP"],
    "Reliability": ["RUL Optimizer", "Maintenance Hub", "Predictive"], 
    "Sustainability Hub": ["Carbon Optimizer", "ESG Compliance", "Forecasting"],
    "Workflows": ["SOP Compliance", "Handover Bus", "GenAI"] 
}

# Generate Matrix
matrix_html = "<table><thead><tr><th style='width:180px;'>Industry Domain</th>" + "".join([f"<th>{p}</th>" for p in sel_prod]) + "</tr></thead><tbody>"
for ind in sel_ind:
    matrix_html += f"<tr><td style='font-weight:800; color:#F97316;'>{ind}</td>"
    for prod in sel_prod:
        p_data = PRODUCT_MAP[prod]
        matrix_html += f"<td>"
        matrix_html += f"<div class='bullet-item' style='color:#94A3B8;'><b>Base Technology DNA:</b><br>{DNA_MAP[ind]}</div>"
        matrix_html += f"<div class='bullet-item' style='border-color:#F97316; color:white;'><b>Strategy Brain:</b> {p_data[0]}<br><small style='color:#F97316;'>{p_data[2]} Modeling</small></div>"
        matrix_html += f"<div class='bullet-item' style='border-color:#10B981; color:#ECFDF5;'><b>Outcome:</b> {p_data[1]}</div>"
        matrix_html += f"</td>"
    matrix_html += "</tr>"
matrix_html += "</tbody></table>"

st.divider()
calc_height = max(500, len(sel_ind) * 300)
components.html(matrix_html, height=calc_height, scrolling=True)

# --- 8. ABOUT & CONTACT ---
st.divider()
st.write("### The Sovereign Strategic Ecosystem")
st.write("Ingenero360AI represents the peak of industrial digital transformation. We don't just build dashboards; we deploy the digital intelligence required to drive the world's most complex plants to their true technical and economic potential.")

with st.form("contact"):
    st.write("### Consult a Strategic Advisory Partner")
    cl, cr = st.columns(2)
    with cl: st.text_input("Name / Title")
    with cr: st.text_input("Corporate Email")
    st.selectbox("Industry Focus", INDUSTRIES)
    st.form_submit_button("Request Executive Briefing")

st.markdown("<center style='color:#475569; margin:60px 0;'>Ingenero360AI | Sovereign Strategic Intelligence</center>", unsafe_allow_html=True)
