"""
Abrham Mosye Belsty - Personal Portfolio & Interactive AI Showcase
Built with Streamlit, custom Glassmorphism CSS, and Anthropic Claude API.
"""

import streamlit as st

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="Abrham Mosye Belsty | Portfolio",
    page_icon="💻",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. Safe Anthropic Library Import
ANTHROPIC_AVAILABLE = False
try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False


# 3. Custom CSS Injection (Glassmorphic Dark Theme with Gradient Accents)
st.markdown("""
<style>
/* Import Google Font */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Global font & background adjustments */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Hide default streamlit header decoration for cleaner aesthetic */
header[data-testid="stHeader"] {
    background: transparent !important;
}

/* Gradient Title */
.gradient-title {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #4fd1c5 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2.8rem;
    font-weight: 800;
    margin-bottom: 0.2rem;
    line-height: 1.2;
    letter-spacing: -0.02em;
}

.subtitle {
    color: #cbd5e1;
    font-size: 1.25rem;
    font-weight: 400;
    margin-top: 0.25rem;
    margin-bottom: 0.5rem;
}

.badge-tagline {
    display: inline-block;
    background: rgba(102, 126, 234, 0.15);
    border: 1px solid rgba(102, 126, 234, 0.35);
    color: #a5b4fc;
    font-size: 0.85rem;
    font-weight: 600;
    padding: 0.35rem 0.85rem;
    border-radius: 9999px;
    margin-bottom: 1rem;
}

/* Stats counter */
.stat-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    text-align: center;
    padding: 1rem 0.5rem;
    transition: transform 0.2s ease, border-color 0.2s ease;
}

.stat-card:hover {
    transform: translateY(-3px);
    border-color: rgba(102, 126, 234, 0.4);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
}

.stat-number {
    font-size: 2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.1;
}

.stat-label {
    color: #94a3b8;
    font-size: 0.82rem;
    font-weight: 500;
    margin-top: 0.3rem;
}

/* Skill badges */
.skill-category-title {
    color: #e2e8f0;
    font-size: 1.05rem;
    font-weight: 600;
    margin-top: 0.75rem;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.skill-badge {
    display: inline-block;
    padding: 0.4rem 0.95rem;
    margin: 0.25rem 0.2rem;
    border-radius: 50px;
    font-size: 0.85rem;
    font-weight: 500;
    color: #ffffff;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    border: 1px solid rgba(255, 255, 255, 0.15);
}

.skill-badge:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.5);
}

.skill-badge-alt {
    background: linear-gradient(135deg, #4f46e5 0%, #06b6d4 100%);
}

.skill-badge-accent {
    background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);
}

/* Project cards */
.project-card {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 1.5rem;
    margin: 1rem 0 0.5rem 0;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}

.project-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.25);
    border-color: rgba(102, 126, 234, 0.4);
}

.project-title {
    color: #f1f5f9;
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.project-desc {
    color: #94a3b8;
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 0.75rem;
}

.project-tools {
    color: #818cf8;
    font-size: 0.85rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

/* Section headers */
.section-header {
    font-size: 1.8rem;
    font-weight: 700;
    color: #f8fafc;
    margin-top: 2rem;
    margin-bottom: 1.25rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid;
    border-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%) 1;
    display: flex;
    align-items: center;
    gap: 0.6rem;
}

/* Contact info */
.contact-container {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 1.5rem;
    margin-top: 1rem;
}

.contact-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.65rem 0;
    font-size: 1rem;
    color: #e2e8f0;
}

.contact-item a {
    color: #818cf8;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s;
}

.contact-item a:hover {
    color: #a5b4fc;
    text-decoration: underline;
}

/* Divider */
.gradient-divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, #667eea, #764ba2, transparent);
    border: none;
    margin: 2.5rem 0;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    font-size: 0.85rem;
    padding: 2.5rem 0 1rem;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    margin-top: 3.5rem;
}

/* Make Streamlit buttons prettier */
.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.55rem 2rem !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 22px rgba(102, 126, 234, 0.5) !important;
}

/* Link buttons */
.stLinkButton > a {
    background: rgba(102, 126, 234, 0.12) !important;
    border: 1px solid rgba(102, 126, 234, 0.35) !important;
    color: #c7d2fe !important;
    border-radius: 50px !important;
    padding: 0.35rem 1.25rem !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
    text-decoration: none !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
}

.stLinkButton > a:hover {
    background: rgba(102, 126, 234, 0.28) !important;
    transform: translateY(-2px) !important;
    border-color: rgba(102, 126, 234, 0.6) !important;
    color: #ffffff !important;
}

/* Sidebar Custom Styling */
.sidebar-profile {
    text-align: center;
    padding: 0.5rem 0 1rem 0;
}

/* Style the sidebar profile image */
[data-testid="stSidebar"] [data-testid="stImage"] {
    border-radius: 16px;
    overflow: hidden;
    border: 2px solid rgba(102, 126, 234, 0.4);
    box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);
    margin-bottom: 0.75rem;
}

.sidebar-name {
    color: #f8fafc;
    font-weight: 700;
    font-size: 1.2rem;
    margin-bottom: 0.2rem;
}

.sidebar-sub {
    color: #94a3b8;
    font-size: 0.85rem;
    line-height: 1.3;
}

.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.3);
    color: #34d399;
    font-size: 0.78rem;
    font-weight: 600;
    padding: 0.25rem 0.7rem;
    border-radius: 9999px;
    margin-top: 0.75rem;
}

.status-dot {
    width: 7px;
    height: 7px;
    background: #10b981;
    border-radius: 50%;
    box-shadow: 0 0 8px #10b981;
}

/* Demo Result Box */
.demo-result-box {
    background: rgba(102, 126, 234, 0.06);
    border: 1px solid rgba(102, 126, 234, 0.25);
    border-radius: 12px;
    padding: 1.25rem;
    margin-top: 1rem;
    color: #e2e8f0;
}

/* Certificate & License Beast UI Cards */
.cert-grid-card {
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.05) 0%, rgba(15, 23, 42, 0.75) 50%, rgba(102, 126, 234, 0.08) 100%);
    border: 1px solid rgba(102, 126, 234, 0.28);
    border-radius: 20px;
    padding: 1.45rem;
    margin-bottom: 0.6rem;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
}

.cert-grid-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 5px;
    height: 100%;
    background: linear-gradient(180deg, #667eea 0%, #a855f7 50%, #06b6d4 100%);
}

.cert-grid-card:hover {
    transform: translateY(-5px);
    border-color: rgba(102, 126, 234, 0.6);
    box-shadow: 0 14px 40px rgba(102, 126, 234, 0.3);
}

.cert-top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.8rem;
    flex-wrap: wrap;
    gap: 0.4rem;
}

.cert-issuer-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    color: #38bdf8;
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    background: rgba(56, 189, 248, 0.1);
    padding: 0.25rem 0.65rem;
    border-radius: 9999px;
    border: 1px solid rgba(56, 189, 248, 0.25);
}

.cert-verified-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    color: #34d399;
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    background: rgba(16, 185, 129, 0.12);
    padding: 0.25rem 0.65rem;
    border-radius: 9999px;
    border: 1px solid rgba(16, 185, 129, 0.3);
}

.cert-title-text {
    color: #ffffff;
    font-size: 1.25rem;
    font-weight: 800;
    margin-bottom: 0.45rem;
    line-height: 1.3;
    letter-spacing: -0.01em;
}

.cert-program-subtitle {
    color: #a5b4fc;
    font-size: 0.82rem;
    font-weight: 600;
    margin-bottom: 0.6rem;
}

.cert-meta-details {
    color: #94a3b8;
    font-size: 0.82rem;
    line-height: 1.5;
    margin-top: 0.5rem;
    padding-top: 0.5rem;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    display: flex;
    flex-direction: column;
    gap: 0.2rem;
}
</style>
""", unsafe_allow_html=True)


