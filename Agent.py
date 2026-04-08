import streamlit as st
import streamlit.components.v1 as components

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Ingenero360AI Command Hub", 
    page_icon="🔘", 
    layout="wide"
)

# --- 2. THE PRECISION UI ENGINE (CSS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    .main .block-container { padding: 1.5rem 3rem !important; background-color: #F8FAFC; font-family: 'Inter', sans-serif; }
    
    /* THE SELECTION DIAL (Parent Agents) */
    .dial-container {
        display: flex; background: #E2E8F0; border-radius: 50px;
        padding: 5px; margin-bottom: 25px; border: 1px solid #CBD5E1;
        box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.05);
    }
    .dial-item {
        flex: 1; text-align: center; padding: 12px 10px;
        cursor: pointer; font-size: 13px; font-weight: 700;
        color: #64748B; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border-radius: 40px; white-space: nowrap;
    }
    .dial-item.active {
        background: #0F172A; color: white;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.3);
    }

    /* INITIATIVE TILES (Child Agents) */
    .child-grid {
        display: grid; grid-template-columns: repeat(5, 1fr); gap: 15px; margin-bottom: 30px;
    }
    .child-tile {
        background: white; border: 1px solid #E2E8F0; border-radius: 12px;
        padding: 15px; text-align: center; cursor: pointer;
        transition: all 0.2s ease;
    }
    .child-tile:hover { transform: translateY(-3px); border-color: #0F172A; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); }
    .child-tile.active { border: 2px solid #0F172A; background: #F1F5F9; }
    .child-title { font-size: 14px; font-weight: 800; color: #1E293B; }

    /* MAS TREE ARCHITECTURE */
    :root {
        --orch-bg: #F8FAFC; --orch-border: #0F172A; --orch-text: #0F172A;
        --tech-bg: #FFFFFF; --tech-border: #E2E8F0; --tech-text: #475569;
        --highlight-bg: #EEEDFE; --highlight-border: #7F77DD; --highlight-text: #26215C;
        --result-bg: #EAF3DE; --result-border: #639922; --result-text: #1E3106;
    }
    .mas-tree { display: flex; flex-direction: column; align-items: center; padding: 20px; }
    .node {
        padding: 14px 18px; border-radius: 10px; border: 2px solid;
        text-align: center; width: 260px; box-shadow: 0 2px 4px rgba(0,0,0,0.03);
        margin: 4px;
    }
    .node .title { font-size: 13px; font-weight: 800; margin-bottom: 3px; }
    .node .desc { font-size: 11px; opacity: 0.8; line-height: 1.3; }
    .node .level-tag { font-size: 9px; font-weight: 900; letter-spacing: 0.5px; margin-top: 6px; text-transform: uppercase; }

    .c-orch { background: var(--orch-bg); border-color: var(--orch-border); color: var(--orch-text); }
    .c-tech { background: var(--tech-bg); border-color: var(--tech-border); color: var(--tech-text); }
    .c-uncommon { 
        background: var(--highlight-bg); border-color: var(--highlight-border); color: var(--highlight-text);
        box-shadow: 0 0 20px rgba(127, 119, 221, 0.25);
    }
    .c-result { 
        background: var(--result-bg); border-color: var(--result-border); color: var(--result-text);
        box-shadow: 0 0 20px rgba(99, 153, 34, 0.2);
    }
    .connector { height: 20px; width: 2px; background: #E2E8F0; }
    .level-row { display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; margin: 5px 0; }
</style>
""", unsafe_allow_html=True)

# --- 3. DATA REPOSITORY ---
PARENT_AGENTS = ["Olefins", "Methanol", "Ammonia", "EO/EG", "MTBE", "Polymers", "Phenols", "Refining", "ASU", "Utilities"]

CHILD_AGENTS = ["Production Efficiency", "Energy Optimization", "Reliability", "Sustainability Hub", "Workflows"]

TECH_MAP = {
    "Olefins": {"l1": ["Furnace Kinetic Agent", "CGC Efficiency Agent", "Quench TLE Agent"], "l2": ["TMT Safety Limits", "Pass Flow Balance"]},
    "Methanol": {"l1": ["SMR Slip Agent", "SynGas Ratio Agent", "Methanol Purity Agent"], "l2": ["S/C Ratio Guard", "Catalyst ΔP"]},
    "Ammonia": {"l1": ["N2/H2 Balancer", "Shift Conv. Agent", "SynLoop Purge Agent"], "l2": ["Conv. Temp Profile", "SynGas Purity"]},
    "EO/EG": {"l1": ["Selectivity Agent", "Glycol Ratio Agent", "EO Reactor Agent"], "l2": ["Vapor Guard", "Catalyst Activity"]},
    "MTBE": {"l1": ["Etherification Agent", "Recovery Agent", "Heat Balance Agent"], "l2": ["Methanol/C4 Ratio", "Isom Limits"]},
    "Polymers": {"l1": ["Reaction Rate Agent", "Grade Transition", "Extruder Torque"], "l2": ["Melt Index Bounds", "Reactor Pressure"]},
    "Phenols": {"l1": ["Oxidation Agent", "Cleavage Yield Agent", "Fractionation Agent"], "l2": ["Peroxide Limits", "Tar Formation Control"]},
    "Refining": {"l1": ["Fractionation Agent", "Pre-heat Train Agent", "Coker Cycle Agent"], "l2": ["D86 Product Specs", "Hydraulic Limits"]},
    "ASU": {"l1": ["Cryogenic Sep. Agent", "MAC Compression", "PPU Health Agent"], "l2": ["O2 Purity Target", "Expander Delta-T"]},
    "Utilities": {"l1": ["Steam Header Agent", "Boiler Firing Agent", "Flare Leak Agent"], "l2": ["HP/LP Balance", "Emission Compliance"]}
}

INIT_MAP = {
    "Production Efficiency": {"l3": "Yield Optimizer Agent", "l4": "Throughput Advisory"},
    "Energy Optimization": {"l3": "SEC Optimizer Agent", "l4": "Energy Intensity Advisory"},
    "Reliability": {"l3": "RUL Optimizer Agent", "l4": "Maintenance Advisory"},
    "Sustainability Hub": {"l3": "Carbon Optimizer Agent", "l4": "ESG Compliance Advisory"},
    "Workflows": {"l3": "SOP Orchestrator Agent", "l4": "Digital Handover Bus"}
}

# --- 4. SESSION STATE ---
if 'tech' not in st.session_state: st.session_state.tech = "Olefins"
if 'init' not in st.session_state: st.session_state.init = "Production Efficiency"

# --- 5. TOP BRANDING ---
st.markdown(f"""
    <div style="display:flex; align-items:center; margin-bottom:20px;">
        <img src="{logo_url}" width="35">
        <div style="margin-left:15px;">
            <div style="font-size:18px; font-weight:800; color:#0F172A; letter-spacing:-0.5px;">INGERO360AI</div>
            <div style="font-size:9px; color:#64748B; font-weight:700; text-transform:uppercase; letter-spacing:1px;">Precision Command Hub</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 6. THE SELECTION DIAL (Parent Agents) ---
st.markdown("<p style='font-size:11px; font-weight:800; color:#94A3B8; text-transform:uppercase; margin-bottom:10px;'>Main Agent Selection Dial</p>", unsafe_allow_html=True)

# Dial implementation via columns and custom class
dial_cols = st.columns(len(PARENT_AGENTS))
for i, tech in enumerate(PARENT_AGENTS):
    with dial_cols[i]:
        active_class = "active" if st.session_state.tech == tech else ""
        if st.button(tech, key=f"d_{tech}", use_container_width=True):
            st.session_state.tech = tech
            st.rerun()

# --- 7. STRATEGY TILES (Child Agents) ---
st.markdown("<p style='font-size:11px; font-weight:800; color:#94A3B8; text-transform:uppercase; margin:20px 0 10px 0;'>Strategic Initiative (Child Agents)</p>", unsafe_allow_html=True)
init_cols = st.columns(len(CHILD_AGENTS))
for i, init in enumerate(CHILD_AGENTS):
    with init_cols[i]:
        # Using a distinct visual style for selected child
        is_selected = st.session_state.init == init
        label = f"✓ {init}" if is_selected else init
        if st.button(label, key=f"c_{init}", use_container_width=True):
            st.session_state.init = init
            st.rerun()

# --- 8. MAS TREE VISUALIZATION ---
st.divider()
t_data = TECH_MAP[st.session_state.tech]
i_data = INIT_MAP[st.session_state.init]

tree_html = f"""
<div class="mas-tree">
    <div class="node c-orch">
        <div class="title">{st.session_state.tech} Orchestrator</div>
        <div class="desc">Parent Agent: Domain Coordination</div>
        <div class="level-tag">L0</div>
    </div>
    <div class="connector"></div>
    
    <div class="level-row">
        {" ".join([f'<div class="node c-tech"><div class="title">{a}</div><div class="desc">Common Tech Logic</div><div class="level-tag">L1</div></div>' for a in t_data['l1']])}
    </div>
    <div class="connector"></div>

    <div class="level-row">
        {" ".join([f'<div class="node c-tech"><div class="title">{a}</div><div class="desc">Safety Guardrail</div><div class="level-tag">L2</div></div>' for a in t_data['l2']])}
    </div>
    <div class="connector"></div>

    <div class="node c-uncommon">
        <div class="title">{i_data['l3']}</div>
        <div class="desc">Uncommon: {st.session_state.init} Optimization</div>
        <div class="level-tag" style="color:#7F77DD;">L3 · Solution Brain</div>
    </div>
    <div class="connector"></div>

    <div class="node c-result">
        <div class="title">{i_data['l4']}</div>
        <div class="desc">Strategic Results Interface</div>
        <div class="level-tag" style="color:#639922;">L4 · Advisory Bus</div>
    </div>
</div>
"""

components.html(tree_html, height=750, scrolling=False)

# --- 9. FOOTER ---
st.markdown(f"""
<div style="background: white; padding: 15px; border-radius: 12px; border: 1px solid #E2E8F0; margin-top: 20px;">
    <p style="font-size:12px; color:#475569; margin:0;">
        <b>Intelligence Architecture:</b> The L0-L2 nodes represent the <b>Common Infrastructure</b> of {st.session_state.tech}. 
        The highlighted L3-L4 nodes represent the <b>Uncommon Intelligence</b> unique to the {st.session_state.init} initiative.
    </p>
</div>
""", unsafe_allow_html=True)
