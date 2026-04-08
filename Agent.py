import streamlit as st
import streamlit.components.v1 as components

# --- 1. PAGE CONFIG & BRANDING ---
st.set_page_config(
    page_title="Ingenero360AI | Agent Command", 
    page_icon="🖥️", 
    layout="wide"
)

# logo_url setup with safety fallback
logo_url = "https://raw.githubusercontent.com/surendalvi/Ingex/main/logo.png"

# --- 2. THE EXECUTIVE UI ENGINE (CSS) ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono:wght@500&display=swap');
    
    .main .block-container {{ padding: 1rem 3rem !important; background-color: #0F172A; font-family: 'Inter', sans-serif; color: white; }}
    
    /* GLASSMORPHISM HEADER */
    .glass-header {{
        background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 16px;
        padding: 15px 25px; display: flex; align-items: center; margin-bottom: 25px;
    }}

    /* SELECTION DIAL (Parent Agents) */
    .stButton > button {{
        border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);
        background: rgba(30, 41, 59, 0.5); color: #94A3B8;
        font-weight: 600; transition: all 0.3s ease; height: 45px; width: 100%;
    }}
    .stButton > button:hover {{ border-color: #38BDF8; color: white; background: rgba(56, 189, 248, 0.1); }}
    
    /* Highlight Active Dial Item */
    div[data-testid="stHorizontalBlock"] .active-parent button {{
        background: #38BDF8 !important; color: #0F172A !important;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.4) !important;
        border: none !important;
    }}

    /* CHILD STRATEGY TILES */
    div.selected-child button {{
        background: rgba(129, 140, 248, 0.2) !important;
        border: 2px solid #818CF8 !important; color: white !important;
    }}

    /* MAS TREE ARCHITECTURE */
    .tree-container {{ display: flex; flex-direction: column; align-items: center; padding: 40px; }}
    .node {{
        padding: 18px 25px; border-radius: 12px; border: 1px solid;
        text-align: center; width: 300px; margin: 5px; position: relative;
    }}
    .node .title {{ font-family: 'JetBrains Mono', monospace; font-size: 14px; font-weight: 800; margin-bottom: 5px; text-transform: uppercase; }}
    .node .desc {{ font-size: 11px; color: #94A3B8; line-height: 1.4; }}
    
    /* Common Tech Nodes */
    .c-common {{ background: rgba(30, 41, 59, 0.8); border-color: #475569; color: #F1F5F9; }}
    
    /* UNCOMMON INITIATIVE NODES */
    .c-uncommon {{ 
        background: rgba(129, 140, 248, 0.1); border-color: #818CF8; color: #E0E7FF;
        box-shadow: 0 0 30px rgba(129, 140, 248, 0.2);
    }}
    .c-result {{ 
        background: rgba(52, 211, 153, 0.1); border-color: #34D399; color: #ECFDF5;
        box-shadow: 0 0 30px rgba(52, 211, 153, 0.2);
    }}

    .connector {{ height: 30px; width: 2px; background: rgba(255,255,255,0.1); }}
    .level-row {{ display: flex; justify-content: center; gap: 25px; flex-wrap: wrap; margin: 10px 0; }}
</style>
""", unsafe_allow_html=True)

# --- 3. DATA REPOSITORY ---
PARENT_AGENTS = ["Olefins", "Methanol", "Ammonia", "EO/EG", "MTBE", "Polymers", "Phenols", "Refining", "ASU", "Utilities"]
CHILD_AGENTS = ["Production Efficiency", "Energy Optimization", "Reliability", "Sustainability Hub", "Workflows"]

TECH_LOGIC = {
    "Olefins": {"l1": ["Furnace Kinetic Agent", "CGC Efficiency Agent", "Quench TLE Agent"], "l2": ["TMT Safety Limits", "Pass Flow Balance"]},
    "Methanol": {"l1": ["SMR Kinetic Agent", "SynGas Ratio Agent", "Product Purity Agent"], "l2": ["S/C Ratio Guard", "Catalyst ΔP Limit"]},
    "Ammonia": {"l1": ["N2/H2 Balancer", "Shift Conv. Agent", "SynLoop Purge Agent"], "l2": ["Conv. Temp Profile", "Inert Conc. Bounds"]},
    "EO/EG": {"l1": ["Selectivity Agent", "Glycol Ratio Agent", "Reactor Heat Agent"], "l2": ["Vapor Concentration", "Catalyst Activity"]},
    "MTBE": {"l1": ["Etherification Agent", "Methanol Recovery", "Isom Health Agent"], "l2": ["Reflux Ratio Bounds", "Methanol/C4 Bal"]},
    "Polymers": {"l1": ["Reaction Rate Agent", "Grade Transition", "Extruder Torque"], "l2": ["Melt Index Control", "Reactor Pressure"]},
    "Phenols": {"l1": ["Oxidation Agent", "Cleavage Yield Agent", "Fractionation Agent"], "l2": ["Peroxide Safety", "Tar Formation Control"]},
    "Refining": {"l1": ["Fractionation Agent", "Pre-heat Train Agent", "Coker Cycle Agent"], "l2": ["ASTM D86 Specs", "Tower Loading Limits"]},
    "ASU": {"l1": ["Cryogenic Sep. Agent", "MAC Compression", "PPU Health Agent"], "l2": ["O2 Purity Target", "Expander Delta-T"]},
    "Utilities": {"l1": ["Steam Header Agent", "Boiler Firing Agent", "Flare Leak Agent"], "l2": ["HP/LP Balance", "Fuel Gas CV Monitor"]}
}

INIT_LOGIC = {
    "Production Efficiency": {"l3": "Yield Optimizer Agent", "l4": "Throughput Advisory Bus"},
    "Energy Optimization": {"l3": "SEC Optimizer Agent", "l4": "Energy Intensity Bus"},
    "Reliability": {"l3": "RUL Optimizer Agent", "l4": "Predictive Maintenance Bus"},
    "Sustainability Hub": {"l3": "Carbon Optimizer Agent", "l4": "ESG Compliance Bus"},
    "Workflows": {"l3": "SOP Orchestrator Agent", "l4": "Digital Handover Bus"}
}

# --- 4. SESSION STATE & TOP BRANDING ---
if 'parent' not in st.session_state: st.session_state.parent = "Olefins"
if 'child' not in st.session_state: st.session_state.child = "Production Efficiency"

st.markdown(f"""
    <div class="glass-header">
        <img src="{logo_url}" width="45">
        <div style="margin-left:20px;">
            <div style="font-size:22px; font-weight:800; letter-spacing:-0.5px; color:#F1F5F9;">INGERO360AI</div>
            <div style="font-size:10px; color:#38BDF8; font-weight:700; text-transform:uppercase; letter-spacing:2px;">Digital Twin Agent Matrix</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 5. SELECTION DIAL (Parent Agents) ---
st.markdown("<p style='font-size:11px; font-weight:800; color:#64748B; text-transform:uppercase; margin-left:5px;'>Parent Technology Dial</p>", unsafe_allow_html=True)
p_cols = st.columns(len(PARENT_AGENTS))
for i, tech in enumerate(PARENT_AGENTS):
    with p_cols[i]:
        active_style = "active-parent" if st.session_state.parent == tech else ""
        st.markdown(f'<div class="{active_style}">', unsafe_allow_html=True)
        if st.button(tech, key=f"p_{tech}"):
            st.session_state.parent = tech
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- 6. STRATEGY TILES (Child Agents) ---
st.markdown("<p style='font-size:11px; font-weight:800; color:#64748B; text-transform:uppercase; margin: 25px 0 10px 5px;'>Strategic Initiative Tiles</p>", unsafe_allow_html=True)
c_cols = st.columns(len(CHILD_AGENTS))
for i, init in enumerate(CHILD_AGENTS):
    with c_cols[i]:
        selected_style = "selected-child" if st.session_state.child == init else ""
        st.markdown(f'<div class="{selected_style}">', unsafe_allow_html=True)
        if st.button(init, key=f"c_{init}"):
            st.session_state.child = init
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- 7. THE AGENT TREE (MAS VISUALIZATION) ---
st.divider()
t_meta = TECH_LOGIC[st.session_state.parent]
i_meta = INIT_LOGIC[st.session_state.child]

tree_html = f"""
<div class="tree-container">
    <div class="node c-common" style="border-color:#F1F5F9;">
        <div class="title">{st.session_state.parent} Orchestrator</div>
        <div class="desc">L0 Parent Agent: Enterprise Governance</div>
    </div>
    <div class="connector"></div>
    
    <div class="level-row">
        {" ".join([f'<div class="node c-common"><div class="title">{a}</div><div class="desc">Common Tech Logic (L1)</div></div>' for a in t_meta['l1']])}
    </div>
    <div class="connector"></div>

    <div class="level-row">
        {" ".join([f'<div class="node c-common"><div class="title">{a}</div><div class="desc">Safety Guardrail (L2)</div></div>' for a in t_meta['l2']])}
    </div>
    <div class="connector"></div>

    <div class="node c-uncommon">
        <div class="title">{i_meta['l3']}</div>
        <div class="desc">Uncommon: {st.session_state.child} Brain (L3)</div>
    </div>
    <div class="connector"></div>

    <div class="node c-result">
        <div class="title">{i_meta['l4']}</div>
        <div class="desc">Decision Support Result Bus (L4)</div>
    </div>
</div>
"""

components.html(tree_html, height=850, scrolling=False)

# --- 8. FOOTER ANALYSIS ---
st.markdown(f"""
<div style="background: rgba(30, 41, 59, 0.5); padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); margin-top: 20px;">
    <p style="font-size:13px; color:#94A3B8; margin:0;">
        <b style="color:#38BDF8;">Architecture Insight:</b> You are currently viewing the Multi-Agent System for <b>{st.session_state.parent}</b>. 
        The grey/dark nodes represent the <b>Common Structural DNA</b> shared by all solutions in this technology. 
        The highlighted Blue and Green nodes represent the <b>Uncommon Intelligence Agents</b> specifically deployed for <b>{st.session_state.child}</b>.
    </p>
</div>
""", unsafe_allow_html=True)
