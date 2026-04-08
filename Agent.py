import streamlit as st
import streamlit.components.v1 as components

# --- 1. PAGE CONFIG & BRANDING ---
st.set_page_config(
    page_title="Ingenero360AI Matrix", 
    page_icon="📊", 
    layout="wide"
)

# logo_url fallback
logo_url = "https://raw.githubusercontent.com/surendalvi/Ingex/main/logo.png"

# --- 2. THE STRATEGIC MATRIX THEME (CSS) ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@500&display=swap');
    
    .main .block-container {{ padding: 1rem 2rem !important; background-color: #0F172A; font-family: 'Inter', sans-serif; color: white; }}
    
    /* CLEAN HEADER */
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
    
    /* HEADERS */
    th.col-header {{
        background: rgba(30, 41, 59, 0.8); color: #94A3B8; font-size: 11px; font-weight: 800;
        text-transform: uppercase; letter-spacing: 1px; padding: 15px; border-radius: 8px;
        border: 1px solid rgba(255,255,255,0.05); text-align: center;
    }}
    td.row-header {{
        background: rgba(30, 41, 59, 0.8); color: #F8FAFC; font-size: 13px; font-weight: 700;
        padding: 15px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.05);
        width: 160px; text-align: left;
    }}

    /* MATRIX CELLS */
    td.matrix-cell {{
        background: rgba(15, 23, 42, 0.4); border: 1px solid rgba(255,255,255,0.05);
        border-radius: 8px; padding: 12px; vertical-align: top;
        transition: all 0.3s ease;
    }}
    td.matrix-cell:hover {{
        background: rgba(30, 41, 59, 0.6); border-color: rgba(56, 189, 248, 0.3);
        transform: translateY(-2px);
    }}

    /* AGENT TAGS INSIDE CELLS */
    .agent-block {{ margin-bottom: 8px; }}
    .lvl-label {{ font-size: 8px; font-weight: 900; letter-spacing: 0.5px; margin-bottom: 2px; }}
    .agent-name {{ font-size: 10.5px; font-weight: 600; line-height: 1.3; }}
    
    /* COMMON DNA COLORS (L1, L2) */
    .c-dna {{ color: #94A3B8; opacity: 0.8; }}
    
    /* UNCOMMON INTELLIGENCE COLORS (L3, L4) */
    .u-brain {{ color: #F97316; }}   /* L3 Highlights */
    .u-result {{ color: #10B981; }}  /* L4 Highlights */

    .model-tag {{ font-family: 'JetBrains Mono', monospace; font-size: 7.5px; color: #475569; margin-top: 2px; }}

    /* RADIO BUTTONS */
    .stRadio > label {{ font-size: 11px !important; font-weight: 800 !important; color: #64748B !important; text-transform: uppercase; }}
</style>
""", unsafe_allow_html=True)

# --- 3. DATA REPOSITORY ---
PARENT_AGENTS = ["Olefins", "Methanol", "Ammonia", "EO/EG", "MTBE", "Polymers", "Phenols", "Refining", "ASU", "Utilities"]
CHILD_AGENTS = ["Production Efficiency", "Energy Optimization", "Reliability", "Sustainability Hub", "Workflows"]

TECH_DNA = {
    "Olefins": {"l1": "Furnace Kinetic", "l2": "TMT Safety"},
    "Methanol": {"l1": "SMR Kinetic", "l2": "S/C Ratio Guard"},
    "Ammonia": {"l1": "N2/H2 Balancer", "l2": "Conv. Temp Map"},
    "EO/EG": {"l1": "Selectivity Agent", "l2": "Vapor Guard"},
    "MTBE": {"l1": "Etherification", "l2": "Reflux Bounds"},
    "Polymers": {"l1": "Reaction Rate", "l2": "Melt Index Guard"},
    "Phenols": {"l1": "Oxidation Rate", "l2": "Peroxide Safety"},
    "Refining": {"l1": "Fractionation", "l2": "ASTM Product Specs"},
    "ASU": {"l1": "Cryogenic Sep.", "l2": "O2 Purity Target"},
    "Utilities": {"l1": "Steam Header", "l2": "Emission Ceiling"}
}

INIT_INTEL = {
    "Production Efficiency": {"l3": "Yield Maximizer", "l4": "Throughput Advisory", "m": "MINLP · BENCHMARK"},
    "Energy Optimization": {"l3": "SEC Optimizer", "l4": "Energy Intensity", "m": "LP · SEC TRENDING"},
    "Reliability": {"l3": "RUL Optimizer", "l4": "Maintenance Hub", "m": "PREDICTIVE · RUL"},
    "Sustainability Hub": {"l3": "Carbon Optimizer", "l4": "ESG Dashboard", "m": "FORECAST · FLARE"},
    "Workflows": {"l3": "SOP Compliance", "l4": "Handover Bus", "m": "GENAI · AUDIT"}
}

# --- 4. HEADER ---
st.markdown(f"""
    <div class="nav-header">
        <img src="{logo_url}" width="45" onerror="this.style.display='none'">
        <div style="margin-left:20px;">
            <div style="font-size:20px; font-weight:700; color:#F8FAFC;">INGERO360AI</div>
            <div style="font-size:9px; color:#F97316; font-weight:800; text-transform:uppercase; letter-spacing:2px;">Strategic Solution Matrix</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 5. INTERACTIVE FOCUS FILTERS ---
st.markdown("<p style='font-size:11px; font-weight:800; color:#475569; text-transform:uppercase; margin-left:5px;'>Filter View</p>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    filter_tech = st.multiselect("Focus Technology (Rows)", PARENT_AGENTS, default=["Olefins", "Refining", "Ammonia", "Utilities"])
with c2:
    filter_init = st.multiselect("Focus Initiative (Columns)", CHILD_AGENTS, default=CHILD_AGENTS)

# --- 6. GENERATE MATRIX HTML ---
matrix_html = f"""
<div class="matrix-wrapper">
    <table class="ing-matrix">
        <thead>
            <tr>
                <th class="col-header" style="background:transparent; border:none;"></th>
                {" ".join([f'<th class="col-header">{col}</th>' for col in filter_init])}
            </tr>
        </thead>
        <tbody>
"""

for tech in filter_tech:
    dna = TECH_DNA[tech]
    matrix_html += f"""
            <tr>
                <td class="row-header">{tech}</td>
    """
    for init in filter_init:
        intel = INIT_INTEL[init]
        matrix_html += f"""
                <td class="matrix-cell">
                    <div class="agent-block c-dna">
                        <div class="lvl-label">L1-L2 · COMMON</div>
                        <div class="agent-name">{dna['l1']} / {dna['l2']}</div>
                    </div>
                    <div class="agent-block u-brain">
                        <div class="lvl-label">L3 · UNCOMMON</div>
                        <div class="agent-name">{intel['l3']}</div>
                        <div class="model-tag">{intel['m']}</div>
                    </div>
                    <div class="agent-block u-result">
                        <div class="lvl-label">L4 · OUTCOME</div>
                        <div class="agent-name">{intel['l4']}</div>
                    </div>
                </td>
        """
    matrix_html += "</tr>"

matrix_html += """
        </tbody>
    </table>
</div>
"""

st.divider()
components.html(matrix_html, height=800, scrolling=True)

# --- 7. FOOTER LEGEND ---
st.markdown(f"""
<div style="background: rgba(30, 41, 59, 0.4); padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); margin-top: 20px;">
    <div style="display:flex; gap:40px; align-items:center;">
        <div style="font-size:11px; color:#94A3B8;"><span style="color:#475569; font-weight:800; margin-right:8px;">■</span><b>COMMON DNA:</b> Foundational Physics & Safety (L1-L2)</div>
        <div style="font-size:11px; color:#94A3B8;"><span style="color:#F97316; font-weight:800; margin-right:8px;">■</span><b>UNCOMMON BRAIN:</b> Strategic Initiative Optimization (L3)</div>
        <div style="font-size:11px; color:#94A3B8;"><span style="color:#10B981; font-weight:800; margin-right:8px;">■</span><b>OUTCOME:</b> Real-time Result Bus & Advisory (L4)</div>
    </div>
</div>
""", unsafe_allow_html=True)