# 4. Custom Sidebar
with st.sidebar:
    st.image("assets/photo.jpg", use_container_width=True)
    st.markdown("""
    <div class="sidebar-profile">
        <div class="sidebar-name">Abrham Mosye Belsty</div>
        <div class="sidebar-sub">4th-Year IT Student<br>Aspiring Prompt Engineer</div>
        <div class="status-pill">
            <span class="status-dot"></span> Open to Collaborations
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📍 Location & Study")
    st.markdown("🏛️ **University of Gondar**  \n🇪🇹 Gondar, Ethiopia")

    st.markdown("### 🔗 Connect")
    st.markdown("""
    - [🐙 GitHub Profile](https://github.com/Laza1996)
    - [💼 LinkedIn Profile](https://linkedin.com/in/abrham-mosye)
    - [✉️ Email Abrham](mailto:abrhammosye232323@gmail.com)
    - [🎬 AI Tool Studio](https://youtube.com/@AIToolStudio.Official)
    - [📖 Story Time](https://youtube.com/@storytime21-12)
    """)

    st.markdown("---")
    st.markdown("### 📄 Quick Resume")
    resume_text = """# Abrham Mosye Belsty
4th-Year Information Technology Student | Aspiring Prompt Engineer
University of Gondar | abrhammosye232323@gmail.com | github.com/Laza1996

SUMMARY:
4th-year IT student passionate about building reliable AI systems, prompt engineering, and full-stack solutions. Experience delivering 2 web applications and 1 cross-platform mobile application.

SKILLS:
- Languages: Python, JavaScript, Dart
- AI/ML: Prompt Engineering, LLM APIs, LightGBM, Machine Learning
- Web: Streamlit, HTML/CSS, Flask
- Mobile: Flutter, Android Fundamentals
- Tools: Git, GitHub, VS Code

VERIFIED LICENSES & CERTIFICATIONS (Udacity Nanodegrees):
1. Artificial Intelligence Fundamentals — Udacity (Feb 2026)
2. Data Analysis Fundamentals — Udacity (Feb 2026)
3. Android Developer Fundamentals — Udacity (Feb 2026)
4. Programming Fundamentals — Udacity (Feb 2026)

PROJECTS:
1. Prompt Techniques Comparison Library (Python, Claude API, OpenAI API)
2. Prompt Evaluation Tool (Python, Streamlit, LLM APIs)
3. Maternal & Neonatal Health Risk System [Final Year Project] (Python, LightGBM, Streamlit, Flutter)
4. Interactive Personal Portfolio Website (Python, Streamlit)
"""
    st.download_button(
        label="📥 Download Resume Summary",
        data=resume_text,
        file_name="Abrham_Mosye_Belsty_Resume.md",
        mime="text/markdown",
        use_container_width=True
    )


# 5. Hero Section
st.markdown('<div class="badge-tagline">🚀 Available for AI & Software Projects</div>', unsafe_allow_html=True)
st.markdown('<div class="gradient-title">Abrham Mosye Belsty</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">4th-Year IT Student | Aspiring Prompt Engineer</div>', unsafe_allow_html=True)
st.markdown('<p style="color: #94a3b8; font-size: 1rem; margin-top: 0.2rem;">🏛️ University of Gondar</p>', unsafe_allow_html=True)

# 6. Quick Stats Counter
st.write("")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">4th</div>
        <div class="stat-label">Year Student</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">4</div>
        <div class="stat-label">Nanodegrees</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">2+</div>
        <div class="stat-label">Websites Built</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">1</div>
        <div class="stat-label">Mobile App</div>
    </div>
    """, unsafe_allow_html=True)
with col5:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">5+</div>
        <div class="stat-label">Tech Stacks</div>
    </div>
    """, unsafe_allow_html=True)


# 7. About Section
st.markdown('<div class="section-header">💡 About Me</div>', unsafe_allow_html=True)
st.markdown("""
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: 1.5rem; line-height: 1.8; color: #cbd5e1; font-size: 1.05rem;">
I am a 4th-year Information Technology student at the <strong>University of Gondar</strong>. I build with Python and I am passionate about prompt engineering to design reliable AI systems. I have built 2 websites and 1 mobile app, and I am continuously expanding my skills in machine learning and AI.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)


# 8. Technical Skills Section
st.markdown('<div class="section-header">🛠️ Technical Skills</div>', unsafe_allow_html=True)

col_s1, col_s2 = st.columns(2)

with col_s1:
    st.markdown('<div class="skill-category-title">💻 Programming</div>', unsafe_allow_html=True)
    st.markdown("""
        <span class="skill-badge">Python</span>
        <span class="skill-badge">JavaScript</span>
        <span class="skill-badge">Dart</span>
    """, unsafe_allow_html=True)

    st.markdown('<div class="skill-category-title">🧠 AI & Machine Learning</div>', unsafe_allow_html=True)
    st.markdown("""
        <span class="skill-badge skill-badge-accent">Prompt Engineering</span>
        <span class="skill-badge skill-badge-accent">LLM APIs</span>
        <span class="skill-badge skill-badge-accent">LightGBM</span>
        <span class="skill-badge skill-badge-accent">Machine Learning</span>
    """, unsafe_allow_html=True)

    st.markdown('<div class="skill-category-title">📱 Mobile Development</div>', unsafe_allow_html=True)
    st.markdown("""
        <span class="skill-badge skill-badge-alt">Flutter</span>
    """, unsafe_allow_html=True)

with col_s2:
    st.markdown('<div class="skill-category-title">🌐 Web Development</div>', unsafe_allow_html=True)
    st.markdown("""
        <span class="skill-badge skill-badge-alt">Streamlit</span>
        <span class="skill-badge skill-badge-alt">HTML/CSS</span>
        <span class="skill-badge skill-badge-alt">Flask</span>
    """, unsafe_allow_html=True)

    st.markdown('<div class="skill-category-title">🔧 Tools & Workflow</div>', unsafe_allow_html=True)
    st.markdown("""
        <span class="skill-badge">Git</span>
        <span class="skill-badge">GitHub</span>
        <span class="skill-badge">VS Code</span>
    """, unsafe_allow_html=True)

st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)


# 9. Featured Projects Section
st.markdown('<div class="section-header">🚀 Featured Projects</div>', unsafe_allow_html=True)

# Project 1: Prompt Techniques Comparison Library
st.markdown("""
<div class="project-card">
    <div class="project-title">1. Prompt Techniques Comparison Library</div>
    <div class="project-desc">
        Compared zero-shot, few-shot, and chain-of-thought prompts on the same tasks and measured accuracy, cost, and latency.
    </div>
    <div class="project-tools">🛠️ Tools: Python, Claude API, OpenAI API</div>
</div>
""", unsafe_allow_html=True)
st.link_button("View on GitHub ↗", "https://github.com/Laza1996/prompt-comparison")

# Project 2: Prompt Evaluation Tool
st.markdown("""
<div class="project-card">
    <div class="project-title">2. Prompt Evaluation Tool</div>
    <div class="project-desc">
        A small tool that lets you test different prompts against a dataset and automatically scores the outputs for relevance, accuracy, and coherence.
    </div>
    <div class="project-tools">🛠️ Tools: Python, Streamlit, LLM APIs</div>
</div>
""", unsafe_allow_html=True)
st.link_button("View on GitHub ↗", "https://github.com/Laza1996/prompt-eval")

# Project 3: Maternal & Neonatal Health Risk System
st.markdown("""
<div class="project-card">
    <div class="project-title">3. Maternal & Neonatal Health Risk System <span style="font-size: 0.8rem; background: rgba(102, 126, 234, 0.2); border: 1px solid rgba(102, 126, 234, 0.4); padding: 0.2rem 0.6rem; border-radius: 9999px; margin-left: 0.5rem; color: #a5b4fc;">Final Year Project</span></div>
    <div class="project-desc">
        An offline-first application and dashboard that predicts maternal and neonatal health risks and helps with emergency referral decisions. Uses ML models trained on clinical data.
    </div>
    <div class="project-tools">🛠️ Tools: Python, LightGBM, Streamlit, Mobile App</div>
</div>
""", unsafe_allow_html=True)
st.link_button("View on GitHub ↗", "https://github.com/Laza1996/maternal-health")

# Project 4: Personal Portfolio Website
st.markdown("""
<div class="project-card">
    <div class="project-title">4. Personal Portfolio Website</div>
    <div class="project-desc">
        This very portfolio — a Streamlit-based interactive site showcasing my work, skills, and a live AI demo.
    </div>
    <div class="project-tools">🛠️ Tools: Python, Streamlit</div>
</div>
""", unsafe_allow_html=True)
st.link_button("View on GitHub ↗", "https://github.com/Laza1996/my-portfolio")

st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)


# 10. Verified Licenses & Certifications Section
st.markdown('<div class="section-header">📜 Verified Licenses & Certifications</div>', unsafe_allow_html=True)
st.markdown("""
<div style="color: #94a3b8; font-size: 0.98rem; margin-bottom: 1.25rem;">
Official Nanodegree Program completions issued by <strong>Udacity (Part of Accenture)</strong>. Each credential is authenticated and verified with an online confirmation link.
</div>
""", unsafe_allow_html=True)

col_cert1, col_cert2 = st.columns(2)

with col_cert1:
    # 1. Artificial Intelligence Fundamentals
    st.markdown("""
    <div class="cert-grid-card">
        <div class="cert-top-bar">
            <span class="cert-issuer-pill">🎓 UDACITY • ACCENTURE</span>
            <span class="cert-verified-pill">✓ VERIFIED</span>
        </div>
        <div class="cert-title-text">🧠 Artificial Intelligence Fundamentals</div>
        <div class="cert-program-subtitle">Nanodegree Program Completion</div>
        <div style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.55; margin-bottom: 0.6rem;">
            Mastered core AI concepts, search algorithms, heuristic problem solving, automated reasoning, and foundation principles of modern AI systems.
        </div>
        <div class="cert-meta-details">
            <div>📅 <strong>Issued:</strong> February 21, 2026</div>
            <div>👤 <strong>Recipient:</strong> Abrham Mosye</div>
            <div>✍️ <strong>Verified by:</strong> Kai Roemmelt, CEO, Udacity</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Verify Credential ↗", "https://www.udacity.com/certificate/e/fae1ab62-0f13-11f1-bdb5-5fad6b598776")

    # 3. Android Developer Fundamentals
    st.markdown("""
    <div class="cert-grid-card">
        <div class="cert-top-bar">
            <span class="cert-issuer-pill">🎓 UDACITY • ACCENTURE</span>
            <span class="cert-verified-pill">✓ VERIFIED</span>
        </div>
        <div class="cert-title-text">📱 Android Developer Fundamentals</div>
        <div class="cert-program-subtitle">Nanodegree Program Completion</div>
        <div style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.55; margin-bottom: 0.6rem;">
            Engineered responsive mobile architectures, lifecycle management, UI layouts, asynchronous background operations, and native mobile services.
        </div>
        <div class="cert-meta-details">
            <div>📅 <strong>Issued:</strong> February 21, 2026</div>
            <div>👤 <strong>Recipient:</strong> Abrham Mosye</div>
            <div>✍️ <strong>Verified by:</strong> Kai Roemmelt, CEO, Udacity</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Verify Credential ↗", "https://www.udacity.com/certificate/e/21ad5450-0f12-11f1-92b2-53db57e9e941")

with col_cert2:
    # 2. Data Analysis Fundamentals
    st.markdown("""
    <div class="cert-grid-card">
        <div class="cert-top-bar">
            <span class="cert-issuer-pill">🎓 UDACITY • ACCENTURE</span>
            <span class="cert-verified-pill">✓ VERIFIED</span>
        </div>
        <div class="cert-title-text">📊 Data Analysis Fundamentals</div>
        <div class="cert-program-subtitle">Nanodegree Program Completion</div>
        <div style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.55; margin-bottom: 0.6rem;">
            Trained in structured data wrangling, exploratory data analysis (EDA), statistical deduction, and data visualization using Python analytical libraries.
        </div>
        <div class="cert-meta-details">
            <div>📅 <strong>Issued:</strong> February 21, 2026</div>
            <div>👤 <strong>Recipient:</strong> Abrham Mosye</div>
            <div>✍️ <strong>Verified by:</strong> Kai Roemmelt, CEO, Udacity</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Verify Credential ↗", "https://www.udacity.com/certificate/e/91580df6-0f15-11f1-8ea7-d3d9fdf6ae47")

    # 4. Programming Fundamentals
    st.markdown("""
    <div class="cert-grid-card">
        <div class="cert-top-bar">
            <span class="cert-issuer-pill">🎓 UDACITY • ACCENTURE</span>
            <span class="cert-verified-pill">✓ VERIFIED</span>
        </div>
        <div class="cert-title-text">💻 Programming Fundamentals</div>
        <div class="cert-program-subtitle">Nanodegree Program Completion</div>
        <div style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.55; margin-bottom: 0.6rem;">
            Established rigorous computer science paradigms, data structures, algorithm design, control flow, modular programming, and debugging standards.
        </div>
        <div class="cert-meta-details">
            <div>📅 <strong>Issued:</strong> February 21, 2026</div>
            <div>👤 <strong>Recipient:</strong> Abrham Mosye</div>
            <div>✍️ <strong>Verified by:</strong> Kai Roemmelt, CEO, Udacity</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Verify Credential ↗", "https://www.udacity.com/certificate/e/790ad740-0f17-11f1-aa50-0b906bcccc04")

st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)


# 11. Live Prompt Demo Section
st.markdown('<div class="section-header">🧪 Try My Prompt</div>', unsafe_allow_html=True)
st.write("See prompt engineering in action! Paste any text below and I'll summarize it in exactly 3 bullet points.")

# Sample presets for quick testing
sample_presets = {
    "Select an example to auto-fill...": "",
    "Healthcare & Maternal Health": (
        "Maternal healthcare in rural clinics faces several bottlenecks including limited specialist access, "
        "delayed emergency referral decisions, and lack of real-time diagnostic triage systems. By deploying "
        "offline-capable machine learning scoring algorithms on lightweight mobile tablets, frontline health "
        "workers can assess vital signs and risk factors instantaneously. Early pilot studies indicate a 35% "
        "reduction in critical intervention delays when health centers receive automated predictive triage alerts."
    ),
    "Prompt Engineering Fundamentals": (
        "Prompt engineering has rapidly transitioned from informal phrasing tricks to a rigorous empirical discipline. "
        "Techniques such as Few-Shot Prompting, Chain-of-Thought (CoT) reasoning, and Self-Consistency decoding "
        "allow practitioners to direct LLM behavior with predictable confidence intervals. Furthermore, combining "
        "declarative system prompts with quantitative evaluation benchmarks ensures that applications remain robust "
        "against hallucinations, format drift, and latency variance across model updates."
    ),
    "Streamlit for Machine Learning UI": (
        "Streamlit transforms data scripts into shareable web apps in minutes without requiring frontend development expertise. "
        "With Python-first declarative syntax, native caching mechanisms via st.cache_data, and responsive component libraries, "
        "data scientists can quickly build internal evaluation tools, interactive prototypes, and production dashboards. "
        "Combined with custom CSS and modern theming, Streamlit enables teams to deliver polished, enterprise-ready user experiences."
    )
}

selected_preset = st.selectbox("💡 Quick Fill with an Example (optional):", list(sample_presets.keys()))

default_text = sample_presets[selected_preset] if selected_preset != "Select an example to auto-fill..." else ""

user_text = st.text_area(
    "Paste your text here:",
    value=default_text,
    height=150,
    placeholder="Paste an article, paragraph, or any text you'd like summarized..."
)

# Optional API Key configuration expander
with st.expander("🔑 Anthropic API Configuration (Optional Override)", expanded=False):
    st.markdown("""
    By default, the app looks for `ANTHROPIC_API_KEY` in `.streamlit/secrets.toml`.
    If you are running this app locally or testing without secrets configured, you can paste an API key below.
    """)
    custom_api_key = st.text_input("Enter Anthropic API Key (optional):", type="password", placeholder="sk-ant-...")

if st.button("✨ Run Prompt", type="primary"):
    if not user_text.strip():
        st.warning("⚠️ Please paste some text into the box above before running the prompt.")
    else:
        # Determine the API key to use
        api_key = None
        if custom_api_key.strip():
            api_key = custom_api_key.strip()
        elif "ANTHROPIC_API_KEY" in st.secrets and st.secrets["ANTHROPIC_API_KEY"] != "your-key-here":
            api_key = st.secrets["ANTHROPIC_API_KEY"]

        # If Anthropic is installed and a real key is present
        if ANTHROPIC_AVAILABLE and api_key:
            try:
                client = anthropic.Anthropic(api_key=api_key)
                with st.spinner("Running prompt..."):
                    reply = client.messages.create(
                        model="claude-sonnet-4-5",
                        max_tokens=500,
                        system="You summarize text in exactly 3 short bullet points. Each bullet should be concise and capture a key insight.",
                        messages=[{"role": "user", "content": user_text}],
                    )
                    st.success("Done!")
                    st.markdown("""
                    <div class="demo-result-box">
                    """, unsafe_allow_html=True)
                    st.markdown(reply.content[0].text)
                    st.markdown("</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")
        elif not ANTHROPIC_AVAILABLE:
            st.error("⚠️ The `anthropic` Python package is not installed. Run `pip install anthropic` to enable live execution.")
        else:
            # API key is still "your-key-here" or missing - provide friendly simulation mode
            st.info("ℹ️ Live Anthropic API key not detected or currently set to placeholder in `.streamlit/secrets.toml`. Running interactive preview simulation:")
            with st.spinner("Simulating prompt execution (3-bullet synthesis)..."):
                # Clean simulated 3-bullet insight demonstration
                sentences = [s.strip() for s in user_text.replace("\n", " ").split(".") if len(s.strip()) > 15]
                b1 = sentences[0] + "." if len(sentences) > 0 else "Primary premise established in the provided text."
                b2 = sentences[len(sentences)//2] + "." if len(sentences) > 1 else "Key operational challenge or technical mechanism identified."
                b3 = sentences[-1] + "." if len(sentences) > 2 else "Final conclusion emphasizing actionable outcomes."

                st.success("Done! (Simulated Prompt Output)")
                st.markdown(f"""
                <div class="demo-result-box">
                    <strong>🎯 System Directive Applied:</strong> <em>"Summarize in exactly 3 short bullet points"</em><br><br>
                    • <strong>Core Focus:</strong> {b1}<br>
                    • <strong>Key Dynamic:</strong> {b2}<br>
                    • <strong>Primary Impact:</strong> {b3}
                </div>
                """, unsafe_allow_html=True)
                st.caption("💡 To connect to live Claude, update `.streamlit/secrets.toml` with your real Anthropic API key or provide it in the configuration expander above.")

st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)


# 12. Contact Section
st.markdown('<div class="section-header">📬 Get In Touch</div>', unsafe_allow_html=True)

st.markdown("""
<div class="contact-container">
    <div class="contact-item">
        <span>📧</span>
        <span>Email: <a href="mailto:abrhammosye232323@gmail.com">abrhammosye232323@gmail.com</a></span>
    </div>
    <div class="contact-item">
        <span>🐙</span>
        <span>GitHub: <a href="https://github.com/Laza1996" target="_blank">github.com/Laza1996</a></span>
    </div>
    <div class="contact-item">
        <span>💼</span>
        <span>LinkedIn: <a href="https://linkedin.com/in/abrham-mosye" target="_blank">linkedin.com/in/abrham-mosye</a></span>
    </div>
    <div class="contact-item">
        <span>🏛️</span>
        <span>University: <strong>University of Gondar</strong> (Department of Information Technology)</span>
    </div>
    <div class="contact-item">
        <span>🎬</span>
        <span>YouTube: <a href="https://youtube.com/@AIToolStudio.Official" target="_blank">@AIToolStudio.Official</a> • <a href="https://youtube.com/@storytime21-12" target="_blank">@storytime21-12</a></span>
    </div>
</div>
""", unsafe_allow_html=True)


# 13. Footer
st.markdown('<div class="footer">© 2026 Abrham Mosye Belsty. Built with ❤️ and Streamlit.</div>', unsafe_allow_html=True)
