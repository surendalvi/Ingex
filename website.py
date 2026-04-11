import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(page_title="Ingenero360AI | Strategic Agentic-AI", layout="wide", initial_sidebar_state="collapsed")

# --- THEME & STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono:wght@500&display=swap');
    .main { background-color: #0F172A; font-family: 'Inter', sans-serif; color: white; }
    
    /* Header & Hero */
    .hero-section {
        padding: 80px 40px; text-align: center;
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
        border-bottom: 3px solid #F97316;
    }
    .hero-h1 { font-size: 56px; font-weight: 800; letter-spacing: -2px; margin-bottom: 10px; color: white; }
    .orange-text { color: #F97316; }
    
    /* Info Boxes */
    .info-card {
        background: rgba(30, 41, 59, 0.5); padding: 30px; border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;
    }
    .stat-box { text-align: center; padding: 40px; background: #1E293B; border-radius: 20px; border-top: 5px solid #10B981; }
    .stat-val { font-size: 48px; font-weight: 800; color: #10B981; }

    /* Matrix Styling */
    .matrix-cell {
        background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255,255,255,0.1);
        border-radius: 10px; padding: 15px; margin-bottom: 10px;
    }
    .sub-agent-label { font-size: 9px; font-weight: 900; color: #38BDF8; text-transform: uppercase; }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
tabs = st.tabs(["🏠 Home", "🧠 Architecture", "📊 Strategic Matrix", "📈 Impact & About"])

# --- TAB 1: HOME (THE PITCH) ---
with tabs[0]:
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-h1">Ingenero<span class="orange-text">360AI</span></h1>
        <p style="font-size:22px; color:#94A3B8; max-width:900px; margin:0 auto;">
            The Strategic Multi-Agent Ecosystem for Industrial Autonomy. 
            Deploy the <b>Strategic Brain</b> that orchestrates profit, reliability, and sustainability.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("## Why Ingenero360AI?")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="info-card"><h3>Agentic Autonomy</h3><p>Beyond monitoring. Autonomous Sub-Agents (L0-L4) negotiate constraints to find the global optimum.</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="info-card"><h3>Industry DNA</h3><p>Pre-configured Parent Agents for Olefins, Refining, and Ammonia. Physics-ready from Day 1.</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="info-card"><h3>Strategic ROI</h3><p>Specifically designed to solve multi-objective goals: High Yields, Low Carbon, Zero Failure.</p></div>""", unsafe_allow_html=True)

# --- TAB 2: ARCHITECTURE (THE AGENTS) ---
with tabs[1]:
    st.write("## The 5-Level Agentic Architecture")
    st.info("Ingenero360AI is powered by a hierarchy of specialized Sub-Agents. This modularity allows us to build a 'Common DNA' for your technology while hot-swapping 'Uncommon Intelligence' for your specific goals.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        #### Foundational Sub-Agents (Common)
        * **L0 Master Orchestrator:** Fleet governance & GenAI coordination.
        * **L1 Sensing Sub-Agents:** High-fidelity Physics & Soft Sensors.
        * **L2 Guardrail Sub-Agents:** Safety & Metallurgical constraints.
        """)
    with col_b:
        st.markdown("""
        #### Strategic Sub-Agents (Uncommon)
        * **L3 Optimizer Sub-Agents:** The Brain (MINLP / Predictive RUL).
        * **L4 Result Bus Sub-Agents:** Forecasted Advisory & Actionable KPIs.
        """)

# --- TAB 3: STRATEGIC MATRIX (INTERACTIVE) ---
with tabs[2]:
    st.write("## Strategic Solution Matrix")
    st.write("Select your Parent and Child agents to see the Agentic-AI configuration.")
    
    # Simple Matrix Logic
    parents = ["Olefins", "Refining", "Ammonia", "Methanol", "Utilities"]
    children = ["Production Efficiency", "Energy Optimization", "Reliability", "Sustainability"]
    
    sel_p = st.selectbox("Select Technology (Parent Agent)", parents)
    sel_c = st.selectbox("Select Initiative (Child Agent)", children)
    
    st.markdown(f"""
    <div style="background:#1E293B; padding:30px; border-radius:15px; border-left:5px solid #F97316;">
        <h3>Configuration: {sel_p} + {sel_c}</h3>
        <div class="matrix-cell">
            <div class="sub-agent-label">Base Foundation Sub-Agents</div>
            <p>• {sel_p} Kinetic Model (L1)<br>• {sel_p} Safety Guardrail (L2)</p>
        </div>
        <div class="matrix-cell" style="border-color:#F97316;">
            <div class="sub-agent-label" style="color:#F97316;">+ Incremental Strategy Sub-Agents</div>
            <p>• {sel_c} Optimizer (L3)<br>• {sel_c} Result Bus (L4)</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- TAB 4: IMPACT & CONTACT ---
with tabs[3]:
    st.write("## Proven Global Impact")
    v1, v2 = st.columns(2)
    with v1:
        st.markdown('<div class="stat-box"><div class="stat-val">$100M+</div><div style="color:#94A3B8;">Realized Client ROI</div></div>', unsafe_allow_html=True)
    with v2:
        st.markdown('<div class="stat-box" style="border-color:#38BDF8;"><div class="stat-val" style="color:#38BDF8;">$500M+</div><div style="color:#94A3B8;">Identified Potential</div></div>', unsafe_allow_html=True)
    
    st.write("### What Our Clients Say")
    st.markdown("> \"Ingenero360AI didn't just give us data; it gave us a strategy. We saw a 3% yield increase in 60 days.\" — *VP Operations, Global Petrochemical Major*")
    
    st.divider()
    st.write("### Contact Our Strategic Advisory Team")
    with st.form("contact"):
        st.text_input("Name")
        st.text_input("Email")
        st.selectbox("Interest", ["Olefins", "Refining", "Sustainability", "General Inquiry"])
        st.form_submit_button("Request Executive Briefing")

st.markdown("<center style='color:#475569; margin-top:50px;'>Ingenero.AI | Digital Foundations to Strategic Autonomy</center>", unsafe_allow_html=True)
