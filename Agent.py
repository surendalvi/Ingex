import streamlit as st
import streamlit.components.v1 as components

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Ingenero360AI Agent Explorer", 
    page_icon="🕸️", 
    layout="wide"
)

# --- 2. PREMIUM CSS: TILES & HIGHLIGHTING ---
st.markdown("""
<style>
    .main .block-container { padding: 1.5rem 3rem !important; background-color: #F8FAFC; }
    
    /* TILE SYSTEM */
    .stButton > button {
        width: 100%; border-radius: 12px; height: 100px;
        border: 1px solid #E2E8F0; background-color: white;
        transition: all 0.3s ease; font-weight: 800; color: #0F172A;
    }
    .stButton > button:hover {
        border-color: #0F172A; transform: translateY(-3px);
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    }
    
    /* HIGHLIGHT SELECTED TILE */
    div[data-testid="stHorizontalBlock"] div.selected-tile button {
        background-color: #0F172A !important;
        color: white !important;
        border-color: #0F172A !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2) !important;
    }

    /* TREE CSS (L0-L4 Hierarchy) */
    :root {
        --orch-bg: #F1F5F9; --orch-border: #94A3B8; --orch-text: #1E293B;
        --l1-bg: #FFFFFF; --l1-border: #CBD5E1; --l1-text: #334155;
        --l2-bg: #FFFFFF; --l2-border: #CBD5E1; --l2-text: #334155;
        
        /* UNCOMMON AGENT HIGHLIGHTING (Initiative Specific) */
        --highlight-bg: #EEEDFE; --highlight-border: #7F77DD; --highlight-text: #26215C;
        --result-bg: #EAF3DE; --result-border: #639922; --result-text: #1E3106;
    }
    .mas-tree { font-family: 'Inter', sans-serif; display: flex; flex-direction: column; align-items: center; padding: 20px; }
    .node {
        padding: 14px 20px; border-radius: 10px; border: 2.5px solid;
        text-align: center; width: 280px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin: 5px;
    }
    .node .title { font-size: 14px; font-weight: 800; margin-bottom: 4px; }
    .node .desc { font-size: 11px; line-height: 1.4; opacity: 0.8; }
    .node .tag { font-size: 9px; font-weight: 900; letter-spacing: 1px; margin-top: 5px; text-transform: uppercase; }

    /* Common Technology Nodes */
    .c-tech { background: var(--l1-bg); border-color: var(--l1-border); color: var(--l1-text); }
    
    /* Uncommon Initiative Nodes (Highlighted) */
    .c-uncommon { 
        background: var(--highlight-bg); border-color: var(--highlight-border); color: var(--highlight-text);
        box-shadow: 0 0 15px rgba(127, 119, 221, 0.3);
    }
    .c-result { 
        background: var(--result-bg); border-color: var(--result-border); color: var(--result-text);
        box-shadow: 0 0 15px rgba(99, 153, 34, 0.2);
    }

    .connector { height: 25px; width: 2px; background: #CBD5E1; }
    .level-row { display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; width: 100%; margin: 5px 0; }
</style>
""", unsafe_allow_html=True)

# --- 3. AGENT REPOSITORY ---
PARENT_AGENTS = [
    "🏭 Olefins", "💧 Methanol", "🌬️ Ammonia", "🧬 EO/EG", "⚗️ MTBE", 
    "🧪 Polymers", "💎 Phenols", "⛽ Refining", "❄️ ASU", "🔧 Utilities"
]

CHILD_AGENTS = [
    "📈 Production Efficiency", "⚡ Energy Optimization", "🛠️ Reliability", 
    "🌱 Sustainability Hub", "🔄 Workflows"
]

TECH_DATA = {
    "🏭 Olefins": {"l1": ["Furnace Kinetic Agent", "CGC Efficiency Agent", "Quench TLE Agent"], "l2": ["TMT Safety Bounds", "Pass Flow Limits"]},
    "💧 Methanol": {"l1": ["SMR Slip Agent", "SynGas Ratio Agent", "Methanol Purity Agent"], "l2": ["S/C Ratio Guardrail", "Catalyst ΔP"]},
    "🌬️ Ammonia": {"l1": ["N2/H2 Balancer Agent", "Shift Conv. Agent", "SynLoop Purge Agent"], "l2": ["Converter Temp Profile", "SynGas Purity Bounds"]},
    "🧬 EO/EG": {"l1": ["Selectivity Agent", "Glycol Ratio Agent", "EO Reactor Agent"], "l2": ["Vapor Concentration Guard", "Catalyst Activity"]},
    "⚗️ MTBE": {"l1": ["Etherification Agent", "Methanol Recovery Agent", "Heat Balance Agent"], "l2": ["Methanol/C4 Ratio", "Isomerization Limits"]},
    "🧪 Polymers": {"l1": ["Reaction Rate Agent", "Grade Transition Agent", "Extruder Torque Agent"], "l2": ["Melt Index Bounds", "Reactor Pressure"]},
    "💎 Phenols": {"l1": ["Oxidation Agent", "Cleavage Yield Agent", "Fractionation Agent"], "l2": ["Peroxide Safety Limits", "Tar Formation Control"]},
    "⛽ Refining": {"l1": ["Fractionation Agent", "Pre-heat Train Agent", "Coker Cycle Agent"], "l2": ["D86 Product Specs", "Tower Hydraulic Limits"]},
    "❄️ ASU": {"l1": ["Cryogenic Sep. Agent", "MAC Compression Agent", "PPU Health Agent"], "l2": ["Oxygen Purity Target", "Expander Delta-T"]},
    "🔧 Utilities": {"l1": ["Steam Header Agent", "Boiler Firing Agent", "Flare Leak Agent"], "l2": ["HP/LP Balance", "Emission Compliance Bounds"]}
}

