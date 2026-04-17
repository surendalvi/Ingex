import streamlit as st

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Ingenero360AI | Agentic AI for Industrial Operations",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------
# Sidebar Navigation
# -------------------------
st.sidebar.title("Ingenero360AI")
page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Platform & Architecture",
        "Solutions",
        "Industries",
        "Agents",
        "Case Studies",
        "Testimonials",
        "Request Demo"
    ]
)

# -------------------------
# Utility Functions
# -------------------------
def section_title(text):
    st.markdown(f"## {text}")

def paragraph(text):
    st.markdown(f"<p style='font-size:18px'>{text}</p>", unsafe_allow_html=True)

# -------------------------
# Pages
# -------------------------

# HOME
if page == "Home":
    st.markdown("# Ingenero360AI")
    st.markdown("### Agentic AI for Industrial Operations")

    paragraph(
        "Autonomous asset intelligence with governed execution and "
        "GenAI‑powered decision support for complex industrial operations."
    )

    st.columns(3)
    st.success("✅ Agentic AI, not dashboards")
    st.success("✅ Accountable actions, not recommendations")
    st.success("✅ GenAI only for human decision support")

    section_title("Why Ingenero360AI")
    paragraph(
        "Ingenero360AI brings together deep process expertise, autonomous AI agents, "
        "governed execution workflows, and GenAI‑powered user interaction into one "
        "enterprise‑grade platform."
    )

    section_title("What You Can Achieve")
    st.markdown("""
    - Improve plant efficiency and throughput  
    - Reduce energy intensity and emissions  
    - Increase asset reliability  
    - Standardize optimization across plants  
    - Convert AI insights into real business outcomes  
    """)

# PLATFORM & ARCHITECTURE
elif page == "Platform & Architecture":
    section_title("Platform Overview")

    paragraph(
        "Ingenero360AI is built as a layered Agentic AI architecture designed "
        "for trust, scalability, and real‑world execution."
    )

    section_title("Architecture Layers")

    st.markdown("""
    **Level‑0:** Ingenero.AI Platform  
    **Level‑1:** Products (IngeneroX, Ingenero360AI)  
    **Level‑2:** Primary Agents (Plant‑level intelligence)  
    **Level‑3:** Domain & Asset Agents  
    **Level‑4:** Cross‑Domain Functional Agents  
    **Level‑5:** Model Agents (Digital Twins, Optimizers)  
    **Level‑6:** Results & Insights  
    **Level‑7:** Action Governance & Accountability  
    **Level‑8:** Decision & User Layer (GenAI, Dashboards, Copilots)  
    """)

    paragraph(
        "This separation ensures AI autonomy without sacrificing control, trust, "
        "or accountability."
    )

# SOLUTIONS
elif page == "Solutions":
    section_title("Solutions")

    st.markdown("""
    ### Plant Efficiency
    - Throughput optimization
    - Bottleneck identification
    - Cross‑asset coordination

    ### Energy Optimization
    - Fuel, steam, and power optimization
    - Utilities coordination
    - Energy intensity reduction

    ### Reliability & Asset Performance
    - Degradation monitoring
    - Failure prediction
    - Maintenance decision support

    ### Sustainability & Energy Transition
    - Emissions and water optimization
    - ESG performance tracking
    - Regulatory readiness
    """)

# INDUSTRIES
elif page == "Industries":
    section_title("Industries Served")

    st.markdown("""
    - Fertilizers (Ammonia, Urea)
    - Petrochemicals (Olefins, Polymers, EO/EG)
    - Chemicals (Phenols, MTBE, BTX)
    - Refining
    - Air Separation Units
    - Utilities & Energy Systems
    """)

    paragraph(
        "Ingenero360AI scales across technologies while preserving deep, "
        "process‑specific intelligence."
    )

# AGENTS
elif page == "Agents":
    section_title("Agent Ecosystem")

    st.markdown("""
    ### Primary Agents
    Outcome‑driven agents that coordinate plant objectives.

    ### Domain & Asset Agents
    Furnace, Reformer, Compressor, Distillation, Utilities, and more – each with
    physics‑based intelligence.

    ### Functional Agents
    - Process Efficiency
    - Energy Optimization
    - Reliability
    - Sustainability
    - Asset Hub
    - APC
    - ORA – Operator Round Automation
    - Turnaround Management

    ### Model Agents
    Digital Twins, Virtual Labs, Benchmarking, Optimizers
    """)

    paragraph(
        "Together, these agents behave like a digital operations team—reasoning, "
        "collaborating, and continuously optimizing."
    )

# CASE STUDIES
elif page == "Case Studies":
    section_title("Case Studies")

    paragraph(
        "Ingenero360AI has delivered measurable value across integrated "
        "chemical and petrochemical complexes."
    )

    st.markdown("""
    **Multi‑Technology Optimization**
    - Methanol, Ammonia, Urea, Polymers, Phenols
    - Olefins, BTX, EO/EG, MTBE, Utilities
    - Significant multi‑million‑dollar value identified and realized

    **Fertilizer Operations**
    - Energy intensity reduction
    - Improved reliability

    **Utilities Optimization**
    - Steam, power, cooling water optimization
    """)

# TESTIMONIALS
elif page == "Testimonials":
    section_title("Client Testimonials")

    st.info(
        "“Ingenero360AI has become a strategic enabler in our journey toward "
        "data‑driven, energy‑efficient, and operationally excellent manufacturing.”"
    )

    st.caption("— Chief Executive Officer, Integrated Chemical Enterprise")

    st.info(
        "“What stood out was Ingenero’s deep understanding of plant operations "
        "and their ability to convert insights into actions our teams could implement.”"
    )

    st.caption("— Head of Operations")

# REQUEST DEMO
elif page == "Request Demo":
    section_title("Request a Demo")

    paragraph(
        "Talk to our experts to understand how Ingenero360AI can transform "
        "your operations."
    )

    with st.form("demo_form"):
        name = st.text_input("Name")
        company = st.text_input("Company")
        role = st.text_input("Role")
        email = st.text_input("Email")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.success("Thank you. Our team will reach out shortly.")
