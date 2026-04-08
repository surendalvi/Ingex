import streamlit as st
import streamlit.components.v1 as components

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ingenero360AI | Agent Architecture",
    page_icon="🤖",
    layout="wide"
)

# --- 2. CSS FOR THE TREE DIAGRAM (Integrated MAS Logic) ---
# This CSS handles the visual hierarchy of L0 to L4 Agents
TREE_CSS = """
<style>
    :root {
        --orch-bg: #EEEDFE; --orch-border: #7F77DD; --orch-text: #26215C;
        --l1-bg: #E6F1FB; --l1-border: #378ADD; --l1-text: #042C53;
        --l2-bg: #FAECE7; --l2-border: #D85A30; --l2-text: #5D2412;
        --l3-bg: #EAF3DE; --l3-border: #639922; --l3-text: #1E3106;
        --l4-bg: #FAEEDA; --l4-border: #BA7517; --l4-text: #4A2E09;
    }
    .mas-tree { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding: 20px; }
    .node-container { display: flex; flex-direction: column; align-items: center; margin-bottom: 30px; }
    .node {
        padding: 12px 18px; border-radius: 10px; border: 2px solid;
        text-align: center; width: 240px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .node .title { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
    .node .desc { font-size: 11px; line-height: 1.4; opacity: 0.9; }
    
    .c-orch { background: var(--orch-bg); border-color: var(--orch-border); color: var(--orch-text); }
    .c-l1 { background: var(--l1-bg); border-color: var(--l1-border); color: var(--l1-text); }
    .c-l2 { background: var(--l2-bg); border-color: var(--l2-border); color: var(--l2-text); }
    .c-l3 { background: var(--l3-bg); border-color: var(--l3-border); color: var(--l3-text); }
    .c-l4 { background: var(--l4-bg); border-color: var(--l4-border); color: var(--l4-text); }

    .connector { height: 20px; width: 2px; background: #CBD5E1; }
    .level-row { display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; width: 100%; }
    .section-label { font-size: 12px; font-weight: 800; color: #94A3B8; margin-top: 10px; text-transform: uppercase; }
</style>
"""

# --- 3. MASTER DATA REPOSITORY ---
TECH_DATA = {
    "Olefins": {"l1": ["Furnace Kinetic Agent", "Quench Oil Agent", "CGC Efficiency Agent"], "l2": ["TMT Safety Limits", "Pass Flow Balance"]},
    "Methanol": {"l1": ["Reformer Slip Agent", "SynGas Ratio Agent", "Methanol Purity Agent"], "l2": ["S/C Ratio Bounds", "Catalyst ΔP"]},
    "Ammonia": {"l1": ["N2/H2 Balance Agent", "Shift Converter Agent", "SynLoop Purge Agent"], "l2": ["Converter Temp Profile", "SynGas Purity"]},
    "EOEG": {"l1": ["Selectivity Agent", "Glycol Ratio Agent", "EO Reactor Agent"], "l2": ["Catalyst Selectivity Bounds", "Vapor Concentration"]},
    "MTBE": {"l1": ["Etherification Agent", "Methanol Recovery Agent", "Reactor Heat Agent"], "l2": ["Methanol/C4 Ratio", "Isomerization Limits"]},
    "Polymers": {"l1": ["Polymerization Rate Agent", "Grade Transition Agent", "Extruder Torque Agent"], "l2": ["Melt Index Bounds", "Reactor Pressure"]},
    "Phenols": {"l1": ["Oxidation Agent", "Cleavage Yield Agent", "Fractionation Agent"], "l2": ["Peroxide Safety Limits", "Tar Formation Control"]},
    "Refining": {"l1": ["Fractionation Cut-Point Agent", "Pre-heat Train Agent", "Coker Cycle Agent"], "l2": ["ASTM D86 Specs", "Hydraulic Flooding Limits"]},
    "ASU": {"l1": ["Cryogenic Separation Agent", "Air Compression Agent", "PPU Health Agent"], "l2": ["Oxygen Purity Target", "Expander Delta-T"]},
    "Utilities": {"l1": ["Steam Header Agent", "Boiler Firing Agent", "Flare Leak Agent"], "l2": ["HP/LP Steam Balance", "Emission Compliance"]}
}

