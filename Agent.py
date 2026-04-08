import streamlit as st
import streamlit.components.v1 as components

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Ingenero360AI Agent Explorer", 
    page_icon="🕸️", 
    layout="wide"
)

# --- 2. CSS FOR TILES AND TREE DIAGRAM ---
st.markdown("""
<style>
    .main .block-container { padding: 1.5rem 3rem !important; background-color: #F8FAFC; }
    
    /* TILE STYLING */
    .tech-tile {
        padding: 20px; border-radius: 12px; background: white;
        border: 1px solid #E2E8F0; text-align: center;
        transition: all 0.3s ease; cursor: pointer; height: 120px;
        display: flex; flex-direction: column; justify-content: center;
    }
    .tech-tile:hover {
        border-color: #0F172A; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    .tech-title { font-size: 16px; font-weight: 800; color: #0F172A; }
    .tech-icon { font-size: 24px; margin-bottom: 8px; }

    /* TREE CSS (L0-L4 Hierarchy) */
    :root {
        --orch-bg: #EEEDFE; --orch-border: #7F77DD; --orch-text: #26215C;
        --l1-bg: #E6F1FB; --l1-border: #378ADD; --l1-text: #042C53;
        --l2-bg: #FAECE7; --l2-border: #D85A30; --l2-text: #5D2412;
        --l3-bg: #EAF3DE; --l3-border: #639922; --l3-text: #1E3106;
        --l4-bg: #FAEEDA; --l4-border: #BA7517; --l4-text: #4A2E09;
    }
    .mas-tree { font-family: 'Inter', sans-serif; display: flex; flex-direction: column; align-items: center; padding: 20px; }
    .node {
        padding: 14px 20px; border-radius: 10px; border: 2px solid;
        text-align: center; width: 260px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .node .title { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
    .node .desc { font-size: 11px; line-height: 1.4; opacity: 0.9; }
    .c-orch { background: var(--orch-bg); border-color: var(--orch-border); color: var(--orch-text); }
    .c-l1 { background: var(--l1-bg); border-color: var(--l1-border); color: var(--l1-text); }
    .c-l2 { background: var(--l2-bg); border-color: var(--l2-border); color: var(--l2-text); }
    .c-l3 { background: var(--l3-bg); border-color: var(--l3-border); color: var(--l3-text); }
    .c-l4 { background: var(--l4-bg); border-color: var(--l4-border); color: var(--l4-text); }
    .connector { height: 25px; width: 2px; background: #CBD5E1; }
    .level-row { display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; width: 100%; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

# --- 3. AGENT REPOSITORY ---
MAIN_AGENTS = {
    "🏭 Olefins/Ethylene": "Furnace and separation master control.",
    "💧 Methanol": "High-pressure synthesis and reformer kinetics.",
    "🌬️ Ammonia": "Shift conversion and synthesis loop logic.",
    "🧬 EO/EG": "Catalytic selectivity and glycol recovery.",
    "⚗️ MTBE": "Etherification and fractionation stability.",
    "🧪 Polymers": "Reaction rates and mechanical handling.",
    "💎 Phenols": "Oxidation and cleavage chain management.",
    "⛽ Refining Complex": "Crude-to-Coke value chain optimization.",
    "❄️ ASU": "Cryogenic air separation and compression.",
    "🔧 Utilities": "Steam, power, and flare network balancing."
}

# Map Tech to specific L1 & L2 Agents
TECH_SPECIFICS = {
    "🏭 Olefins/Ethylene": {"l1": ["Furnace Kinetic Agent", "CGC Efficiency Agent", "Quench TLE Agent"], "l2": ["TMT Safety Bounds", "Pass Flow Limits"]},
    "💧 Methanol": {"l1": ["SMR Slip Agent", "SynGas Ratio Agent", "Methanol Purity Agent"], "l2": ["S/C Ratio Guardrail", "Catalyst ΔP"]},
    "🌬️ Ammonia": {"l1": ["N2/H2 Balancer Agent", "Shift Conv. Agent", "SynLoop Purge Agent"], "l2": ["Converter Temp Profile", "SynGas Purity Bounds"]},
    "🧬 EO/EG": {"l1": ["Selectivity Agent", "Glycol Ratio Agent", "EO Reactor Agent"], "l2": ["Vapor Concentration Guard", "Catalyst Activity"]},
    "⚗️ MTBE": {"l1": ["Etherification Agent", "Methanol Recovery Agent", "Heat Balance Agent"], "l2": ["Methanol/C4 Ratio", "Isomerization Limits"]},
    "🧪 Polymers": {"l1": ["Reaction Rate Agent", "Grade Transition Agent", "Extruder Torque Agent"], "l2": ["Melt Index Bounds", "Reactor Pressure"]},
    "💎 Phenols": {"l1": ["Oxidation Agent", "Cleavage Yield Agent", "Fractionation Agent"], "l2": ["Peroxide Safety Limits", "Tar Formation Control"]},
    "⛽ Refining Complex": {"l1": ["Fractionation Agent", "Pre-heat Train Agent", "Coker Cycle Agent"], "l2": ["D86 Product Specs", "Tower Hydraulic Limits"]},
    "❄️ ASU": {"l1": ["Cryogenic Sep. Agent", "MAC Compression Agent", "PPU Health Agent"], "l2": ["Oxygen Purity Target", "Expander Delta-T"]},
    "🔧 Utilities": {"l1": ["Steam Header Agent", "Boiler Firing Agent", "Flare Leak Agent"], "l2": ["HP/LP Balance", "Emission Compliance Bounds"]}
}

INITIATIVES = {
    "📈 Production Efficiency": {"l3": "Yield Optimizer Agent", "l4": "Throughput Advisory"},
    "⚡ Energy Optimization": {"l3": "SEC Optimizer Agent", "l4": "Energy Intensity Advisory"},
    "🛠️ Reliability": {"l3": "RUL Optimizer Agent", "l4": "Maintenance Advisory"},
    "🌱 Sustainability Hub": {"l3": "Carbon Optimizer Agent", "l4": "ESG Compliance Advisory"},
    "🔄 Workflows": {"l3": "SOP Orchestrator Agent", "l4": "Shift Handover Advisory"}
}

# --- 4. DASHBOARD UI ---
st.title("🌐 Ingenero360AI | Solutions Agent Explorer")
st.markdown("### 1. Select Main Agent (Parent Technology)")

# Session State for Selection
if 'selected_tech' not in st.session_state:
    st.session_state.selected_tech = None

# TILE GRID
tech_list = list(MAIN_AGENTS.keys())
cols = st.columns(5)
for i, tech in enumerate(tech_list):
    with cols[i % 5]:
        if st.button(tech, key=f"btn_{tech}", use_container_width=True):
            st.session_state.selected_tech = tech

if st.session_state.selected_tech:
    st.divider()
    st.markdown(f"### 2. Child Agents (Strategic Initiatives) for **{st.session_state.selected_tech}**")
    
    # Initiative Selection
    init_choice = st.radio("Select an Initiative to explore the MAS Hierarchy:", list(INITIATIVES.keys()), horizontal=True)

    # --- 5. TREE GENERATION ---
    tech = st.session_state.selected_tech
    t_data = TECH_SPECIFICS[tech]
    i_data = INITIATIVES[init_choice]

    tree_html = f"""
    <div class="mas-tree">
        <div class="node c-orch">
            <div class="title">{tech} Orchestrator (L0)</div>
            <div class="desc">Fleet-wide coordination & master state monitoring</div>
        </div>
        <div class="connector"></div>
        
        <p style="font-size:10px; color:#94A3B8; font-weight:800; margin:0;">L1 · PRIMARY PHYSICS AGENTS</p>
        <div class="level-row">
            {" ".join([f'<div class="node c-l1"><div class="title">{a}</div><div class="desc">Domain Logic</div></div>' for a in t_data['l1']])}
        </div>
        <div class="connector"></div>

        <p style="font-size:10px; color:#94A3B8; font-weight:800; margin:0;">L2 · CONSTRAINT GUARDRAILS</p>
        <div class="level-row">
            {" ".join([f'<div class="node c-l2"><div class="title">{a}</div><div class="desc">Safety & Quality Limits</div></div>' for a in t_data['l2']])}
        </div>
        <div class="connector"></div>

        <p style="font-size:10px; color:#94A3B8; font-weight:800; margin:0;">L3 · STRATEGIC OPTIMIZER</p>
        <div class="node c-l3">
            <div class="title">{i_data['l3']}</div>
            <div class="desc">Multi-Objective Constraint Solver</div>
        </div>
        <div class="connector"></div>

        <p style="font-size:10px; color:#94A3B8; font-weight:800; margin:0;">L4 · RESULT BUS</p>
        <div class="node c-l4">
            <div class="title">{i_data['l4']}</div>
            <div class="desc">Actionable Advisory for Operators</div>
        </div>
    </div>
    """
    
    components.html(tree_html, height=800, scrolling=True)

    # --- 6. AGENT SCRIPTING DETAILS ---
    st.divider()
    st.markdown("### 📝 Detailed Agent Scripting")
    d1, d2 = st.columns(2)
    with d1:
        st.info(f"**How {tech} Agents work:**\nThe L0 Orchestrator dispatches L1 agents to ingest real-time sensor data from the DCS. The L1 agents apply {tech}-specific kinetics and physics to calculate unmeasured variables (Soft Sensors).")
    with d2:
        st.success(f"**How {init_choice} is achieved:**\nThe L3 Optimizer Agent takes the validated state from L1/L2 and identifies the most profitable operating point that respects all safety guardrails, sending results to the L4 Advisory Bus.")

else:
    st.info("Select a Main Agent tile above to explore the Child Agent hierarchy.")
