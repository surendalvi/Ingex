import streamlit as st
import streamlit.components.v1 as components

# --- 1. PAGE CONFIG & BRANDING ---
st.set_page_config(
    page_title="Ingenero360AI Strategic Horizon", 
    page_icon="↔️", 
    layout="wide"
)

# logo_url setup with safety fallback
logo_url = "https://raw.githubusercontent.com/surendalvi/Ingex/main/logo.png"

# --- 2. THE HORIZONTAL FLOW ENGINE (CSS) ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@500&display=swap');
    
    .main .block-container {{ padding: 1rem 2rem !important; background-color: #0F172A; font-family: 'Inter', sans-serif; color: white; }}
    
    /* NAV HEADER */
    .nav-header {{
        display: flex; align-items: center; padding: 15px 25px; 
        background: rgba(30, 41, 59, 0.4); border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px; border-radius: 12px;
    }}

    /* SELECTION RADIO CUSTOMIZATION */
    .stRadio > label {{ font-size: 11px !important; font-weight: 800 !important; color: #64748B !important; text-transform: uppercase; letter-spacing: 1px; }}
    div[role="radiogroup"] {{ gap: 10px; }}

    /* HORIZONTAL FLOW TREE */
    .horizon-container {{
        display: flex; align-items: center; justify-content: space-between;
        padding: 60px 20px; overflow-x: auto; min-width: 1200px;
    }}
    
    .node-group {{ display: flex; flex-direction: column; align-items: center; gap: 15px; position: relative; }}
    
    .node {{
        padding: 15px 20px; border-radius: 10px; border: 1.5px solid;
        text-align: left; width: 220px; min-height: 90px;
        background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(8px);
        transition: all 0.3s ease;
    }}
    
    .node .level-tag {{ 
        font-size: 9px; font-weight: 900; color: #38BDF8; margin-bottom: 5px; 
        text-transform: uppercase; letter-spacing: 1px; 
    }}
    .node .title {{ font-size: 13px; font-weight: 700; color: #F1F5F9; line-height: 1.3; }}
    .node .models {{ font-family: 'JetBrains Mono', monospace; font-size: 8px; color: #94A3B8; margin-top: 8px; }}

    /* COMMON NODES */
    .c-common {{ border-color: #475569; opacity: 0.8; }}
    
    /* UNCOMMON NODES (THE HIGHLIGHT) */
    .c-uncommon {{ 
        border-color: #F97316; border-width: 2px;
        box-shadow: 0 0 20px rgba(249, 115, 22, 0.2);
    }}
    .c-uncommon .level-tag {{ color: #F97316; }}
    
    .c-result {{ 
        border-color: #10B981; border-width: 2px;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.2);
    }}
    .c-result .level-tag {{ color: #10B981; }}

    /* HORIZONTAL CONNECTOR */
    .h-line {{ flex-grow: 1; height: 1.5px; background: rgba(255,255,255,0.1); margin: 0 10px; min-width: 40px; }}
</style>
""", unsafe_allow_html=True)

# --- 3. DATA REPOSITORY ---
PARENT_AGENTS = ["Olefins", "Methanol", "Ammonia", "EO/EG", "MTBE", "Polymers", "Phenols", "Refining", "ASU", "Utilities"]
CHILD_AGENTS = ["Production Efficiency", "Energy Optimization", "Reliability", "Sustainability Hub", "Workflows"]

TECH_MAP = {
    "Olefins": {"l1": ["Furnace Kinetic Agent", "CGC Efficiency Agent"], "l2": ["TMT Safety Guardrail", "Pass Flow Balance"]},
    "Methanol": {"l1": ["SMR Kinetic Agent", "SynGas Ratio Agent"], "l2": ["S/C Guardrail", "Catalyst ΔP Monitor"]},
    "Ammonia": {"l1": ["N2/H2 Balancer", "Shift Conv. Agent"], "l2": ["Converter Profile", "Inert Conc. Bounds"]},
    "EO/EG": {"l1": ["Selectivity Agent", "Glycol Ratio Agent"], "l2": ["Vapor Guardrail", "Heat Flux Tracking"]},
    "MTBE": {"l1": ["Etherification Agent", "Recovery Agent"], "l2": ["Reflux Ratio Bounds", "Feed Ratio Guard"]},
    "Polymers": {"l1": ["Reaction Rate Agent", "Grade Logic Agent"], "l2": ["Melt Index Consistency", "Pressure Guard"]},
    "Phenols": {"l1": ["Oxidation Agent", "Cleavage Yield Agent"], "l2": ["Peroxide Safety", "Tar Analytics"]},
    "Refining": {"l1": ["Fractionation Agent", "Coker Cycle Agent"], "l2": ["ASTM Product Specs", "Hydraulic Limits"]},
    "ASU": {"l1": ["Cryogenic Separation", "MAC Health Agent"], "l2": ["O2 Purity Target", "Thermal Profile"]},
    "Utilities": {"l1": ["Steam Header Agent", "Boiler Firing Agent"], "l2": ["HP/LP Load Balance", "Emissions Ceiling"]}
}

INIT_MAP = {
    "Production Efficiency": {"l3": "Yield Maximizer", "l4": "Throughput Advisory", "models": "MINLP · BENCHMARKING"},
    "Energy Optimization": {"l3": "SEC Optimizer", "l4": "Energy Intensity Bus", "models": "LP · SEC TRENDING"},
    "Reliability": {"l3": "RUL Optimizer", "l4": "Maintenance Advisory", "models": "PREDICTIVE RUL · FAILURE MODES"},
    "Sustainability Hub": {"l3": "Carbon Optimizer", "l4": "ESG Compliance Bus", "models": "FORECASTING · FLARE ANALYSIS"},
    "Workflows": {"l3": "SOP Orchestrator", "l4": "Digital Handover Bus", "models": "GENAI (LLM) · SOP ANALYSIS"}
}

# --- 4. NAVIGATION & SELECTION ---
st.markdown(f"""
    <div class="nav-header">
        <img src="{logo_url}" width="45" onerror="this.style.display='none'">
        <div style="margin-left:20px;">
            <div style="font-size:20px; font-weight:700; color:#F8FAFC; letter-spacing:-0.5px;">INGERO360AI</div>
            <div style="font-size:9px; color:#38BDF8; font-weight:800; text-transform:uppercase; letter-spacing:2px;">Strategic Horizon Center</div>
        </div>
    </div>
""", unsafe_allow_html=True)

col_p, col_c = st.columns([1, 1])
with col_p:
    p_choice = st.radio("Main Parent Agent (Technology DNA)", PARENT_AGENTS, horizontal=True)
with col_c:
    c_choice = st.radio("Child Agent Strategy (Strategic Intent)", CHILD_AGENTS, horizontal=True)

# --- 5. HORIZONTAL STRATEGIC TREE ---
t_meta = TECH_MAP[p_choice]
i_meta = INIT_MAP[c_choice]

tree_html = f"""
<div class="horizon-container">
    <div class="node-group">
        <div class="node c-common">
            <div class="level-tag">L0 · Orchestrator</div>
            <div class="title">{p_choice} Master Control</div>
            <div class="models">GENAI · MULTI-VARIATE</div>
        </div>
    </div>
    
    <div class="h-line"></div>

    <div class="node-group">
        {" ".join([f'<div class="node c-common"><div class="level-tag">L1 · Sensing</div><div class="title">{a}</div><div class="models">PHYSICS · SOFT SENSORS</div></div>' for a in t_meta['l1']])}
    </div>

    <div class="h-line"></div>

    <div class="node-group">
        {" ".join([f'<div class="node c-common"><div class="level-tag">L2 · Guardrail</div><div class="title">{a}</div><div class="models">BOUNDARY · TRENDING</div></div>' for a in t_meta['l2']])}
    </div>

    <div class="h-line" style="background:rgba(249, 115, 22, 0.4); border: 1px dashed rgba(249, 115, 22, 0.3);"></div>

    <div class="node-group">
        <div class="node c-uncommon">
            <div class="level-tag">L3 · Strategic Brain</div>
            <div class="title">{i_meta['l3']}</div>
            <div class="models">{i_meta['models']}</div>
        </div>
    </div>

    <div class="h-line" style="background:rgba(16, 185, 129, 0.4);"></div>

    <div class="node-group">
        <div class="node c-result">
            <div class="level-tag">L4 · Outcome</div>
            <div class="title">{i_meta['l4']}</div>
            <div class="models">FORECASTING · GENAI</div>
        </div>
    </div>
</div>
"""

st.divider()
components.html(tree_html, height=450, scrolling=True)

# --- 6. LEGEND & ROI INSIGHT ---
st.markdown(f"""
<div style="background: rgba(30, 41, 59, 0.5); padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
    <div style="display:flex; gap:30px; align-items:center;">
        <div style="font-size:12px; color:#94A3B8;">
            <span style="color:#475569; font-weight:800;">■ FOUNDATIONAL DNA (COMMON):</span> L0-L2 agents provide the high-fidelity physics foundation for {p_choice}.
        </div>
        <div style="font-size:12px; color:#94A3B8;">
            <span style="color:#F97316; font-weight:800;">■ STRATEGIC INTELLIGENCE (UNCOMMON):</span> L3-L4 agents are the <b>Difference Makers</b> hot-swapped for <b>{c_choice}</b>.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