INITIATIVE_DATA = {
    "Production Efficiency": {"l3": "Yield/Selectivity Optimizer", "l4": "Throughput Advice Bus"},
    "Energy Optimization": {"l3": "Specific Energy (SEC) Optimizer", "l4": "Energy Intensity Bus"},
    "Reliability": {"l3": "Asset Health/RUL Optimizer", "l4": "Maintenance Advisory Bus"},
    "Sustainability & Asset Metric Hub": {"l3": "Carbon/Flare Intensity Optimizer", "l4": "ESG Compliance Bus"},
    "Workflows": {"l3": "Digital SOP/Alert Orchestrator", "l4": "Shift Handover Bus"}
}

# --- 4. STREAMLIT UI ---
st.title("🌐 Ingenero360AI | Enterprise MAS Dashboard")
st.markdown("### Digital Solution Multi-Agent Hierarchy")

with st.sidebar:
    st.header("⚙️ Configuration")
    tech_choice = st.selectbox("Select Technology", list(TECH_DATA.keys()))
    init_choice = st.selectbox("Select Initiative", list(INITIATIVE_DATA.keys()))
    
    st.divider()
    st.info("**Agent Logic Hierarchy:**\n\n"
            "**L0:** Domain Orchestrator\n"
            "**L1:** Primary Sensing Agents\n"
            "**L2:** Guardrail Constraints\n"
            "**L3:** Strategic Optimizers\n"
            "**L4:** Result Bus (Decision Support)")

# --- 5. TREE GENERATION LOGIC ---
def generate_tree(tech, init):
    t_info = TECH_DATA[tech]
    i_info = INITIATIVE_DATA[init]
    
    html = f"""
    {TREE_CSS}
    <div class="mas-tree">
        <div class="node-container">
            <div class="node c-orch">
                <div class="title">{tech} Orchestrator</div>
                <div class="desc">Fleet-wide coordination & state management</div>
            </div>
            <div class="connector"></div>
            <div class="section-label">L1 · Primary Technology Agents</div>
            <div class="level-row">
                {" ".join([f'<div class="node c-l1"><div class="title">{a}</div><div class="desc">Domain Physics/Kinetics</div></div>' for a in t_info['l1']])}
            </div>
            <div class="connector"></div>
            <div class="section-label">L2 · Constraint Guardrails</div>
            <div class="level-row">
                {" ".join([f'<div class="node c-l2"><div class="title">{a}</div><div class="desc">Safety & Quality Bounds</div></div>' for a in t_info['l2']])}
            </div>
            <div class="connector"></div>
            <div class="section-label">L3 · {init} Optimizer</div>
            <div class="node c-l3">
                <div class="title">{i_info['l3']}</div>
                <div class="desc">Strategic Multi-Objective Solver</div>
            </div>
            <div class="connector"></div>
            <div class="section-label">L4 · Result Bus</div>
            <div class="node c-l4">
                <div class="title">{i_info['l4']}</div>
                <div class="desc">Actionable Advisory for Operators</div>
            </div>
        </div>
    </div>
    """
    return html

# --- 6. RENDER ---
tree_html = generate_tree(tech_choice, init_choice)
components.html(tree_html, height=850, scrolling=True)

# --- 7. AGENT SCRIPTING DETAILS ---
st.divider()
st.markdown("### 📝 Agent Role Details")

col1, col2 = st.columns(2)
with col1:
    st.write(f"**Technology Stack: {tech_choice}**")
    for a in TECH_DATA[tech_choice]['l1']:
        st.write(f"- `{a}`: Responsible for ingestion of DCS/Historian data and applying {tech_choice}-specific physics/kinetic models.")
with col2:
    st.write(f"**Initiative Stack: {init_choice}**")
    st.write(f"- `{INITIATIVE_DATA[init_choice]['l3']}`: Consumes L1/L2 data to solve for the best economic/technical operating point.")
    st.write(f"- `{INITIATIVE_DATA[init_choice]['l4']}`: Formats the L3 output into human-readable advice or automated setpoint changes.")

st.markdown("<br><center><small>Ingenero360AI | Confidential Strategy Matrix</small></center>", unsafe_allow_html=True)