INIT_DATA = {
    "📈 Production Efficiency": {"l3": "Yield Optimizer Agent", "l4": "Throughput Advisory Bus"},
    "⚡ Energy Optimization": {"l3": "SEC Optimizer Agent", "l4": "Energy Intensity Bus"},
    "🛠️ Reliability": {"l3": "RUL Optimizer Agent", "l4": "Maintenance Advisory Bus"},
    "🌱 Sustainability Hub": {"l3": "Carbon Optimizer Agent", "l4": "ESG Compliance Bus"},
    "🔄 Workflows": {"l3": "SOP Orchestrator Agent", "l4": "Digital Handover Bus"}
}

# --- 4. SESSION STATE FOR INTERACTIVITY ---
if 'selected_parent' not in st.session_state:
    st.session_state.selected_parent = "🏭 Olefins"
if 'selected_child' not in st.session_state:
    st.session_state.selected_child = "📈 Production Efficiency"

# --- 5. PARENT TILES (TECHNOLOGY) ---
st.markdown("### 1. Select Parent Agent (Technology Domain)")
cols = st.columns(5)
for i, tech in enumerate(PARENT_AGENTS):
    with cols[i % 5]:
        is_selected = "selected-tile" if st.session_state.selected_parent == tech else ""
        st.markdown(f'<div class="{is_selected}">', unsafe_allow_html=True)
        if st.button(tech, key=f"p_{tech}"):
            st.session_state.selected_parent = tech
        st.markdown('</div>', unsafe_allow_html=True)

# --- 6. CHILD TILES (INITIATIVE) ---
st.divider()
st.markdown(f"### 2. Select Child Agent (Strategic Initiative) for {st.session_state.selected_parent}")
cols_child = st.columns(5)
for i, init in enumerate(CHILD_AGENTS):
    with cols_child[i]:
        is_selected = "selected-tile" if st.session_state.selected_child == init else ""
        st.markdown(f'<div class="{is_selected}">', unsafe_allow_html=True)
        if st.button(init, key=f"c_{init}"):
            st.session_state.selected_child = init
        st.markdown('</div>', unsafe_allow_html=True)

# --- 7. THE MAS TREE (UNCOMMON HIGHLIGHTING) ---
st.divider()
tech_meta = TECH_DATA[st.session_state.selected_parent]
init_meta = INIT_DATA[st.session_state.selected_child]

tree_html = f"""
<div class="mas-tree">
    <div class="node c-tech" style="background:#F8FAFC;">
        <div class="title">{st.session_state.selected_parent} Master Orchestrator</div>
        <div class="desc">Parent Agent: Fleet coordination</div>
        <div class="tag" style="color:#94A3B8;">Level 0</div>
    </div>
    <div class="connector"></div>
    
    <p style="font-size:10px; color:#94A3B8; font-weight:800; margin:0;">COMMON TECHNOLOGY INFRASTRUCTURE</p>
    
    <div class="level-row">
        {" ".join([f'<div class="node c-tech"><div class="title">{a}</div><div class="desc">Domain Physics</div><div class="tag">L1</div></div>' for a in tech_meta['l1']])}
    </div>
    <div class="connector"></div>

    <div class="level-row">
        {" ".join([f'<div class="node c-tech"><div class="title">{a}</div><div class="desc">Guardrail</div><div class="tag">L2</div></div>' for a in tech_meta['l2']])}
    </div>
    <div class="connector"></div>

    <p style="font-size:10px; color:#7F77DD; font-weight:900; margin:0;">UNCOMMON INITIATIVE-SPECIFIC AGENTS</p>

    <div class="node c-uncommon">
        <div class="title">{init_meta['l3']}</div>
        <div class="desc">Solving for {st.session_state.selected_child} objectives</div>
        <div class="tag" style="color:#26215C;">Level 3 · Difference Maker</div>
    </div>
    <div class="connector"></div>

    <div class="node c-result">
        <div class="title">{init_meta['l4']}</div>
        <div class="desc">Strategic Advisory Output</div>
        <div class="tag" style="color:#1E3106;">Level 4 · Outcome</div>
    </div>
</div>
"""

components.html(tree_html, height=850, scrolling=True)

# --- 8. COMPARISON FOOTER ---
st.info(f"**Visual Intelligence:** The L1 and L2 agents (White) are common to {st.session_state.selected_parent}. The L3 and L4 agents (Purple/Green) are the **uncommon components** that change specifically when you switch to **{st.session_state.selected_child}**.")
