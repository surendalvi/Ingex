import streamlit as st
import streamlit.components.v1 as components

# --- 1. CONFIGURATION & BRANDING ---
st.set_page_config(
    page_title="Ingenero360AI | Agent Strategy", 
    page_icon="🌳", 
    layout="wide"
)

# logo_url fallback
logo_url = "https://raw.githubusercontent.com/surendalvi/Ingex/main/logo.png"

# --- 2. CSS ARCHITECTURE (HIGH-FIDELITY TREE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=JetBrains+Mono:wght@500&display=swap');
    
    .main .block-container { padding: 1.5rem 3rem !important; background-color: #0B0F19; font-family: 'Outfit', sans-serif; color: #E2E8F0; }
    
    /* SELECTION DIAL (PARENT AGENTS) */
    .stButton > button {
        border-radius: 12px; border: 1px solid rgba(255,255,255,0.08);
        background: rgba(30, 41, 59, 0.4); color: #94A3B8;
        font-weight: 600; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        height: 50px; width: 100%; font-size: 14px;
    }
    .stButton > button:hover { border-color: #6366F1; color: white; background: rgba(99, 102, 241, 0.1); }
    
    /* ACTIVE SELECTION HIGHLIGHTS */
    div[data-testid="stHorizontalBlock"] .active-parent button {
        background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%) !important;
        color: white !important; box-shadow: 0 0 25px rgba(79, 70, 229, 0.4) !important;
        border: none !important;
    }
    div.selected-child button {
        background: rgba(16, 185, 129, 0.1) !important;
        border: 2px solid #10B981 !important; color: #10B981 !important;
    }

    /* THE TREE DIAGRAM (CSS DAG) */
    .tree-wrapper { display: flex; flex-direction: column; align-items: center; padding: 40px 0; }
    .agent-node {
        padding: 20px 25px; border-radius: 14px; border: 1.5px solid;
        text-align: center; width: 320px; margin: 8px; position: relative;
        background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(8px);
    }
    .agent-node .title { font-family: 'JetBrains Mono', monospace; font-size: 15px; font-weight: 800; margin-bottom: 6px; letter-spacing: -0.5px; }
    .agent-node .sub { font-size: 11px; color: #94A3B8; line-height: 1.5; font-weight: 400; }
    
    /* Level Tags */
    .level-tag { 
        position: absolute; top: -10px; right: 10px; padding: 2px 8px; 
        border-radius: 20px; font-size: 9px; font-weight: 900; 
        background: #1E293B; border: 1px solid rgba(255,255,255,0.1); 
    }

    /* NODE CATEGORIES */
    .c-parent   { border-color: #6366F1; color: #EEF2FF; } /* L0 Master */
    .c-common   { border-color: #475569; color: #F1F5F9; } /* L1-L2 Foundation */
    .c-uncommon { border-color: #F59E0B; color: #FFFBEB; box-shadow: 0 0 30px rgba(245, 158, 11, 0.15); } /* L3 Optimizer */
    .c-result   { border-color: #10B981; color: #ECFDF5; box-shadow: 0 0 30px rgba(16, 185, 129, 0.15); } /* L4 Decision */

    .line-v { height: 35px; width: 2px; background: linear-gradient(to bottom, rgba(255,255,255,0.2), rgba(255,255,255,0.05)); }
    .level-row { display: flex; justify-content: center; gap: 30px; flex-wrap: wrap; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

# --- 3. DATA REPOSITORY ---
PARENT_AGENTS = ["Olefins", "Methanol", "Ammonia", "EO/EG", "MTBE", "Polymers", "Phenols", "Refining", "ASU", "Utilities"]
CHILD_AGENTS = ["Production Efficiency", "Energy Optimization", "Reliability", "Sustainability Hub", "Workflows"]

AGENT_TECH_MAP = {
    "Olefins": {"l1": ["Furnace Kinetic Agent", "CGC Efficiency Agent", "Quench TLE Agent"], "l2": ["TMT Metallurgy Safety", "Pass Flow Balance Monitoring"]},
    "Methanol": {"l1": ["SMR Kinetic Agent", "SynGas Ratio Agent", "Methanol Purity Agent"], "l2": ["S/C Ratio Guardrail", "Catalyst ΔP Limit Analytics"]},
    "Ammonia": {"l1": ["N2/H2 Balancer Agent", "Shift Conv. Efficiency", "SynLoop Purge Agent"], "l2": ["Converter Temp Mapping", "Inert Concentration Bounds"]},
    "EO/EG": {"l1": ["Selectivity Agent", "Glycol Ratio Agent", "Reactor Heat Flux Agent"], "l2": ["Vapor Concentration Guard", "Catalyst Activity Tracking"]},
    "MTBE": {"l1": ["Etherification Agent", "Methanol Recovery Agent", "Heat Balance Agent"], "l2": ["Methanol/C4 Ratio Control", "Isomerization Limit Monitor"]},
    "Polymers": {"l1": ["Reaction Rate Agent", "Grade Transition Logic", "Extruder Torque Monitor"], "l2": ["Melt Index Consistency", "Reactor Pressure Guard"]},
    "Phenols": {"l1": ["Oxidation Rate Agent", "Cleavage Yield Agent", "Fractionation Precision"], "l2": ["Peroxide Safety Protocol", "Tar Formation Analytics"]},
    "Refining": {"l1": ["Fractionation Agent", "Pre-heat Train Agent", "Coker Cycle Agent"], "l2": ["ASTM Product Specs", "Tower Hydraulic Loading"]},
    "ASU": {"l1": ["Cryogenic Separation", "MAC Compression Health", "PPU Efficiency Agent"], "l2": ["O2/N2 Purity Target", "Expander Thermal Profile"]},
    "Utilities": {"l1": ["Steam Header Agent", "Boiler Firing Logic", "Flare Leak Detection"], "l2": ["HP/MP/LP Balance", "Emission Ceiling Monitoring"]}
}

AGENT_INIT_MAP = {
    "Production Efficiency": {"l3": "Yield Maximization Optimizer", "l4": "Throughput Advisory Dashboard"},
    "Energy Optimization": {"l3": "Specific Energy (SEC) Optimizer", "l4": "Energy Intensity Result Bus"},
    "Reliability": {"l3": "Asset Health & RUL Optimizer", "l4": "Maintenance Advisory Hub"},
    "Sustainability Hub": {"l3": "Carbon Intensity Optimizer", "l4": "ESG Compliance Dashboard"},
    "Workflows": {"l3": "SOP Compliance Orchestrator", "l4": "Digital Handover Result Bus"}
}

# --- 4. SELECTION LOGIC ---
if 'parent' not in st.session_state: st.session_state.parent = "Olefins"
if 'child' not in st.session_state: st.session_state.child = "Production Efficiency"

# Header
st.markdown(f"""
    <div style="display:flex; align-items:center; margin-bottom:30px;">
        <img src="{logo_url}" width="48">
        <div style="margin-left:20px;">
            <div style="font-size:24px; font-weight:800; letter-spacing:-0.5px; color:#F1F5F9;">INGERO360AI</div>
            <div style="font-size:10px; color:#6366F1; font-weight:700; text-transform:uppercase; letter-spacing:2.5px;">Strategic Agent Architecture</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Selection Dial
st.markdown("<p style='font-size:11px; font-weight:800; color:#475569; text-transform:uppercase; margin-left:5px;'>Parent Technology selection</p>", unsafe_allow_html=True)
p_cols = st.columns(len(PARENT_AGENTS))
for i, tech in enumerate(PARENT_AGENTS):
    with p_cols[i]:
        active_class = "active-parent" if st.session_state.parent == tech else ""
        st.markdown(f'<div class="{active_class}">', unsafe_allow_html=True)
        if st.button(tech, key=f"p_{tech}"):
            st.session_state.parent = tech
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# Initiative Tiles
st.markdown("<p style='font-size:11px; font-weight:800; color:#475569; text-transform:uppercase; margin: 30px 0 10px 5px;'>Strategic Initiative Mapping</p>", unsafe_allow_html=True)
c_cols = st.columns(len(CHILD_AGENTS))
for i, init in enumerate(CHILD_AGENTS):
    with c_cols[i]:
        selected_class = "selected-child" if st.session_state.child == init else ""
        st.markdown(f'<div class="{selected_class}">', unsafe_allow_html=True)
        if st.button(init, key=f"c_{init}"):
            st.session_state.child = init
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. RENDER AGENT TREE ---
st.divider()
t_data = AGENT_TECH_MAP[st.session_state.parent]
i_data = AGENT_INIT_MAP[st.session_state.child]

tree_html = f"""
<div class="tree-wrapper">
    <div class="agent-node c-parent">
        <div class="level-tag">L0</div>
        <div class="title">{st.session_state.parent} Orchestrator</div>
        <div class="sub">Master Solution Governance · Agent Synchronization</div>
    </div>
    <div class="line-v"></div>
    
    <p style="font-size:10px; color:#475569; font-weight:800; margin:5px 0;">FOUNDATIONAL TECHNOLOGY AGENTS (COMMON)</p>
    <div class="level-row">
        {" ".join([f'<div class="agent-node c-common"><div class="level-tag">L1</div><div class="title">{a}</div><div class="sub">High-Fidelity Physics & Sensor Ingestion</div></div>' for a in t_data['l1']])}
    </div>
    <div class="line-v"></div>

    <div class="level-row">
        {" ".join([f'<div class="agent-node c-common"><div class="level-tag">L2</div><div class="title">{a}</div><div class="sub">Safety Guardrail & Constraint Management</div></div>' for a in t_data['l2']])}
    </div>
    <div class="line-v"></div>

    <p style="font-size:10px; color:#F59E0B; font-weight:800; margin:5px 0;">STRATEGIC INTENT AGENT (UNCOMMON)</p>
    <div class="agent-node c-uncommon">
        <div class="level-tag" style="background:#F59E0B; color:#1E1B4B;">L3</div>
        <div class="title">{i_data['l3']}</div>
        <div class="sub">Objective-Specific Optimization Engine for {st.session_state.child}</div>
    </div>
    <div class="line-v"></div>

    <div class="agent-node c-result">
        <div class="level-tag" style="background:#10B981; color:#064E3B;">L4</div>
        <div class="title">{i_data['l4']}</div>
        <div class="sub">Final Strategic Output · Real-time Operating Advisory</div>
    </div>
</div>
"""

components.html(tree_html, height=880, scrolling=False)

# --- 6. ARCHITECTURE LOGIC FOOTER ---
with st.expander("🔍 Strategic Architecture Insights"):
    st.markdown(f"""
    The **{st.session_state.parent}** solution architecture is built on a "Common DNA" framework. 
    The L1 and L2 agents represent the **Common Infrastructure** that stays constant for this technology domain.
    When you transition between initiatives, the **Uncommon Agents** (L3 and L4) are hot-swapped by the Master Orchestrator to pivot the AI's objective from, for example, *Reliability* to *Sustainability*.
    """)
