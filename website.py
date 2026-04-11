import streamlit as st
import streamlit.components.v1 as components

# --- 1. CONFIGURATION & PAGE SETUP ---
st.set_page_config(
    page_title="Ingenero360AI | Sovereign Strategic Brain", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. PREMIUM BRANDED THEME ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono:wght@500&display=swap');
    
    .main { background-color: #0B0F19; font-family: 'Inter', sans-serif; color: #E2E8F0; }
    
    /* CLEAN PROMINENT HEADER */
    .nav-header {
        display: flex; align-items: center; justify-content: space-between;
        padding: 30px 60px; background: #0F172A; 
        border-bottom: 4px solid #F97316; /* Ingenero Orange */
        position: sticky; top: 0; z-index: 1000;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    }
    .hero { text-align: center; padding: 120px 60px; background: radial-gradient(circle at top right, #1E293B, #0B0F19); }
    .hero h1 { font-size: 82px; font-weight: 800; letter-spacing: -4px; color: white; margin-bottom: 0px; line-height: 1; }
    .hero-tag { font-size: 18px; color: #F97316; font-weight: 800; text-transform: uppercase; letter-spacing: 5px; margin-bottom: 25px; }

    /* ARCHITECTURE BRIEF BOX */
    .agentic-box {
        background: rgba(56, 189, 248, 0.08); border: 1.5px solid rgba(56, 189, 248, 0.2);
        padding: 35px; border-radius: 16px; margin: 40px 60px; line-height: 1.6;
    }

    /* HORIZONTAL AGENT FLOW */
    .horizon-scroll { display: flex; align-items: center; gap: 15px; padding: 40px; overflow-x: auto; justify-content: center; }
    .agent-node {
        min-width: 190px; padding: 22px; border-radius: 14px; border: 1.5px solid rgba(255,255,255,0.1);
        background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(12px); transition: 0.3s;
    }
    .role-tag { font-size: 9px; font-weight: 900; color: #38BDF8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }
    .agent-title { font-size: 14px; font-weight: 700; color: white; margin-bottom: 6px; }
    .agent-desc { font-size: 11px; color: #94A3B8; line-height: 1.5; }

    /* HIGHLIGHTS */
    .u-brain { border-color: #F97316; box-shadow: 0 0 25px rgba(249, 115, 22, 0.2); }
    .u-brain .role-tag { color: #F97316; }
    .u-result { border-color: #10B981; }
    .u-result .role-tag { color: #10B981; }

    /* MATRIX DYNAMICS */
    .matrix-wrapper { padding: 20px 60px; }
    table { width: 100%; border-collapse: separate; border-spacing: 12px; }
    th { background: #1E293B; color: #94A3B8; font-size: 12px; padding: 20px; border-radius: 10px; text-transform: uppercase; letter-spacing: 1px; }
    td { background: rgba(30, 41, 59, 0.4); border-radius: 12px; padding: 25px; vertical-align: top; border: 1px solid rgba(255,255,255,0.06); }
    .bullet-item { border-left: 3px solid #F97316; padding-left: 12px; margin-bottom: 15px; font-size: 13px; color: #CBD5E1; }
    
    /* RADIO OVERRIDE */
    .stRadio > label { color: #F97316 !important; font-weight: 800 !important; font-size: 14px !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. PROMINENT HEADER & HERO ---
st.markdown(f"""
    <div class="nav-header">
        <div style="display:flex; align-items:center;">
            <div style="font-size:32px; font-weight:800; color:white; letter-spacing:-1px;">INGERO360AI</div>
            <div style="margin-left:25px; font-size:11px; color:#F97316; font-weight:700; text-transform:uppercase; letter-spacing:3px;">Sovereign Strategic Ecosystem</div>
        </div>
        <div style="font-size:13px; color:#94A3B8; font-weight:700;">DIGITAL FOUNDATIONS TO STRATEGIC AUTONOMY</div>
    </div>
    
    <div class="hero">
        <div class="hero-tag">Alchemy of Industrial Inference</div>
        <h1>Noise into <span style="color:#F97316">Knowledge</span></h1>
        <p style="font-size:24px; color:#94A3B8; max-width:900px; margin:25px auto;">
            Ingenero360AI is the only autonomous brain that deciphers industrial chaos, 
            applies engineering DNA, and executes strategic executive intent.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- 4. AGENTIC ARCHITECTURE BRIEF ---
st.markdown("""
    <div class="agentic-box">
        <span style="color:#38BDF8; font-weight:800; text-transform:uppercase; font-size:12px; letter-spacing:2px; display:block; margin-bottom:10px;">Agentic-AI Architecture</span>
        <span style="font-size:16px; color:#F1F5F9;">
            The Ingenero360AI ecosystem utilizes a modular <b>Multi-Agent System (MAS)</b>. 
            The base infrastructure (Sensing, Sentinel, and Guardrails) provides the technology-specific foundation. 
            The <b>Strategic Sub-Agents</b> (Optimizer and Result Bus) are stacked incrementally to target 
            specific multi-million dollar business outcomes.
        </span>
    </div>
""", unsafe_allow_html=True)

# --- 5. THE AGENT FLOW (HORIZONTAL) ---
st.write("### The Coordinated Brain: Sub-Agent Workflow")
st.markdown("""
<div class="horizon-scroll">
    <div class="agent-node">
        <div class="role-tag">The Conductor</div>
        <div class="agent-title">Master Orchestrator</div>
        <div class="agent-desc">Governance sub-agent using <b>GenAI</b> to sync fleet intent.</div>
    </div>
    <div style="color:#475569;">➔</div>
    <div class="agent-node">
        <div class="role-tag">The Seer</div>
        <div class="agent-title">Sensing Agent</div>
        <div class="agent-desc">DNA sub-agent calculating hidden <b>Soft Sensors</b>.</div>
    </div>
    <div style="color:#475569;">➔</div>
    <div class="agent-node" style="border-color:#38BDF8;">
        <div class="role-tag" style="color:#38BDF8;">The Time-Traveler</div>
        <div class="agent-title">Trend Sentinel</div>
        <div class="agent-desc">Predicts future process drifts and <b>Anomalies</b>.</div>
    </div>
    <div style="color:#475569;">➔</div>
    <div class="agent-node">
        <div class="role-tag">The Sentinel</div>
        <div class="agent-title">Guardrail Agent</div>
        <div class="agent-desc">Enforces metallurgical and safety limits 24/7.</div>
    </div>
    <div style="color:#F97316;">★</div>
    <div class="agent-node u-brain">
        <div class="role-tag">The Alchemist</div>
        <div class="agent-title">Optimizer Agent</div>
        <div class="agent-desc">Strategic brain solving complex <b>MINLP</b> math.</div>
    </div>
    <div style="color:#10B981;">➔</div>
    <div class="agent-node u-result">
        <div class="role-tag">The Oracle</div>
        <div class="agent-title">Result Bus Agent</div>
        <div class="agent-desc">Forecasts ROI via <b>What-If</b> simulations.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. ROI METRICS ---
st.markdown("""
<div style="display: flex; justify-content: space-around; padding: 70px 0; background: #0F172A; border-radius: 20px; margin: 40px 60px;">
    <div style="text-align: center;">
        <div style="font-size: 72px; font-weight: 800; color: #10B981;">$100M+</div>
        <div style="font-size: 15px; color: #94A3B8; text-transform: uppercase; font-weight: 800;">Realized Client ROI</div>
    </div>
    <div style="text-align: center;">
        <div style="font-size: 72px; font-weight: 800; color: #38BDF8;">$500M+</div>
        <div style="font-size: 15px; color: #94A3B8; text-transform: uppercase; font-weight: 800;">Identified Pipeline</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 7. STRATEGIC SOLUTION MATRIX (FULL VIEW) ---
st.write("### Strategic Solution Matrix: Industries & Products")

INDUSTRIES = ["Olefins", "Refining", "Ammonia/Urea", "Methanol", "EO/EG", "MTBE", "Aromatics", "Polymers", "Phenols", "ASU", "Utilities"]
PRODUCTS = ["Production Efficiency", "Energy Optimization", "Reliability", "Sustainability Hub", "Workflows"]

row_nav, col_nav = st.columns([1, 1])
with row_nav: sel_ind = st.multiselect("Select Focus Industries", INDUSTRIES, default=["Olefins", "Refining"])
with col_nav: sel_prod = st.multiselect("Select Focus Products", PRODUCTS, default=["Production Efficiency"])

DNA_MAP = { 
    "Olefins": "Furnace Kinetics / TMT Safety", "Refining": "Fractionation / ASTM Specs", "Ammonia/Urea": "Synthesis Loop / Conv. Temp",
    "Methanol": "SMR Kinetics / S/C Ratio", "EO/EG": "Selectivity / Vapor Guard", "MTBE": "Etherification / Reflux",
    "Aromatics": "Hydro-Separation / Purity", "Polymers": "Reaction Rate / Melt Index", "Phenols": "Oxidation Rate / Peroxide Guard", 
    "ASU": "Cryo-Sep / O2 Purity", "Utilities": "Steam Header / HP-LP Balance" 
}

PRODUCT_INTEL = { 
    "Production Efficiency": ["Yield Maximizer", "Throughput Advisory", "MINLP"], 
    "Energy Optimization": ["SEC Optimizer", "Energy Intensity", "LP"],
    "Reliability": ["RUL Optimizer", "Maintenance Hub", "Predictive"], 
    "Sustainability Hub": ["Carbon Optimizer", "ESG Compliance", "Forecasting"],
    "Workflows": ["SOP Compliance", "Handover Bus", "GenAI"] 
}

# Generate Table with Dynamic Height to prevent cutting
matrix_html = "<table style='table-layout: fixed;'><thead><tr><th style='width:150px;'>Industry</th>" + "".join([f"<th>{p}</th>" for p in sel_prod]) + "</tr></thead><tbody>"
for ind in sel_ind:
    matrix_html += f"<tr><td style='font-weight:800; color:#F97316; font-size:14px;'>{ind}</td>"
    for prod in sel_prod:
        p_data = PRODUCT_INTEL[prod]
        matrix_html += f"<td>"
        matrix_html += f"<div class='bullet-item' style='color:#94A3B8;'><b>Foundation DNA:</b><br>{DNA_MAP[ind]}</div>"
        matrix_html += f"<div class='bullet-item' style='border-color:#F97316; color:white;'><b>Strategy Brain:</b> {p_data[0]}<br><small style='color:#F97316;'>{p_data[2]} Models</small></div>"
        matrix_html += f"<div class='bullet-item' style='border-color:#10B981; color:#ECFDF5;'><b>Outcome:</b> {p_data[1]}</div>"
        matrix_html += f"</td>"
    matrix_html += "</tr>"
matrix_html += "</tbody></table>"

# Dynamic height adjustment
calc_height = max(500, len(sel_ind) * 280)
st.divider()
components.html(matrix_html, height=calc_height, scrolling=True)

# --- 8. FOOTER & CONTACT ---
st.divider()
st.write("### The Sovereign Strategic Ecosystem")
st.write("Ingenero360AI is the culmination of decades of deep-tier engineering expertise and modern autonomous agentic design. We don't just build dashboards; we deploy the digital intelligence required to drive the world's most complex plants to their true technical and economic potential.")

with st.form("contact"):
    st.write("### Consult an Expert Strategic Advisor")
    c_left, c_right = st.columns(2)
    with c_left: st.text_input("Corporate Name")
    with c_right: st.text_input("Corporate Email")
    st.selectbox("Select Target Industry", INDUSTRIES)
    st.form_submit_button("Request Executive Strategy Session")

st.markdown("<center style='color:#475569; margin:40px 0;'>Ingenero360AI | Sovereign Strategic Intelligence</center>", unsafe_allow_html=True)
