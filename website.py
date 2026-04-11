import streamlit as st
import streamlit.components.v1 as components

# --- 1. CONFIGURATION & THEME ---
st.set_page_config(page_title="Ingenero360AI | The Strategic Brain", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono:wght@500&display=swap');
    
    .main { background-color: #0B0F1A; font-family: 'Inter', sans-serif; color: #E2E8F0; }
    
    /* Hero Branding */
    .hero-container {
        padding: 100px 50px; text-align: center;
        background: radial-gradient(circle at top right, #1E293B, #0B0F19);
        border-bottom: 2px solid #F97316; margin-bottom: 40px;
    }
    .hero-h1 { font-size: 72px; font-weight: 800; letter-spacing: -3px; color: white; margin-bottom: 0px; }
    .hero-tag { font-size: 20px; color: #F97316; font-weight: 700; text-transform: uppercase; letter-spacing: 4px; margin-bottom: 20px; }
    .hero-p { font-size: 22px; color: #94A3B8; max-width: 850px; margin: 0 auto; line-height: 1.6; }

    /* The Data Alchemy Section */
    .alchemy-box {
        background: linear-gradient(90deg, rgba(56, 189, 248, 0.05) 0%, rgba(15, 23, 42, 0) 100%);
        border-left: 4px solid #38BDF8; padding: 40px; border-radius: 0 15px 15px 0; margin: 50px 0;
    }

    /* Agent Cards */
    .agent-card {
        background: rgba(30, 41, 59, 0.4); padding: 30px; border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.05); height: 100%; transition: 0.4s;
    }
    .agent-card:hover { border-color: #F97316; transform: translateY(-10px); background: rgba(30, 41, 59, 0.6); }
    .agent-role { color: #F97316; font-weight: 800; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; }
    .agent-name { font-size: 22px; font-weight: 700; color: white; margin: 10px 0; }
    .agent-desc { font-size: 14px; color: #94A3B8; line-height: 1.5; }

    /* ROI Stats */
    .roi-section { display: flex; justify-content: space-around; padding: 60px 0; background: #0F172A; border-radius: 20px; margin: 40px 0; }
    .roi-item { text-align: center; }
    .roi-val { font-size: 56px; font-weight: 900; color: #10B981; }
    .roi-label { font-size: 14px; color: #94A3B8; text-transform: uppercase; font-weight: 700; }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] { gap: 40px; }
    .stTabs [data-baseweb="tab"] { font-size: 18px; font-weight: 700; color: #94A3B8; }
    .stTabs [aria-selected="true"] { color: #F97316 !important; }
</style>
""", unsafe_allow_html=True)

# --- 2. HERO SECTION ---
st.markdown("""
<div class="hero-container">
    <div class="hero-tag">Digital Foundations to Strategic Autonomy</div>
    <h1 class="hero-h1">Ingenero<span style="color:#F97316">360AI</span></h1>
    <p class="hero-p">
        Meet the <b>Strategic Brain</b> of the modern industrial enterprise. 
        A modular Multi-Agent Ecosystem that transforms raw data into high-margin autonomous inferences.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 3. THE DATA ALCHEMY (Importance of Analytics) ---
st.markdown("""
<div class="alchemy-box">
    <h2 style="color:white; margin-bottom:15px;">The Alchemy of Data Analytics</h2>
    <p style="font-size:18px; color:#CBD5E1; max-width:1000px;">
        Raw data is just noise—a chaotic stream of 1s and 0s from thousands of sensors. 
        <b>Analytics is the catalyst</b> that turns this noise into magic. By applying deep-tier physics 
        and Agentic-AI, we don't just see what is happening; we <b>infer what is possible</b>. 
        Raw data says "Temperature is 600°C." Ingenero360AI says "You can increase yield by 2.1% 
        without risking metallurgy." That is the power of a Strategic Brain.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 4. MEET THE AGENTS (Role-Based) ---
st.write("## Meet the Agents of Intelligence")
st.write("Our Multi-Agent System (MAS) replaces rigid code with autonomous roles.")

a_col1, a_col2, a_col3 = st.columns(3)
with a_col1:
    st.markdown("""
    <div class="agent-card">
        <div class="agent-role">The Grand Conductor</div>
        <div class="agent-name">L0: Master Orchestrator</div>
        <div class="agent-desc">Synchronizes all agents. It uses <b>GenAI</b> to translate complex plant physics into executive intent and ensures the fleet moves as one unit.</div>
    </div>
    """, unsafe_allow_html=True)
with a_col2:
    st.markdown("""
    <div class="agent-card">
        <div class="agent-role">The Physics Seer</div>
        <div class="agent-name">L1: Sensing Agent</div>
        <div class="agent-desc">The "Eyes" of the system. Uses <b>Soft Sensors</b> and kinetic models to see unmeasured variables—calculating catalyst health and internal purities in real-time.</div>
    </div>
    """, unsafe_allow_html=True)
with a_col3:
    st.markdown("""
    <div class="agent-card">
        <div class="agent-role">The Safety Sentinel</div>
        <div class="agent-name">L2: Guardrail Agent</div>
        <div class="agent-desc">The "Enforcer." It monitors metallurgical and environmental limits 24/7, ensuring that every profitable move remains 100% safe.</div>
    </div>
    """, unsafe_allow_html=True)

st.write("") # Spacer

a_col4, a_col5 = st.columns([1.5, 1.5])
with a_col4:
    st.markdown("""
    <div class="agent-card" style="border-color:#F97316;">
        <div class="agent-role" style="color:#F97316;">The Strategy Alchemist</div>
        <div class="agent-name">L3: Strategic Optimizer</div>
        <div class="agent-desc">The <b>"Brain"</b>. Using <b>MINLP</b> and <b>Optimizers</b>, it solves for the highest profit, lowest energy, or best reliability based on your chosen initiative.</div>
    </div>
    """, unsafe_allow_html=True)
with a_col5:
    st.markdown("""
    <div class="agent-card" style="border-color:#10B981;">
        <div class="agent-role" style="color:#10B981;">The Executive Oracle</div>
        <div class="agent-name">L4: Result Bus Agent</div>
        <div class="agent-desc">The <b>"Voice"</b>. It translates deep math into <b>Generative Advisory</b> and <b>What-If Forecasting</b>, showing you the exact ROI before you make a move.</div>
    </div>
    """, unsafe_allow_html=True)

# --- 5. TABS: INDUSTRIES & INITIATIVES ---
st.markdown("<br><br>", unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["🏗️ Industries Covered", "🎯 Strategic Initiatives", "📦 Product Package"])

with tab1:
    st.write("### Built-in Technology DNA")
    st.write("Ingenero360AI is pre-configured for the world's most complex industrial sectors.")
    ind_cols = st.columns(5)
    ind_cols[0].metric("Olefins", "Ethylene/Propylene")
    ind_cols[1].metric("Refining", "CDU/Coker/FCCU")
    ind_cols[2].metric("Ammonia", "Synthesis Loop")
    ind_cols[3].metric("Methanol", "Reformer Kinetics")
    ind_cols[4].metric("Utilities", "Steam/Power/Flare")

with tab2:
    st.write("### Hot-Swap Your Strategic Goal")
    st.write("Choose your 'Child Agent' to pivot the entire ecosystem's focus.")
    st.markdown("""
    - **📈 Production Efficiency:** Maximize yield and throughput (MINLP).
    - **⚡ Energy Optimization:** Minimize specific energy consumption (SEC).
    - **🛠️ Asset Reliability:** Predictive maintenance and RUL (Remaining Useful Life).
    - **🌱 Sustainability Hub:** Real-time Carbon Intensity & ESG tracking.
    """)

with tab3:
    st.write("### The Ingenero Portfolio")
    p1, p2 = st.columns(2)
    with p1:
        st.info("**IngeneroX (The Toolkit):** Digital enablement for engineers. The 'Tools' to monitor, analyze, and build.")
    with p2:
        st.success("**Ingenero360AI (The Brain):** The autonomous strategic ecosystem. The 'Solution' that orchestrates intent.")

# --- 6. ROI & TESTIMONIALS ---
st.markdown("""
<div class="roi-section">
    <div class="roi-item">
        <div class="roi-val">$100M+</div>
        <div class="roi-label">Realized Client ROI</div>
    </div>
    <div class="roi-item">
        <div class="roi-val" style="color:#38BDF8;">$500M+</div>
        <div class="roi-label">Identified Potential</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("### Voices of Authority")
st.markdown("> \"Ingenero360AI transformed our noise into knowledge. We identified $12M in energy savings within 90 days without replacing a single piece of hardware.\" — *Operations Director, Fortune 500 Petrochemical.*")

# --- 7. ABOUT & CONTACT ---
st.divider()
c_left, c_right = st.columns(2)
with c_left:
    st.write("### About Us")
    st.write("Ingenero is a global leader in industrial AI and specialized engineering. We bridge the gap between complex physics and digital intelligence, helping the world's largest plants reach their technical and economic potential.")

with c_right:
    st.write("### Request an Executive Briefing")
    with st.form("contact"):
        st.text_input("Name")
        st.text_input("Corporate Email")
        st.selectbox("Primary Interest", ["Olefins", "Refining", "Sustainability", "Reliability", "General Inquiry"])
        st.form_submit_button("Consult an Expert")

st.markdown("<center style='color:#475569; margin:40px 0;'>Ingenero.AI | 360-Degree Strategic Intelligence</center>", unsafe_allow_html=True)
