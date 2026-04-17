import streamlit as st

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Ingenero360AI | Agentic AI for Industrial Operations",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------------------------------
# Custom CSS (Enterprise Look & Feel)
# -------------------------------------------------
def load_css():
    st.markdown("""
    <style>

    .block-container {
        max-width: 1200px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #0B4C8C;
        font-weight: 600;
    }

    p {
        font-size: 17px;
        line-height: 1.7;
        color: #1F2933;
    }

    section[data-testid="stSidebar"] {
        background-color: #F5F7FA;
        padding-top: 2rem;
    }

    .stButton button {
        background-color: #0B4C8C;
        color: white;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
        border-radius: 6px;
        border: none;
    }

    .stButton button:hover {
        background-color: #093A6A;
    }

    hr {
        border: 0;
        height: 1px;
        background: #E5E7EB;
        margin: 2.5rem 0;
    }

    </style>
    """, unsafe_allow_html=True)

load_css()

# -------------------------------------------------
# Helpers
# -------------------------------------------------
def section(title, body):
    st.markdown(f"## {title}")
    st.markdown(body)

def divider():
    st.markdown("<hr />", unsafe_allow_html=True)

# -------------------------------------------------
# Sidebar Navigation
# -------------------------------------------------
st.sidebar.title("Ingenero360AI")
page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Platform",
        "Architecture",
        "Solutions",
        "Industries",
        "Agents",
        "Case Studies",
        "Testimonials",
        "Request a Demo"
    ],
)

# =================================================
# HOME
# =================================================
if page == "Home":
    st.markdown("# Ingenero360AI")
    st.markdown("### Agentic AI Platform for Industrial Operations")

    st.markdown("""
    Ingenero360AI delivers **autonomous asset intelligence** with built‑in governance
    and **GenAI‑powered decision support**, enabling measurable and sustainable
    operational excellence across complex industrial environments.
    """)

    st.button("Request a Demo")

    divider()

    section(
        "Why Ingenero360AI",
        """
        - Agentic AI that reasons and acts across assets  
        - Governed workflows that ensure accountability  
        - GenAI only at the interface — never in plant control  
        """
    )

    divider()

    section(
        "Proven Across Technologies",
        """
        Methanol • Ammonia • Urea • Polymers • Phenols • Olefins • BTX • EO/EG • MTBE • Utilities
        """
    )

# =================================================
# PLATFORM
# =================================================
elif page == "Platform":
    section(
        "What is Ingenero360AI?",
        """
        Ingenero360AI is an enterprise‑grade Agentic AI platform designed for
        process industries. It combines autonomous AI agents, deep process
        expertise, advanced optimization models, and governance frameworks
        into a single operational intelligence system.
        """
    )

    section(
        "Core Principles",
        """
        - Outcome‑driven intelligence, not isolated analytics  
        - Continuous reasoning, not point‑in‑time recommendations  
        - Trust, transparency, and accountability by design  
        """
    )

# =================================================
# ARCHITECTURE
# =================================================
elif page == "Architecture":
    section(
        "Layered Agentic AI Architecture",
        """
        **Level 0:** Ingenero.AI Platform  
        **Level 1:** Products (Ingenero360AI)  
        **Level 2:** Primary Agents (Plant‑level intelligence)  
        **Level 3:** Domain & Asset Agents  
        **Level 4:** Cross‑Domain Functional AI Agents  
        **Level 5:** Model Agents (Digital Twins, Optimizers)  
        **Level 6:** Results & Insights  
        **Level 7:** Action Governance & Accountability  
        **Level 8:** Decision & User Layer (GenAI, Dashboards, Copilots)  
        """
    )

    st.caption("This structure ensures autonomy without sacrificing safety or control.")

# =================================================
# SOLUTIONS
# =================================================
elif page == "Solutions":
    section(
        "Plant Efficiency",
        "Throughput improvement, constraint removal, and stable operations."
    )
    section(
        "Energy Optimization",
        "Fuel, steam, and power optimization across processes and utilities."
    )
    section(
        "Reliability & Asset Performance",
        "Failure prediction, degradation tracking, and maintenance decision support."
    )
    section(
        "Sustainability & Energy Transition",
        "Energy intensity reduction, emissions tracking, and ESG readiness."
    )

# =================================================
# INDUSTRIES
# =================================================
elif page == "Industries":
    section(
        "Industries We Serve",
        """
        - Fertilizers (Ammonia, Urea)  
        - Petrochemicals (Olefins, Polymers, EO/EG)  
        - Chemicals (Phenols, MTBE, BTX)  
        - Refining & Energy  
        - Air Separation Units  
        - Utilities & Infrastructure  
        """
    )

# =================================================
# AGENTS
# =================================================
elif page == "Agents":
    section(
        "Agent Ecosystem",
        """
        **Primary Agents** – Plant‑level outcome coordination  
        **Domain & Asset Agents** – Furnace, Reformer, Distillation, Compression, Utilities  
        **Functional Agents** – Process Efficiency, Energy, Reliability, Sustainability  
        **ORA** – Operator Round Automation  
        **TAM** – Turnaround Management  
        **Model Agents** – Digital Twins, Virtual Labs, Optimizers  
        """
    )

# =================================================
# CASE STUDIES
# =================================================
elif page == "Case Studies":
    section(
        "Multi‑Technology Optimization",
        """
        Integrated deployment across Methanol, Ammonia, Polymers, Olefins,
        EO/EG, MTBE, and Utilities delivering significant multi‑million‑dollar
        value with disciplined execution.
        """
    )

# =================================================
# TESTIMONIALS
# =================================================
elif page == "Testimonials":
    st.info(
        "“Ingenero360AI has become a critical enabler in our journey toward "
        "data‑driven, energy‑efficient, and operationally excellent manufacturing.”"
    )
    st.caption("— Chief Executive Officer, Integrated Chemical Enterprise")

    st.info(
        "“Ingenero’s deep process understanding and accountable AI approach "
        "turned complex insights into actions our teams could implement.”"
    )
    st.caption("— Head of Operations")

# =================================================
# REQUEST DEMO (STABLE IMPLEMENTATION)
# =================================================
elif page == "Request a Demo":
    section(
        "Request a Demo",
        "Engage with our experts to understand how Ingenero360AI can transform your operations."
    )

    with st.form("demo_form_v2", clear_on_submit=True):
        st.text_input("Full Name", key="name")
        st.text_input("Company", key="company")
        st.text_input("Role / Designation", key="role")
        st.text_input("Work Email", key="email")
        st.text_area("Brief Description of Your Challenge", key="challenge")

        submit = st.form_submit_button("Submit")

    if submit:
        st.success("Thank you. Our team will reach out shortly.")
