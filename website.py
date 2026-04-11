import streamlit as st
import streamlit.components.v1 as components

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Ingenero360AI | Strategic Brain", layout="wide", initial_sidebar_state="collapsed")

# --- 2. PREMIUM THEME ENGINE ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono:wght@500&display=swap');
    .main { background-color: #0B0F19; font-family: 'Inter', sans-serif; color: #E2E8F0; }
    
    /* Prominent Clean Header */
    .nav-header {
        display: flex; align-items: center; justify-content: space-between;
        padding: 25px 50px; background: #0F172A; border-bottom: 3px solid #F97316;
        position: sticky; top: 0; z-index: 1000; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .hero { text-align: center; padding: 100px 50px; background: radial-gradient(circle at top right, #1E293B, #0B0F19); }
    .hero h1 { font-size: 72px; font-weight: 800; letter-spacing: -3px; color: white; margin-bottom: 0px; }
    .hero-tag { font-size: 18px; color: #F97316; font-weight: 800; text-transform: uppercase; letter-spacing: 4px; margin-bottom: 20px; }
    
    /* Agent Flow (Horizontal) */
    .horizon-container { display: flex; align-items: center; gap: 15px; padding: 40px; overflow-x: auto; justify-content: center; }
    .agent-node {
        min-width: 200px; padding: 20px; border-radius: 12px; border: 1.5px solid rgba(255,255,255,0.1);
        background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(10px);
    }
    .role-tag { font-size: 9px; font-weight: 900; color: #38BDF8; text-transform: uppercase; margin-bottom: 5px; }
    .agent-title { font-size: 14px; font-weight: 700; color: white; margin-bottom: 5px; }
    .agent-desc { font-size: 11px; color: #94A3B8; line-height: 1.4; }

    /* Highlights for Uncommon Agents */
    .u-brain { border-color: #F97316; box-shadow: 0 0 15px rgba(249, 115, 22, 0.2); }
    .u-brain .role-tag { color: #F97316; }
    .u-result { border-color: #10B981; }
    .u-result .role-tag { color: #10B981; }

    /* Matrix Table */
    .matrix-wrapper { overflow-x: auto; padding: 20px; }
    table { width: 100%; border-collapse: separate; border-spacing: 10px; }
    th { background: #1E293B; color: #94A3B8; font-size: 11px; padding: 15px; border-radius: 8px; text-transform: uppercase; }
    td { background: rgba(30, 41, 59, 0.4); border-radius: 10px; padding: 20px; vertical-align: top; border: 1px solid rgba(255,255,255,0.05); }
    .bullet { border-left: 3px solid #F97316; padding-left: 10px; margin-bottom: 10px; font-size: 13px; }
</style>
""", unsafe_allow_html=True)

# --- 3. HEADER & HERO ---
st.markdown(f"""
    <div class="nav-header">
        <div style="display:flex; align-items:center;">
            <div style="font-size:28px; font-weight:800; color:white; letter-spacing:-1px;">INGERO360AI</div>
            <div style="margin-left:20px; font-size:10px; color:#F97316; font-weight:700; text-transform:uppercase; letter-spacing:2px;">The Strategic Multi-Agent Ecosystem</div>
        </div>
        <div style="font-size:12px; color:#94A3B8; font-weight:600;">AUTONOMOUS INDUSTRIAL BRAIN</div>
    </div>
    
    <div class="hero">
        <div class="hero-tag">From Foundations to Autonomy</div>
        <h1>Transform Noise into <span style="color:#F97316">Knowledge</span></h1>
        <p style="font-size:22px; color:#94A3B8; max-width:850px; margin:20px auto;">
            Ingenero360AI is the only ecosystem that deciphers raw plant noise, applies deep engineering DNA, 
            and executes strategic intent at scale.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- 4. DATA ALCHEMY SECTION ---
st.markdown("""
<div style="padding: 60px; background: #1E293B; margin: 40px; border-radius: 20px; border-left: 6px solid #38BDF8;">
    <h2 style="color:white; margin-bottom:15px;">The Alchemy of Inference</h2>
    <p style="font-size:18px; color:#CBD5E1; line-height:1.6;">
        Raw data says: <i>"Compressor Power is 12MW."</i><br>
        <b>Ingenero360AI infers:</b> <i>"You can shift 20% of the cooling load to the night shift to save $45,000 in energy costs today."</i><br><br>
        This is the magic of <b>Agentic-AI</b>. We don't just display data; our autonomous Sub-Agents 
        negotiate physics, safety, and profit to tell you <b>what is possible</b>.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 5. AGENTIC ARCHITECTURE (HORIZONTAL) ---
st.write("### The Agentic Ecosystem: A Coordinated Brain")
st.markdown("""
<div class="horizon-container">
    <div class="agent-node">
        <div class="role-tag">The Grand Conductor</div>
        <div class="agent-title">Master Orchestrator</div>
        <div class="agent-desc">Governance Sub-Agent. Synchronizes fleet intent using <b>GenAI</b>.</div>
    </div>
    <div style="color:#475569;">➔</div>
    <div class="agent-node">
        <div class="role-tag">The Physics Seer</div>
        <div class="agent-title">Sensing Sub-Agent</div>
        <div class="agent-desc">DNA Sub-Agent. Uses <b>Soft Sensors</b> to see unmeasured variables.</div>
    </div>
    <div style="color:#475569;">➔</div>
    <div class="agent-node">
        <div class="role-tag">The Time-Traveler</div>
        <div class="agent-title">Trend Sentinel</div>
        <div class="agent-desc">Pattern Sub-Agent. Predicts future process drifts and anomalies.</div>
    </div>
    <div style="color:#475569;">➔</div>
    <div class="agent-node">
        <div class="role-tag">The Safety Sentinel</div>
        <div class="agent-title">Guardrail Sub-Agent</div>
        <div class="agent-desc">Safety Sub-Agent. Enforces metallurgical and design limits 24/7.</div>
    </div>
    <div style="color:#F97316;">★</div>
    <div class="agent-node u-brain">
        <div class="role-tag">The Strategy Alchemist</div>
        <div class="agent-title">Optimizer Sub-Agent</div>
        <div class="agent-desc"><b>Strategic Brain.</b> Solves complex <b>MINLP</b> to find the global optimum.</div>
    </div>
    <div style="color:#10B981;">➔</div>
    <div class="agent-node u-result">
        <div class="role-tag">The Executive Oracle</div>
        <div class="agent-title">Result Bus Sub-Agent</div>
        <div class="agent-desc"><b>Strategic Outcome.</b> Forecasts ROI and delivers <b>What-If</b> simulations.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. ROI SECTION ---
st.markdown("""
<div style="display: flex; justify-content: space-around; padding: 60px 0; background: #0F172A; border-radius: 20px; margin: 40px;">
    <div style="text-align: center;">
        <div style="font-size: 64px; font-weight: 800; color: #10B981;">$100M+</div>
        <div style="font-size: 14px; color: #94A3B8; text-transform: uppercase; font-weight: 700;">Realized Client ROI</div>
    </div>
    <div style="text-align: center;">
        <div style="font-size: 64px; font-weight: 800; color: #38BDF8;">$500M+</div>
        <div style="font-size: 14px; color: #94A3B8; text-transform: uppercase; font-weight: 700;">Identified Potential</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 7. STRATEGIC MATRIX (INDUSTRIES & PRODUCTS) ---
st.write("### Strategic Solution Matrix")
INDUSTRIES = ["Olefins", "Refining", "Ammonia/Urea", "Methanol", "EO/EG", "MTBE", "Polymers", "Phenols", "ASU", "Utilities"]
PRODUCTS = ["Production Efficiency", "Energy Optimization", "Reliability", "Sustainability Hub", "Workflows"]

row_nav, col_nav = st.columns(2)
with row_nav: sel_ind = st.multiselect("Select Industries", INDUSTRIES, default=["Olefins"])
with col_nav: sel_prod = st.multiselect("Select Products", PRODUCTS, default=["Production Efficiency"])

# Matrix Data
DNA = { "Olefins": "Furnace Kinetics / TMT Safety", "Refining": "Fractionation / ASTM Specs", "Ammonia/Urea": "Synthesis / Conv. Temp",
       "Methanol": "SMR Kinetics / S/C Ratio", "EO/EG": "Selectivity / Vapor Guard", "MTBE": "Etherification / Reflux",
       "Polymers": "Reaction Rate / Melt Index", "Phenols": "Oxidation / Peroxide Guard", "ASU": "Cryo-Sep / O2 Purity", "Utilities": "Steam Header / Emissions" }
INTEL = { "Production Efficiency": ["Yield Maximizer", "Throughput Advisory", "MINLP"], "Energy Optimization": ["SEC Optimizer", "Energy Intensity", "LP"],
         "Reliability": ["RUL Optimizer", "Maintenance Hub", "Predictive"], "Sustainability Hub": ["Carbon Optimizer", "ESG Dashboard", "Forecast"],
         "Workflows": ["SOP Compliance", "Handover Bus", "GenAI"] }

matrix_html = "<table><thead><tr><th></th>" + "".join([f"<th>{p}</th>" for p in sel_prod]) + "</tr></thead><tbody>"
for ind in sel_ind:
    matrix_html += f"<tr><td style='font-weight:800; color:#F97316;'>{ind}</td>"
    for prod in sel_prod:
        p_data = INTEL[prod]
        matrix_html += f"<td><div class='bullet' style='color:#94A3B8;'><b>Foundation DNA:</b><br>{DNA[ind]}</div>"
        matrix_html += f"<div class='bullet' style='border-color:#F97316; color:white;'><b>Brain:</b> {p_data[0]}<br><small style='color:#F97316;'>{p_data[2]} Models</small></div>"
        matrix_html += f"<div class='bullet' style='border-color:#10B981; color:#ECFDF5;'><b>Outcome:</b> {p_data[1]}</div></td>"
    matrix_html += "</tr>"
matrix_html += "</tbody></table>"

components.html(matrix_html, height=600, scrolling=True)

# --- 8. ABOUT & CONTACT ---
st.divider()
st.write("### The Sovereign Strategic Ecosystem")
st.write("Ingenero360AI is the culmination of decades of deep-tier engineering expertise and modern autonomous agentic design. We don't just build dashboards; we deploy the digital intelligence required to drive the world's most complex plants to their true technical and economic potential.")

with st.form("contact"):
    st.write("### Consult an Expert Strategy Partner")
    st.text_input("Corporate Name")
    st.text_input("Corporate Email")
    st.selectbox("Industry Focus", INDUSTRIES)
    st.form_submit_button("Request Executive Briefing")

st.markdown("<center style='color:#475569; margin:40px 0;'>Ingenero360AI | Sovereign Strategic Intelligence</center>", unsafe_allow_html=True)
