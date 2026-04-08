import streamlit as st
import streamlit.components.v1 as components

# --- 1. PAGE CONFIG & BRANDING ---
st.set_page_config(
    page_title="Ingenero360AI Agentic Hub", 
    page_icon="🤖", 
    layout="wide"
)

logo_url = "https://raw.githubusercontent.com/surendalvi/Ingex/main/logo.png"

# --- 2. THE AGENTIC MATRIX THEME (CSS) ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@500&display=swap');
    
    .main .block-container {{ padding: 1rem 2rem !important; background-color: #0F172A; font-family: 'Inter', sans-serif; color: white; }}
    
    .nav-header {{
        display: flex; align-items: center; padding: 15px 25px; 
        background: rgba(30, 41, 59, 0.4); border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px; border-radius: 12px;
    }}

    /* MATRIX TABLE STYLING */
    .matrix-wrapper {{ overflow-x: auto; padding: 10px; }}
    table.ing-matrix {{
        width: 100%; border-collapse: separate; border-spacing: 8px; table-layout: fixed;
    }}
    
    th.col-header {{
        background: rgba(30, 41, 59, 0.8); color: #94A3B8; font-size: 11px; font-weight: 800;
        text-transform: uppercase; letter-spacing: 1px; padding: 15px; border-radius: 8px;
        border: 1px solid rgba(255,255,255,0.05); text-align: center;
    }}
    td.row-header {{
        background: rgba(30, 41, 59, 0.8); color: #F8FAFC; font-size: 13px; font-weight: 700;
        padding: 15px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.05);
        width: 180px; text-align: left;
    }}

    td.matrix-cell {{
        background: rgba(15, 23, 42, 0.4); border: 1px solid rgba(255,255,255,0.05);
        border-radius: 8px; padding: 15px; vertical-align: top;
        transition: all 0.3s ease;
    }}
    
    /* SPECIAL STYLING FOR INCREMENTAL CELLS */
    td.increment-cell {{
        border: 1px dashed rgba(249, 115, 22, 0.3);
        background: rgba(249, 115, 22, 0.03);
    }}

    /* BULLET LIST STYLING */
    .agent-list {{ list-style-type: none; padding: 0; margin: 0; }}
    .agent-item {{ margin-bottom: 12px; position: relative; padding-left: 20px; }}
    .agent-item::before {{
        content: "•"; position: absolute; left: 0; font-weight: bold;
    }}
    
    .lvl-label {{ font-size: 9px; font-weight: 900; letter-spacing: 0.5px; margin-bottom: 2px; text-transform: uppercase; }}
    .agent-name {{ font-size: 11px; font-weight: 600; line-height: 1.3; color: #F1F5F9; }}
    .model-tag {{ font-family: 'JetBrains Mono', monospace; font-size: 8px; color: #64748B; margin-top: 2px; }}

    /* SUB-AGENT SPECIFIC HIGHLIGHTS */
    .base-agent .lvl-label {{ color: #38BDF8; }}
    .opt-agent .lvl-label {{ color: #F97316; }}
    .res-agent .lvl-label {{ color: #10B981; }}
    
    .incremental-tag {{
        font-size: 8px; color: #F97316; font-weight: 800; text-transform: uppercase;
        letter-spacing: 1px; margin-bottom: 8px; display: block;
    }}
</style>
""", unsafe_allow_html=True)

# --- 3. DATA REPOSITORY ---
PARENT_AGENTS = ["Olefins", "Methanol", "Ammonia", "EO/EG", "MTBE", "Polymers", "Phenols", "Refining", "ASU", "Utilities"]
CHILD_AGENTS = ["Production Efficiency", "Energy Optimization", "Reliability", "Sustainability Hub", "Workflows"]

TECH_BASE_AGENTS = {
    "Olefins": {"l1": "Furnace Kinetic Sub-Agent", "l2": "TMT Safety Sub-Agent"},
    "Methanol": {"l1": "SMR Kinetic Sub-Agent", "l2": "S/C Ratio Sub-Agent"},
    "Ammonia": {"l1": "N2/H2 Balancer Sub-Agent", "l2": "Conv. Temp Sub-Agent"},
    "EO/EG": {"l1": "Selectivity Sub-Agent", "l2": "Vapor Guard Sub-Agent"},
    "MTBE": {"l1": "Etherification Sub-Agent", "l2": "Reflux Sub-Agent"},
    "Polymers": {"l1": "Reaction Rate Sub-Agent", "l2": "Melt Index Sub-Agent"},
    "Phenols": {"l1": "Oxidation Rate Sub-Agent", "l2": "Peroxide Sub-Agent"},
    "Refining": {"l1": "Fractionation Sub-Agent", "l2": "ASTM Spec Sub-Agent"},
    "ASU": {"l1": "Cryogenic Sep. Sub-Agent", "l2": "O2 Purity Sub-Agent"},
    "Utilities": {"l1": "Steam Header Sub-Agent", "l2": "Emission Sub-Agent"}
}

INIT_INCREMENTAL_AGENTS = {
    "Production Efficiency": {"l3": "Yield Maximizer Sub-Agent", "l4": "Throughput Advisory Sub-Agent", "m": "MINLP · BENCHMARK"},
    "Energy Optimization": {"l3": "SEC Optimizer Sub-Agent", "l4": "Energy Intensity Sub-Agent", "m": "LP · SEC TRENDING"},
    "Reliability": {"l3": "RUL Optimizer Sub-Agent", "l4": "Maintenance Hub Sub-Agent", "m": "PREDICTIVE · RUL"},
    "Sustainability Hub": {"l3": "Carbon Optimizer Sub-Agent", "l4": "ESG Dashboard Sub-Agent", "m": "FORECAST · FLARE"},
    "Workflows": {"l3": "SOP Compliance Sub-Agent", "l4": "Handover Bus Sub-Agent", "m": "GENAI · AUDIT"}
}

# --- 4. HEADER ---
st.markdown(f"""
    <div class="nav-header">
        <img src="{logo_url}" width="45" onerror="this.style.display='none'">
        <div style="margin-left:20px;">
            <div style="font-size:20px; font-weight:700; color:#F8FAFC;">INGERO360AI</div>
            <div style="font-size:9px; color:#38BDF8; font-weight:800; text-transform:uppercase; letter-spacing:2px;">Agentic-AI Solution Matrix</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 5. INTERACTIVE FILTERS (DEFAULTS: OLEFINS & PROD EFFICIENCY) ---
c1, c2 = st.columns(2)
with c1:
    filter_tech = st.multiselect("Parent Agents (Technology Domain)", PARENT_AGENTS, default=["Olefins"])
with c2:
    filter_init = st.multiselect("Child Agents (Strategic Initiative)", CHILD_AGENTS, default=["Production Efficiency"])

# --- 6. GENERATE AGENTIC MATRIX ---
matrix_html = f"""
<div class="matrix-wrapper">
    <table class="ing-matrix">
        <thead>
            <tr>
                <th class="col-header" style="background:transparent; border:none;"></th>
                <th class="col-header" style="background:rgba(56, 189, 248, 0.1); color:#38BDF8;">Base Foundation Agents</th>
                {" ".join([f'<th class="col-header">{col}</th>' for col in filter_init])}
            </tr>
        </thead>
        <tbody>
"""

for tech in filter_tech:
    base = TECH_BASE_AGENTS[tech]
    matrix_html += f"""
            <tr>
                <td class="row-header">{tech}</td>
                <td class="matrix-cell">
                    <ul class="agent-list">
                        <li class="agent-item base-agent">
                            <div class="lvl-label">Sub-Agent 1: Sensing</div>
                            <div class="agent-name">{base['l1']}</div>
                        </li>
                        <li class="agent-item base-agent">
                            <div class="lvl-label">Sub-Agent 2: Guardrails</div>
                            <div class="agent-name">{base['l2']}</div>
                        </li>
                    </ul>
                </td>
    """
    for init in filter_init:
        extra = INIT_INCREMENTAL_AGENTS[init]
        matrix_html += f"""
                <td class="matrix-cell increment-cell">
                    <span class="incremental-tag">+ Incremental Strategy</span>
                    <ul class="agent-list">
                        <li class="agent-item opt-agent">
                            <div class="lvl-label">Sub-Agent 3: Optimizer</div>
                            <div class="agent-name">{extra['l3']}</div>
                            <div class="model-tag">{extra['m']}</div>
                        </li>
                        <li class="agent-item res-agent">
                            <div class="lvl-label">Sub-Agent 4: Result Bus</div>
                            <div class="agent-name">{extra['l4']}</div>
                        </li>
                    </ul>
                </td>
        """
    matrix_html += "</tr>"

matrix_html += """
        </tbody>
    </table>
</div>
"""

st.divider()
components.html(matrix_html, height=600, scrolling=True)

# --- 7. FOOTER LEGEND ---
st.info("**Agentic-AI Architecture:** The Ingenero360AI ecosystem uses a modular multi-agent structure. The 'Base Foundation' provides the technology-specific sensing and safety. Each 'Strategic Initiative' then stacks incremental Sub-Agents (Optimizer & Result Bus) to target specific business value.")
