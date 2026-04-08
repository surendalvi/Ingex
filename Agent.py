import streamlit as st
import streamlit.components.v1 as components

# --- 1. PAGE CONFIG & BRANDING ---
st.set_page_config(
    page_title="Ingenero360AI Agentic Hub", 
    page_icon="🤖", 
    layout="wide"
)

# logo_url setup with fallback
logo_url = "https://raw.githubusercontent.com/surendalvi/Ingex/main/logo.png"

# --- 2. THE PREMIUM AGENTIC THEME (CSS) ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@500&display=swap');
    
    /* Background & Global Font */
    .main .block-container {{ padding: 1rem 2rem !important; background-color: #0F172A; font-family: 'Inter', sans-serif; color: white; }}
    
    /* PROMINENT CLEAN HEADER */
    .nav-header {{
        display: flex; align-items: center; padding: 25px 35px; 
        background: linear-gradient(90deg, #1E293B 0%, #0F172A 100%); 
        border-bottom: 3px solid #F97316; /* Ingenero Orange Accent */
        margin-bottom: 20px; border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }}

    /* AGENTIC-AI ARCHITECTURE BOX (At Top) */
    .agentic-info-box {{
        background: rgba(56, 189, 248, 0.08); /* Subtle Blue Tint */
        border: 1.5px solid rgba(56, 189, 248, 0.2);
        padding: 20px 30px; border-radius: 12px; margin-bottom: 25px;
        line-height: 1.6;
    }}
    .agentic-title {{ color: #38BDF8; font-weight: 800; font-size: 16px; margin-bottom: 8px; display: block; }}
    .agentic-body {{ color: #CBD5E1; font-size: 14px; font-weight: 400; }}

    /* RADIO BUTTON CUSTOMIZATION */
    .stRadio > label {{ font-size: 12px !important; font-weight: 700 !important; color: #94A3B8 !important; text-transform: uppercase; margin-bottom: 10px; }}
    div[role="radiogroup"] {{ gap: 12px; }}

    /* MATRIX TABLE STYLING */
    .matrix-wrapper {{ overflow-x: auto; padding: 10px; }}
    table.ing-matrix {{ width: 100%; border-collapse: separate; border-spacing: 12px; table-layout: fixed; }}
    
    th.col-header {{
        background: rgba(30, 41, 59, 0.8); color: #F8FAFC; font-size: 12px; font-weight: 800;
        text-transform: uppercase; letter-spacing: 1.5px; padding: 18px; border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.1); text-align: center;
    }}
    td.row-header {{
        background: rgba(30, 41, 59, 0.8); color: #F97316; font-size: 14px; font-weight: 800;
        padding: 20px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1);
        width: 190px; text-align: left;
    }}

    td.matrix-cell {{
        background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px; padding: 20px; vertical-align: top; transition: all 0.3s ease;
    }}
    
    /* SUB-AGENT STYLING */
    .agent-list {{ list-style-type: none; padding: 0; margin: 0; }}
    .agent-item {{ margin-bottom: 15px; position: relative; padding-left: 20px; }}
    .agent-item::before {{ content: "•"; position: absolute; left: 0; font-weight: bold; font-size: 18px; line-height: 1; }}
    
    .lvl-label {{ font-size: 9px; font-weight: 900; letter-spacing: 1px; margin-bottom: 4px; text-transform: uppercase; }}
    .agent-name {{ font-size: 11.5px; font-weight: 600; line-height: 1.4; color: #F1F5F9; }}
    .model-tag {{ font-family: 'JetBrains Mono', monospace; font-size: 8.5px; color: #64748B; margin-top: 4px; }}

    /* COLOR CODING */
    .base-agent .lvl-label {{ color: #38BDF8; }}
    .increment-cell .lvl-label {{ color: #F97316; }}
    .increment-cell .agent-item:last-child .lvl-label {{ color: #10B981; }}
    
    .incremental-tag {{
        font-size: 9px; color: #F97316; font-weight: 900; text-transform: uppercase;
        letter-spacing: 1.5px; margin-bottom: 12px; display: flex; align-items: center; gap: 5px;
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

# --- 4. TOP PROMINENT HEADER ---
st.markdown(f"""
    <div class="nav-header">
        <img src="{logo_url}" width="55" onerror="this.style.display='none'">
        <div style="margin-left:25px;">
            <div style="font-size:28px; font-weight:800; color:#F8FAFC; letter-spacing:-1px;">INGERO360AI</div>
            <div style="font-size:12px; color:#F97316; font-weight:700; text-transform:uppercase; letter-spacing:3px;">Strategic Agent Ecosystem</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 5. AGENTIC-AI ARCHITECTURE INFO BOX ---
st.markdown("""
    <div class="agentic-info-box">
        <span class="agentic-title">Agentic-AI Architecture</span>
        <span class="agentic-body">
            The Ingenero360AI ecosystem uses a modular multi-agent structure. The <b>'Base Foundation'</b> 
            provides the technology-specific sensing and safety. Each <b>'Strategic Initiative'</b> 
            then stacks incremental Sub-Agents (Optimizer & Result Bus) to target specific business value.
        </span>
    </div>
""", unsafe_allow_html=True)

# --- 6. SELECTION INTERFACE (DEFAULTS: OLEFINS & PROD EFFICIENCY) ---
row_nav1, row_nav2 = st.columns(2)
with row_nav1:
    filter_tech = st.multiselect("Parent Agents (Technology DNA)", PARENT_AGENTS, default=["Olefins"])
with row_nav2:
    filter_init = st.multiselect("Child Agents (Strategic Intent)", CHILD_AGENTS, default=["Production Efficiency"])

# --- 7. THE STRATEGIC MATRIX ---
matrix_html = f"""
<div class="matrix-wrapper">
    <table class="ing-matrix">
        <thead>
            <tr>
                <th class="col-header" style="background:transparent; border:none;"></th>
                <th class="col-header" style="background:rgba(56, 189, 248, 0.1); color:#38BDF8; border-color:rgba(56, 189, 248, 0.3);">Base Foundation Agents</th>
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
                <td class="matrix-cell" style="border: 1px dashed rgba(249, 115, 22, 0.4); background: rgba(249, 115, 22, 0.05);">
                    <span class="incremental-tag"><span style="font-size:14px;">+</span> Incremental Strategy</span>
                    <ul class="agent-list" style="margin-top:10px;">
                        <li class="agent-item increment-cell">
                            <div class="lvl-label">Sub-Agent 3: Optimizer</div>
                            <div class="agent-name">{extra['l3']}</div>
                            <div class="model-tag">{extra['m']}</div>
                        </li>
                        <li class="agent-item increment-cell">
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
components.html(matrix_html, height=650, scrolling=True)

# --- 8. MARKETING LEGEND ---
st.markdown(f"""
<div style="background: rgba(30, 41, 59, 0.6); padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); margin-top: 25px; text-align: center;">
    <div style="display:inline-flex; gap:50px; align-items:center;">
        <div style="font-size:12px; color:#94A3B8;"><span style="color:#38BDF8; font-weight:800; margin-right:8px;">■</span><b>Base DNA:</b> Common Tech Sub-Agents</div>
        <div style="font-size:12px; color:#94A3B8;"><span style="color:#F97316; font-weight:800; margin-right:8px;">■</span><b>Incremental Brain:</b> Initiative Sub-Agents</div>
        <div style="font-size:12px; color:#94A3B8;"><span style="color:#10B981; font-weight:800; margin-right:8px;">■</span><b>Result Bus:</b> Final Decision Support</div>
    </div>
</div>
""", unsafe_allow_html=True)
