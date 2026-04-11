import streamlit as st
import streamlit.components.v1 as components

# 1. SETUP & THEME
st.set_page_config(page_title="Ingenero360AI | Strategic Agentic-AI", layout="wide")

# Custom CSS for a Marketing Landing Page
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');
    .main { background-color: #0F172A; font-family: 'Inter', sans-serif; color: white; }
    
    /* Hero Section */
    .hero {
        padding: 100px 50px; text-align: center;
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
        border-bottom: 4px solid #F97316; margin-bottom: 50px;
    }
    .hero h1 { font-size: 64px; font-weight: 900; letter-spacing: -2px; margin-bottom: 10px; }
    .hero p { font-size: 20px; color: #94A3B8; max-width: 800px; margin: 0 auto; }

    /* Feature Cards */
    .card {
        background: rgba(30, 41, 59, 0.5); padding: 30px; border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.1); transition: 0.3s;
    }
    .card:hover { border-color: #F97316; transform: translateY(-5px); }
    .card h3 { color: #38BDF8; margin-bottom: 15px; }

    /* Agentic Box */
    .agentic-box {
        background: rgba(56, 189, 248, 0.05); border: 1px solid #38BDF8;
        padding: 30px; border-radius: 20px; margin: 40px 0;
    }
</style>
""", unsafe_allow_html=True)

# 2. HERO SECTION
st.markdown("""
<div class="hero">
    <h1>INGERO360AI</h1>
    <p>The World's First <b>Strategic Multi-Agent Ecosystem</b> for Industrial Autonomy. 
    Bridge the gap between raw data and executive intent with Agentic-AI.</p>
    <br>
    <a href="#matrix" style="text-decoration:none;">
        <button style="background:#F97316; color:white; border:none; padding:12px 30px; border-radius:30px; font-weight:800; cursor:pointer;">
            Explore the Ecosystem
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# 3. VALUE PROPOSITION
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""<div class="card"><h3>Built-in Technology DNA</h3><p>Pre-configured Parent Agents for 10+ industries including Olefins, Refining, and Ammonia.</p></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="card"><h3>Strategic Initiatives</h3><p>Hot-swap Sub-Agents to pivot between Energy, Yield, Reliability, and Sustainability instantly.</p></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="card"><h3>Agentic-AI Core</h3><p>Powered by a 5-level hierarchy of autonomous Sub-Agents using MINLP and GenAI models.</p></div>""", unsafe_allow_html=True)

# 4. THE AGENTIC EXPLANATION
st.markdown("""
<div class="agentic-box">
    <h2 style="color:#F8FAFC; margin-bottom:10px;">The Architecture of Intelligence</h2>
    <p style="color:#94A3B8;">Unlike standard monitoring tools, <b>Ingenero360AI</b> uses a modular multi-agent structure. 
    Our <b>Base Foundation Sub-Agents</b> handle the high-fidelity physics (L1-L2), while 
    <b>Strategic Sub-Agents</b> (L3-L4) are stacked on top to target specific business value like ROI and ESG targets.</p>
</div>
""", unsafe_allow_html=True)

# 5. THE STRATEGIC MATRIX (Your Core Interactive Element)
st.markdown("<h2 id='matrix' style='text-align:center;'>Strategic Solution Matrix</h2>", unsafe_allow_html=True)
# ... [Insert the Matrix Code provided in the previous turn here] ...

# 6. CONTACT SECTION
st.markdown("""
<div style="text-align:center; padding:100px 0;">
    <h2 style="color:#F97316;">Ready to Deploy?</h2>
    <p>Join the future of industrial intelligence.</p>
    <br>
    <p style="color:#475569;">Ingenero.AI | Digital Foundations to Strategic Autonomy</p>
</div>
""", unsafe_allow_html=True)
