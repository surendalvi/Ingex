import streamlit as st
import streamlit.components.v1 as components

# --- 1. PAGE CONFIG & BRANDING ---
st.set_page_config(
    page_title="Ingenero360AI | Strategic Hub", 
    page_icon="🖥️", 
    layout="wide"
)

# logo_url setup with safety fallback
logo_url = "https://raw.githubusercontent.com/surendalvi/Ingex/main/logo.png"

# --- 2. THE INGENERO PRO THEME (CLEAN CSS) ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@500&display=swap');
    
    /* Background & Global Font */
    .main .block-container {{ padding: 1.5rem 3rem !important; background-color: #0F172A; font-family: 'Inter', sans-serif; color: white; }}
    
    /* CLEAN HEADER */
    .nav-header {{
        display: flex; align-items: center; padding: 20px; 
        background: rgba(30, 41, 59, 0.4); border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 30px; border-radius: 12px;
    }}

    /* RADIO BUTTON OVERRIDES (Segmented Control Look) */
    .stRadio > label {{ font-size: 12px !important; font-weight: 700 !important; color: #94A3B8 !important; text-transform: uppercase; margin-bottom: 10px; }}
    div[data-testid="stHorizontalBlock"] .stRadio div[role="radiogroup"] {{
        display: flex; flex-direction: row; gap: 10px;
    }}
    
    /* THE TREE DIAGRAM (Clean & Modern) */
    .tree-container {{ display: flex; flex-direction: column; align-items: center; padding: 40px; }}
    .node {{
        padding: 20px 25px; border-radius: 12px; border: 1px solid;
        text-align: center; width: 340px; margin: 10px; position: relative;
        background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(10px);
    }}
    .node .level-tag {{ 
        position: absolute; top: -10px; right: 10px; background: #334155; 
        padding: 2px 10px; border-radius: 20px; font-size: 10px; font-weight: 800; 
        border: 1px solid rgba(255,255,255,0.2); color: #F1F5F9;
    }}
    .node .title {{ font-size: 15px; font-weight: 700; margin-bottom: 6px; letter-spacing: -0.5px; }}
    .node .models {{ font-family: 'JetBrains Mono', monospace; font-size: 9px; color: #F97316; font-weight: 600; margin-bottom: 8px; text-transform: uppercase; }}
    .node .desc {{ font-size: 11px; color: #94A3B8; line-height: 1.5; }}
    
    /* Common Tech Nodes (The DNA) */
    .c-common {{ border-color: #475569; color: #F8FAFC; }}
    
    /* UNCOMMON INITIATIVE NODES (The Brain) */
    .c-uncommon {{ 
        border-color: #F97316; color: #FFF7ED;
        box-shadow: 0 0 25px rgba(249, 115, 22, 0.15);
    }}
    .c-result {{ 
        border-color: #10B981; color: #ECFDF5;
        box-shadow: 0 0 25px rgba(16, 185, 129, 0.15);
    }}

    .connector {{ height: 35px; width: 2px; background: rgba(255,255,255,0.1); }}
    .level-row {{ display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; }}
</style>
""", unsafe_allow_html=True)

# --- 3. DATA REPOSITORY ---
PARENT_AGENTS = ["Olefins", "Methanol", "Ammonia", "EO/EG", "MTBE", "Polymers", "Phenols", "Refining", "ASU", "Utilities"]
CHILD_AGENTS = ["Production Efficiency", "Energy Optimization", "Reliability", "Sustainability Hub", "Workflows"]

TECH_LOGIC = {
    "Olefins": {"l1": ["Furnace Kinetic Agent", "CGC Efficiency Agent"], "l2": ["TMT Safety Guardrail", "Pass Flow Balancer"]},
    "Methanol": {"l1": ["SMR Kinetic Agent", "SynGas Ratio Agent"], "l2": ["S/C Ratio Guardrail", "Catalyst Health Monitor"]},
    "Ammonia": {"l1": ["N2/H2 Balancer", "Shift Conversion Agent"], "l2": ["Converter Temp Profile", "SynLoop Purge Limit"]},
    "EO/EG": {"l1": ["Selectivity Agent", "Glycol Ratio Agent"], "l2": ["Vapor Concentration Guard", "Reactor Heat Flux"]},
    "MTBE": {"l1": ["Etherification Agent", "Methanol Recovery"], "l2": ["Reflux Ratio Bounds", "Feed Ratio Guard"]},
    "Polymers": {"l1": ["Reaction Rate Agent", "Grade Transition Logic"], "l2": ["Melt Index Consistency", "Reactor Pressure"]},
    "Phenols": {"l1": ["Oxidation Rate Agent", "Cleavage Yield Agent"], "l2": ["Peroxide Safety Protocol", "Tar Formation Monitor"]},
    "Refining": {"l1": ["Fractionation Agent", "Coker Cycle Agent"], "l2": ["ASTM Product Specs", "Tower Hydraulic Loading"]},
    "ASU": {"l1": ["Cryogenic Separation", "MAC Compression Health"], "l2": ["O2/N2 Purity Target", "Expander Delta-T"]},
    "Utilities": {"l1": ["Steam Header Agent", "Boiler Firing Agent"], "l2": ["HP/LP Steam Balance", "Emission Ceiling Monitor"]}
}

INIT_LOGIC = {
    "Production Efficiency": {"l3": "Yield Maximization Optimizer", "l4": "Throughput Advisory Dashboard", "models": "MINLP · BENCHMARKING · ANALYSIS"},
    "Energy Optimization": {"l3": "Specific Energy (SEC) Optimizer", "l4": "Energy Intensity Advisory", "models": "LP · SEC TRENDING · FORECASTING"},
    "Reliability": {"l3": "Asset Health & RUL Optimizer", "l4": "Maintenance Advisory Hub", "models": "PREDICTIVE RUL · FAILURE MODES · TRENDING"},
    "Sustainability Hub": {"l3": "Carbon Intensity Optimizer", "l4": "ESG Compliance Dashboard", "models": "FORECASTING · FLARE ANALYSIS · EMISSIONS"},
    "Workflows": {"l3": "SOP Compliance Orchestrator", "l4": "Digital Handover Result Bus", "models": "GENAI (LLM) · SOP ANALYSIS · AUDIT"}
}

# --- 4. HEADER & NAVIGATION ---
st.markdown(f"""
    <div class="nav-header">
        <img src="{logo_url}" width="50" onerror="this.style.display='none'">
        <div style="margin-left:20px;">
            <div style="font-size:24px; font-weight:700; color:#F8FAFC;">INGERO360AI</div>
            <div style="font-size:11px; color:#F97316; font-weight:600; text-transform:uppercase; letter-spacing:2px;">Strategic Agent Ecosystem</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# SELECTION ROW
c1, c2 = st.columns([2, 1])
with c1:
    parent_choice = st.radio("Main Parent Agent (Technology DNA)", PARENT_AGENTS, horizontal=True)
with c2:
    child_choice = st.radio("Child Agent Strategy (Strategic Intent)", CHILD_AGENTS, horizontal=True)

# --- 5. THE STRATEGIC AGENT TREE ---
st.divider()
t_meta = TECH_LOGIC[parent_choice]
i_meta = INIT_LOGIC[child_choice]

tree_html = f"""
<div class="tree-container">
    <div class="node c-common" style="border-color:#F8FAFC;">
        <div class="level-tag">L0</div>
        <div class="models">GENAI · MULTI-VARIATE ANALYSIS</div>
        <div class="title">{parent_choice} Master Orchestrator</div>
        <div class="desc">Domain Governance · Real-time Agent Synchronization</div>
    </div>
    <div class="connector"></div>
    
    <div class="level-row">
        {" ".join([f'<div class="node c-common"><div class="level-tag">L1</div><div class="models">PREDICTIVE · SOFT SENSORS</div><div class="title">{a}</div><div class="desc">Common DNA: Physics & Kinetics Engine</div></div>' for a in t_meta['l1']])}
    </div>
    <div class="connector"></div>

    <div class="level-row">
        {" ".join([f'<div class="node c-common"><div class="level-tag">L2</div><div class="models">BOUNDARY ANALYSIS · TRENDING</div><div class="title">{a}</div><div class="desc">Common DNA: Mechanical & Safety Guardrails</div></div>' for a in t_meta['l2']])}
    </div>
    <div class="connector"></div>

    <div class="node c-uncommon">
        <div class="level-tag">L3</div>
        <div class="models">{i_meta['models']}</div>
        <div class="title">{i_meta['l3']}</div>
        <div class="desc">Uncommon Intelligence: {child_choice} Brain</div>
    </div>
    <div class="connector"></div>

    <div class="node c-result">
        <div class="level-tag">L4</div>
        <div class="models">FORECASTING · GENAI ADVISORY</div>
        <div class="title">{i_meta['l4']}</div>
        <div class="desc">Final Result Bus: Actionable Operating Targets</div>
    </div>
</div>
"""

components.html(tree_html, height=900, scrolling=False)

# --- 6. ARCHITECTURE LEGEND ---
st.markdown(f"""
<div style="background: rgba(30, 41, 59, 0.4); padding: 25px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); margin-top: 20px;">
    <p style="font-size:13px; color:#94A3B8; margin:0; line-height:1.6;">
        <b style="color:#F97316;">Strategic Methodology:</b> The Ingenero360AI package uses a Multi-Agent System (MAS) to solve complex industrial problems. 
        The white nodes (L0-L2) represent the <b>Common DNA</b> (Physics & Safety) inherent to the {parent_choice} domain. 
        The orange-highlighted node (L3) is the <b>Uncommon Intelligence</b>—the specific mathematical engine (like MINLP or Predictive RUL) activated for <b>{child_choice}</b>.
    </p>
</div>
""", unsafe_allow_html=True)
