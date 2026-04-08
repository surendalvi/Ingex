import streamlit as st
import streamlit.components.v1 as components

# --- 1. PAGE CONFIG & BRANDING ---
st.set_page_config(
    page_title="Ingenero360AI Command Hub", 
    page_icon="🔘", 
    layout="wide"
)

# Robust Logo Definition to prevent NameError
def get_logo_url():
    repo_url = "https://github.com/surendalvi/Ingex/blob/main/logo.png"
    # Fallback to an empty string if the function is missing or fails
    try:
        parts = repo_url.split("/")
        username, repo_name = parts[3], parts[4]
        return f"https://raw.githubusercontent.com/{username}/{repo_name}/main/logo.png"
    except:
        return ""

logo_url = get_logo_url()

# --- 2. PREMIUM CSS: THE PRECISION UI ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    .main .block-container { padding: 1.5rem 3rem !important; background-color: #F8FAFC; font-family: 'Inter', sans-serif; }
    
    /* Selection Dial styling */
    .stButton > button {
        width: 100%; border-radius: 50px; height: 50px;
        border: 1px solid #CBD5E1; background-color: #E2E8F0;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        font-weight: 700; color: #64748B; font-size: 13px;
    }
    
    /* Highlight Active Selection */
    div[data-testid="stHorizontalBlock"] button[kind="secondary"]:active,
    div[data-testid="stHorizontalBlock"] button[kind="secondary"]:focus,
    div[data-testid="stHorizontalBlock"] button[kind="secondary"]:hover {
        border-color: #0F172A;
    }

    /* MAS TREE Logic */
    :root {
        --orch-bg: #F8FAFC; --orch-border: #0F172A; --orch-text: #0F172A;
        --tech-bg: #FFFFFF; --tech-border: #E2E8F0; --tech-text: #475569;
        --highlight-bg: #EEEDFE; --highlight-border: #7F77DD; --highlight-text: #26215C;
        --result-bg: #EAF3DE; --result-border: #639922; --result-text: #1E3106;
    }
    .mas-tree { display: flex; flex-direction: column; align-items: center; padding: 20px; }
    .node {
        padding: 14px 18px; border-radius: 10px; border: 2px solid;
        text-align: center; width: 260px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); margin: 4px;
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

# Agent Logic Mapping
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
        <img src="{logo_url}" width="35" onerror="this.style.display='none'">
        <div style="margin-left:15px;">
            <div style="font-size:18px; font-weight:800; color:#0F172A; letter-spacing:-0.5px;">INGERO360AI</div>
            <div style="font-size:9px; color:#64748B; font-weight:700; text-transform:uppercase; letter-spacing:1px;">Precision Command Hub</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 6. SELECTION DIAL (Parent Agents) ---
st.markdown("<p style='font-size:11px; font-weight:800; color:#94A3B8; text-transform:uppercase; margin-bottom:10px;'>Parent Agent Selection Dial</p>", unsafe_allow_html=True)
dial_cols = st.columns(len(PARENT_AGENTS))
for i, tech in enumerate(PARENT_AGENTS):
    with dial_cols[i]:
        # Using a distinct label if active
        label = f"◈ {tech}" if st.session_state.tech == tech else tech
        if st.button(label, key=f"d_{tech}", use_container_width=True):
            st.session_state.tech = tech
            st.rerun()

# --- 7. STRATEGY TILES (Child Agents) ---
st.markdown("<p style='font-size:11px; font-weight:800; color:#94A3B8; text-transform:uppercase; margin:20px 0 10px 0;'>Child Agent Strategy Tiles</p>", unsafe_allow_html=True)
init_cols = st.columns(len(CHILD_AGENTS))
for i, init in enumerate(CHILD_AGENTS):
    with init_cols[i]:
        label = f"✓ {init}" if st.session_state.init == init else init
        if st.button(label, key=f"c_{init}", use_container_width=True):
            st.session_state.init = init
            st.rerun()

# --- 8. MAS TREE (UNCOMMON AGENT HIGHLIGHTING) ---
st.divider()
t_data = TECH_MAP[st.session_state.tech]
i_data = INIT_MAP[st.session_state.init]

tree_html = f"""
<div class="mas-tree">
    <div class="node c-orch">
        <div class="title">{st.session_state.tech} Orchestrator</div>
        <div class="desc">L0 Parent Agent: Domain Governance</div>
        <div class="level-tag">Master</div>
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
        <div class="desc">Uncommon: {st.session_state.init} Brain</div>
        <div class="level-tag" style="color:#7F77DD;">L3 · Difference Maker</div>
    </div>
    <div class="connector"></div>

    <div class="node c-result">
        <div class="title">{i_data['l4']}</div>
        <div class="desc">Strategic Results Interface</div>
        <div class="level-tag" style="color:#639922;">L4 · Outcome</div>
    </div>
</div>
"""

components.html(tree_html, height=750, scrolling=False)
