import streamlit as st
import streamlit.components.v1 as components

# --- 1. CONFIG & BRANDING ---
st.set_page_config(page_title="Ingenero360AI | Strategic Brain", layout="wide")

logo_url = "https://raw.githubusercontent.com/surendalvi/Ingex/main/logo.png"

# --- 2. PREMIUM CLEAN THEME (CSS) ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono:wght@500&display=swap');
    
    .main .block-container {{ padding: 0 !important; background-color: #0F172A; font-family: 'Inter', sans-serif; color: white; }}
    
    /* PROMINENT HEADER */
    .nav-header {{
        display: flex; align-items: center; justify-content: space-between;
        padding: 30px 60px; background: rgba(15, 23, 42, 0.9);
        border-bottom: 4px solid #F97316; sticky: top; z-index: 100;
    }}

    /* HERO SECTION: DATA ALCHEMY */
    .hero {{
        text-align: center; padding: 100px 60px;
        background: radial-gradient(circle at top right, #1E293B, #0F172A);
    }}
    .hero h1 {{ font-size: 72px; font-weight: 800; letter-spacing: -3px; margin-bottom: 10px; }}
    .hero p {{ font-size: 22px; color: #94A3B8; max-width: 800px; margin: 0 auto; line-height: 1.6; }}

    /* ALCHEMY BOX */
    .alchemy-section {{
        padding: 60px; background: #1E293B; margin: 40px; border-radius: 20px;
        border-left: 6px solid #38BDF8;
    }}

    /* AGENTIC FLOW (HORIZONTAL) */
    .horizon-scroll {{
        display: flex; align-items: center; gap: 20px; padding: 40px;
        overflow-x: auto; justify-content: center;
    }}
    .agent-node {{
        min-width: 260px; padding: 25px; border-radius: 15px; border: 1px solid rgba(255,255,255,0.1);
        background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(10px); text-align: left;
    }}
    .role-tag {{ font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; }}
    .agent-title {{ font-size: 18px; font-weight: 700; color: white; margin-bottom: 10px; }}
    .agent-desc {{ font-size: 12px; color: #94A3B8; line-height: 1.4; }}

    /* COLOR CODING */
    .c-foundational {{ border-color: #475569; }}
    .c-foundational .role-tag {{ color: #38BDF8; }}
    
    .c-strategic {{ border-color: #F97316; box-shadow: 0 0 20px rgba(249, 115, 22, 0.15); }}
    .c-strategic .role-tag {{ color: #F97316; }}

    /* ROI STATS */
    .roi-grid {{ display: flex; justify-content: space-around; padding: 60px; }}
    .roi-card {{ text-align: center; }}
    .roi-val {{ font-size: 64px; font-weight: 800; color: #10B981; }}
    .roi-sub {{ font-size: 14px; color: #94A3B8; text-transform: uppercase; font-weight: 700; }}

    /* MATRIX TABLE */
    .matrix-container {{ padding: 40px; }}
    table {{ width: 100%; border-collapse: separate; border-spacing: 10px; }}
    td {{ background: rgba(30, 41, 59, 0.4); border-radius: 12px; padding: 20px; vertical-align: top; border: 1px solid rgba(255,255,255,0.05); }}
    .bullet-list {{ list-style-type: none; padding: 0; }}
    .bullet-item {{ margin-bottom: 12px; font-size: 13px; color: #F1F5F9; border-left: 3px solid #F97316; padding-left: 10px; }}
</style>
""", unsafe_allow_html=True)

# --- 3. HEADER & HERO ---
st.markdown(f"""
    <div class="nav-header">
        <div style="display:flex; align-items:center;">
            <img src="{logo_url}" width="50" onerror="this.style.display='none'">
            <div style="margin-left:20px;">
                <div style="font-size:26px; font-weight:800; color:white; letter-spacing:-1px;">INGERO360AI</div>
                <div style="font-size:10px; color:#F97316; font-weight:700; text-transform:uppercase; letter-spacing:2px;">The Strategic Multi-Agent Ecosystem</div>
            </div>
        </div>
        <div style="font-size:12px; color:#94A3B8; font-weight:600;">OPERATIONAL TOOLKIT ➔ STRATEGIC BRAIN</div>
    </div>
    
    <div class="hero">
        <h1>Transform Noise into <span style="color:#F97316">Knowledge</span></h1>
        <p>Industrial data is chaotic. Ingenero360AI is the <b>Autonomous Brain</b> that deciphers the noise, 
        applies engineering DNA, and executes strategic intent at scale.</p>
    </div>
""", unsafe_allow_html=True)

# --- 4. THE DATA ALCHEMY SECTION ---
st.markdown("""
<div class="alchemy-section">
    <h2 style="color:white; margin-bottom:15px;">The Alchemy of Inference</h2>
    <p style="font-size:18px; color:#CBD5E1; line-height:1.6;">
        Raw data says: "Pressure is 40 bar."<br>
        <b>Ingenero360AI infers:</b> "You can increase throughput by 4% while staying 12% below your carbon ceiling."<br><br>
        This is the magic of <b>Agentic-AI</b>. We don't just show you what is happening; our specialized Sub-Agents 
        negotiate physics, safety, and profit to tell you <b>what is possible</b>.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 5. THE HORIZONTAL AGENTIC FLOW ---
st.write("### The Agentic Architecture: A Coordinated Brain")
st.markdown("""
<div class="horizon-scroll">
    <div class="agent-node c-foundational">
        <div class="role-tag">The Grand Conductor</div>
        <div class="agent-title">Master Orchestrator</div>
        <div class="agent-desc">Governance Sub-Agent. Synchronizes fleet intent using <b>GenAI (LLM)</b> and Multi-Variate Analysis.</div>
    </div>
    <div style="color:#475569; font-size:24px;">➔</div>
    <div class="agent-node c-foundational">
        <div class="role-tag">The Physics Seer</div>
        <div class="agent-title">Sensing Sub-Agent</div>
        <div class="agent-desc">DNA Sub-Agent. Uses <b>Soft Sensors</b> and high-fidelity kinetics to see unmeasured variables.</div>
    </div>
    <div style="color:#475569; font-size:24px;">➔</div>
    <div class="agent-node c-foundational">
        <div class="role-tag">The Safety Sentinel</div>
        <div class="agent-title">Guardrail Sub-Agent</div>
        <div class="agent-desc">Safety Sub-Agent. Monitors <b>Metallurgical Bounds</b> and environmental ceilings 24/7.</div>
    </div>
    <div style="color:#F97316; font-size:24px;">★</div>
    <div class="agent-node c-strategic">
        <div class="role-tag">The Strategy Alchemist</div>
        <div class="agent-title">Optimizer Sub-Agent</div>
        <div class="agent-desc"><b>Strategic Increment.</b> Solves complex <b>MINLP</b> to find the global optimum for your goal.</div>
    </div>
    <div style="color:#F97316; font-size:24px;">➔</div>
    <div class="agent-node c-strategic" style="border-color:#10B981;">
        <div class="role-tag" style="color:#10B981;">The Executive Oracle</div>
        <div class="agent-title">Result Bus Sub-Agent</div>
        <div class="agent-desc"><b>Strategic Outcome.</b> Forecasts ROI and delivers <b>What-If</b> simulations to the board.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. ROI SECTION ---
st.markdown("""
<div class="roi-grid">
    <div class="roi-card">
        <div class="roi-val">$100M+</div>
        <div class="roi-sub">Realized Client ROI</div>
    </div>
    <div class="roi-card">
        <div class="roi-val" style="color:#38BDF8;">$500M+</div>
        <div class="roi-sub">Identified Potential</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 7. STRATEGIC MATRIX ---
st.write("### Strategic Initiative Matrix")
c1, c2 = st.columns(2)
with c1:
    sel_tech = st.radio("Select Technology (Parent DNA)", ["Olefins", "Refining", "Ammonia", "Methanol", "Utilities"], horizontal=True)
with c2:
    sel_init = st.radio("Select Strategy (Child Intent)", ["Production Efficiency", "Energy Optimization", "Reliability", "Sustainability"], horizontal=True)

# Dynamic content based on selection
st.markdown(f"""
<div class="matrix-container">
    <table>
        <tr>
            <td style="width:40%;">
                <div style="color:#38BDF8; font-size:10px; font-weight:800; margin-bottom:10px;">FOUNDATIONAL TECHNOLOGY DNA</div>
                <div class="bullet-item"><b>Sensing:</b> {sel_tech} Physics & Kinetic Sub-Agent</div>
                <div class="bullet-item"><b>Safety:</b> {sel_tech} Guardrail & Constraint Sub-Agent</div>
            </td>
            <td style="border: 2px dashed #F97316;">
                <div style="color:#F97316; font-size:10px; font-weight:800; margin-bottom:10px;">STRATEGIC INCREMENTAL INTELLIGENCE</div>
                <div class="bullet-item"><b>Optimizer:</b> {sel_init} Strategic Sub-Agent (MINLP)</div>
                <div class="bullet-item"><b>Result:</b> {sel_init} Outcome Sub-Agent (Forecasting)</div>
            </td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)

# --- 8. ABOUT & CONTACT ---
st.divider()
st.write("### About Ingenero.AI")
st.write("We are the pioneers of Agentic-AI for the process industries. By bridging the gap between deep-tier engineering physics and modern autonomous agents, we help the world's largest industrial complexes reach their true technical and economic potential.")

with st.form("contact"):
    st.write("### Request an Executive Strategy Session")
    st.text_input("Name")
    st.text_input("Corporate Email")
    st.selectbox("Technology of Interest", ["Olefins", "Refining", "Ammonia", "Sustainability"])
    st.form_submit_button("Consult an Expert")

st.markdown("<center style='color:#475569; margin:40px 0;'>Ingenero.AI | Digital Foundations to Strategic Autonomy</center>", unsafe_allow_html=True)
