import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Poonam Dhanuka | Finance & Compliance",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_photo_b64():
    for name in ["poonam_photo.jpg", "poonam_photo.jpeg", "poonam_photo.png"]:
        p = Path(name)
        if p.exists():
            return base64.b64encode(p.read_bytes()).decode()
    return None

photo_b64 = get_photo_b64()
photo_html = (
    f'<img src="data:image/jpeg;base64,{photo_b64}" class="hero-photo" alt="Poonam Dhanuka"/>'
    if photo_b64 else '<div class="hero-photo-placeholder">👤</div>'
)

# ── CSS ──────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [class*="css"] { font-family: 'Inter', system-ui, sans-serif !important; }
.stApp { background: #F0F6FF !important; color: #0F172A !important; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.stDeployButton, [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
:root {
  --navy: #1B3A6B; --blue: #2563EB; --blue2: #3B82F6;
  --light: #F0F6FF; --light2: #E0EDFF; --card: #FFFFFF;
  --text: #0F172A; --muted: #475569; --border: rgba(27,58,107,0.15);
}
.nav {
  background: rgba(240,246,255,0.96); backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--border); padding: 0 6%;
  display: flex; align-items: center; justify-content: space-between;
  height: 62px; position: sticky; top: 0; z-index: 100;
}
.nav-brand { font-size: 1.05rem; font-weight: 900; color: var(--navy); }
.nav-brand span { color: var(--blue); }
.nav-links { display: flex; gap: 24px; list-style: none; }
.nav-links a { color: var(--muted); text-decoration: none; font-size: 0.84rem; font-weight: 500; }
.nav-links a:hover { color: var(--navy); }
.nav-cta { background: var(--navy) !important; color: #fff !important; padding: 7px 18px; border-radius: 7px; }
.hero {
  min-height: 88vh; display: flex; align-items: center;
  padding: 80px 6% 60px;
  background: linear-gradient(135deg, #F0F6FF 0%, #E0EDFF 100%);
}
.hero-inner { display: flex; align-items: center; justify-content: space-between; width: 100%; gap: 60px; }
.hero-left { max-width: 600px; }
.hero-greeting {
  font-size: 0.9rem; color: var(--blue); font-weight: 700;
  letter-spacing: 1px; text-transform: uppercase; margin-bottom: 10px;
}
.hero-name { font-size: clamp(2.4rem,4.5vw,3.6rem); font-weight: 900; color: var(--navy); line-height: 1.08; letter-spacing: -1px; margin-bottom: 12px; }
.hero-title { font-size: 0.95rem; color: var(--muted); margin-bottom: 8px; }
.hero-title strong { color: var(--blue); }
.open-badge {
  display: inline-flex; align-items: center; gap: 7px;
  background: rgba(37,99,235,0.10); border: 1px solid rgba(37,99,235,0.3);
  color: var(--blue); font-size: 0.76rem; font-weight: 700;
  padding: 5px 14px; border-radius: 20px; margin: 10px 0 18px;
}
.open-badge .dot { width: 7px; height: 7px; background: #22c55e; border-radius: 50%; animation: pulse 1.8s ease-in-out infinite; }
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.5;transform:scale(1.4)} }
.hero-bio { font-size: 0.92rem; color: var(--muted); line-height: 1.8; margin-bottom: 28px; max-width: 540px; }
.hero-btns { display: flex; gap: 12px; flex-wrap: wrap; }
.btn-p { background: var(--navy); color: #fff; padding: 12px 26px; border-radius: 9px; text-decoration: none; font-weight: 700; font-size: 0.88rem; }
.btn-o { border: 1.5px solid var(--blue); color: var(--navy); padding: 12px 26px; border-radius: 9px; text-decoration: none; font-weight: 600; font-size: 0.88rem; background: transparent; }
.hero-right { flex-shrink: 0; }
.photo-frame { position: relative; width: 300px; }
.photo-frame::before { content: ''; position: absolute; top: 16px; left: 16px; right: -16px; bottom: -16px; background: var(--light2); border-radius: 24px; z-index: 0; }
.hero-photo { position: relative; z-index: 1; width: 300px; height: 370px; object-fit: cover; object-position: center top; border-radius: 20px; box-shadow: 0 20px 60px rgba(27,58,107,0.2); border: 3px solid rgba(37,99,235,0.2); }
.photo-badge { position: absolute; bottom: -14px; right: 16px; z-index: 3; background: var(--navy); color: #fff; font-size: 0.72rem; font-weight: 700; padding: 7px 14px; border-radius: 20px; box-shadow: 0 4px 14px rgba(27,58,107,0.35); white-space: nowrap; }
.photo-badge2 { position: absolute; top: -14px; left: 10px; z-index: 4; background: var(--blue); color: #fff; font-size: 0.68rem; font-weight: 700; padding: 6px 12px; border-radius: 20px; box-shadow: 0 4px 14px rgba(37,99,235,0.35); white-space: nowrap; }
.sec { padding: 80px 6%; }
.sec-alt { padding: 80px 6%; background: var(--light2); }
.sec-label { font-size: 0.72rem; color: var(--blue); font-weight: 700; letter-spacing: 2.5px; text-transform: uppercase; margin-bottom: 6px; }
.sec-title { font-size: clamp(1.7rem,3vw,2.2rem); font-weight: 800; color: var(--navy); letter-spacing: -0.5px; }
.divider { width: 44px; height: 3px; background: linear-gradient(90deg, var(--navy), var(--blue)); border-radius: 2px; margin: 12px 0 40px; }
.stats-row { display: grid; grid-template-columns: repeat(4,1fr); gap: 14px; margin-bottom: 36px; }
.about-stat { background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 20px 16px; text-align: center; }
.about-stat-num { font-size: 2rem; font-weight: 900; color: var(--navy); }
.about-stat-label { font-size: 0.76rem; color: var(--muted); margin-top: 3px; }
.about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; max-width: 860px; }
.about-p { font-size: 0.92rem; color: var(--muted); line-height: 1.82; margin-bottom: 14px; }
.tl { position: relative; padding-left: 32px; max-width: 820px; }
.tl::before { content: ''; position: absolute; left: 8px; top: 6px; bottom: 0; width: 2px; background: linear-gradient(180deg, var(--navy) 0%, rgba(27,58,107,0.1) 100%); }
.tl-item { position: relative; margin-bottom: 44px; }
.tl-dot { position: absolute; left: -30px; top: 18px; width: 14px; height: 14px; border-radius: 50%; background: var(--navy); border: 2.5px solid var(--light); box-shadow: 0 0 0 3px rgba(27,58,107,0.2); }
.tl-head { display: flex; align-items: flex-start; gap: 14px; margin-bottom: 10px; }
.tl-icon { width: 44px; height: 44px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; flex-shrink: 0; }
.tl-co { font-size: 0.7rem; color: var(--blue); font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 3px; }
.tl-role { font-size: 1.02rem; font-weight: 800; color: var(--navy); margin-bottom: 3px; }
.tl-date { font-size: 0.74rem; color: var(--muted); background: rgba(27,58,107,0.08); border: 1px solid var(--border); padding: 3px 10px; border-radius: 20px; display: inline-block; margin-bottom: 3px; }
.tl-loc { font-size: 0.78rem; color: #94A3B8; }
.cur { display: inline-block; background: rgba(34,197,94,0.1); border: 1px solid rgba(34,197,94,0.3); color: #16a34a; font-size: 0.67rem; font-weight: 700; padding: 2px 9px; border-radius: 10px; margin-left: 8px; }
.tl-desc { font-size: 0.86rem; color: var(--muted); line-height: 1.75; padding-left: 14px; margin: 10px 0; }
.tl-desc li { margin-bottom: 5px; }
.tl-desc li strong { color: var(--blue); }
.tl-tag { display: inline-block; background: rgba(27,58,107,0.08); border: 1px solid rgba(27,58,107,0.18); color: var(--blue); font-size: 0.7rem; padding: 3px 10px; border-radius: 10px; margin: 3px 3px 0 0; }
.edu-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px,1fr)); gap: 18px; }
.edu-card { background: var(--card); border: 1px solid var(--border); border-radius: 16px; padding: 26px 24px; transition: border-color 0.2s, transform 0.2s; }
.edu-card:hover { border-color: var(--blue); transform: translateY(-3px); }
.edu-icon { font-size: 1.8rem; margin-bottom: 12px; }
.edu-school { font-size: 0.7rem; color: var(--blue); font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 5px; }
.edu-degree { font-size: 0.98rem; font-weight: 700; color: var(--navy); margin-bottom: 4px; }
.edu-detail { font-size: 0.8rem; color: var(--muted); line-height: 1.6; }
.edu-gpa { display: inline-block; margin-top: 12px; background: rgba(37,99,235,0.10); border: 1px solid rgba(37,99,235,0.3); color: var(--blue); font-size: 0.76rem; font-weight: 700; padding: 4px 12px; border-radius: 10px; }
.sk-grid { display: grid; grid-template-columns: repeat(auto-fit,minmax(230px,1fr)); gap: 18px; }
.sk-cat { background: var(--card); border: 1px solid var(--border); border-radius: 16px; padding: 24px 22px; }
.sk-cat:hover { border-color: var(--blue); }
.sk-title { font-size: 0.76rem; font-weight: 700; color: var(--navy); letter-spacing: 1px; text-transform: uppercase; margin-bottom: 14px; }
.sk-pill { display: inline-flex; align-items: center; gap: 5px; background: rgba(224,237,255,0.8); border: 1px solid var(--border); color: var(--blue); font-size: 0.79rem; padding: 5px 12px; border-radius: 20px; margin: 4px 4px 0 0; }
.proj-grid { display: grid; grid-template-columns: repeat(auto-fit,minmax(300px,1fr)); gap: 22px; }
.proj-card { background: var(--card); border: 1px solid var(--border); border-radius: 18px; overflow: hidden; display: flex; flex-direction: column; }
.proj-card:hover { border-color: var(--blue); transform: translateY(-4px); box-shadow: 0 12px 40px rgba(27,58,107,0.13); }
.proj-hdr { height: 130px; display: flex; align-items: center; justify-content: center; font-size: 3rem; position: relative; overflow: hidden; }
.proj-body { padding: 24px; flex: 1; display: flex; flex-direction: column; }
.proj-type { font-size: 0.68rem; color: var(--blue); font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 8px; }
.proj-title { font-size: 1.06rem; font-weight: 800; color: var(--navy); margin-bottom: 10px; }
.proj-desc { font-size: 0.84rem; color: var(--muted); line-height: 1.72; flex: 1; }
.proj-tech { margin-top: 14px; }
.proj-tech span { display: inline-block; background: rgba(27,58,107,0.08); border: 1px solid rgba(27,58,107,0.16); color: var(--blue); font-size: 0.7rem; padding: 3px 9px; border-radius: 10px; margin: 3px 3px 0 0; }
.proj-link { display: inline-flex; align-items: center; gap: 6px; color: var(--navy); font-size: 0.82rem; font-weight: 600; text-decoration: none; margin-top: 16px; }
.proj-link:hover { color: var(--blue); }
.cert-grid { display: grid; grid-template-columns: repeat(auto-fit,minmax(250px,1fr)); gap: 14px; }
.cert-card { background: var(--card); border: 1px solid var(--border); border-radius: 13px; padding: 18px 20px; display: flex; align-items: flex-start; gap: 14px; }
.cert-card:hover { border-color: var(--blue); }
.cert-icon { font-size: 1.6rem; flex-shrink: 0; }
.cert-name { font-size: 0.9rem; font-weight: 700; color: var(--navy); margin-bottom: 3px; }
.cert-issuer { font-size: 0.76rem; color: var(--muted); }
.contact-wrap { text-align: center; }
.contact-email { font-size: 1.2rem; font-weight: 700; color: var(--navy); text-decoration: none; display: inline-block; margin: 16px 0 26px; border-bottom: 2px solid rgba(27,58,107,0.25); padding-bottom: 3px; }
.soc-links { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
.soc-link { background: var(--card); border: 1px solid var(--border); color: var(--blue); padding: 11px 22px; border-radius: 10px; text-decoration: none; font-size: 0.84rem; font-weight: 600; display: flex; align-items: center; gap: 7px; }
.soc-link:hover { background: var(--navy); color: #fff; }
.footer { background: linear-gradient(135deg, #1B3A6B 0%, #2563EB 100%); color: rgba(255,255,255,0.85); text-align: center; padding: 20px 6%; font-size: 0.78rem; }
.footer strong { color: #fff; }
</style>
""", unsafe_allow_html=True)

# ── NAV ──────────────────────────────────────────────────────────
st.markdown('<div class="nav"><div class="nav-brand">Poonam <span>Dhanuka</span></div><ul class="nav-links"><li><a href="#about">About</a></li><li><a href="#experience">Experience</a></li><li><a href="#education">Education</a></li><li><a href="#projects">Projects</a></li><li><a href="#contact" class="nav-cta">Contact</a></li></ul></div>', unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────
st.markdown(f"""<div class="hero" id="home"><div class="hero-inner"><div class="hero-left">
<div class="hero-greeting">Hi, I'm</div>
<h1 class="hero-name">Poonam Dhanuka</h1>
<p class="hero-title"><strong>MS Finance · DePaul University</strong> &nbsp;·&nbsp; Company Secretary (ICSI) &nbsp;·&nbsp; Finance &amp; Compliance Professional</p>
<div class="open-badge"><span class="dot"></span> Open to Work · Chicago, IL</div>
<p class="hero-bio">Finance professional with 6+ years across compliance risk, corporate governance, and regulatory intelligence. Collaborated with PwC &amp; Deloitte, led organization-wide compliance assessments, and represented companies before the NCLT. Now at DePaul (GPA 3.8), bridging deep regulatory expertise with financial modeling and capital markets.</p>
<div class="hero-btns"><a href="mailto:pdhanuka@depaul.edu" class="btn-p">Get in Touch →</a>&nbsp;<a href="https://www.linkedin.com/in/poonam-dhanuka/" target="_blank" class="btn-o">LinkedIn Profile</a></div>
</div><div class="hero-right"><div class="photo-frame">{photo_html}<div class="photo-badge">🏆 GPA 3.8 · DePaul MSF</div><div class="photo-badge2">✅ Company Secretary · ICSI</div></div></div>
</div></div>""", unsafe_allow_html=True)

# ── ABOUT ────────────────────────────────────────────────────────
st.markdown('<div class="sec-alt" id="about"><div class="sec-label">About Me</div><h2 class="sec-title">Where Governance Meets Finance</h2><div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="stats-row"><div class="about-stat"><div class="about-stat-num">6+</div><div class="about-stat-label">Years Experience</div></div><div class="about-stat"><div class="about-stat-num">3.8</div><div class="about-stat-label">GPA · DePaul MSF</div></div><div class="about-stat"><div class="about-stat-num">3</div><div class="about-stat-label">Countries Worked</div></div><div class="about-stat"><div class="about-stat-num">Big 4</div><div class="about-stat-label">PwC &amp; Deloitte</div></div></div>', unsafe_allow_html=True)
st.markdown('<div class="about-grid"><div><p class="about-p">Finance professional with 6+ years spanning compliance risk, corporate governance, and regulatory intelligence across India\'s NBFC and listed-company sectors. Led organization-wide compliance assessments, collaborated with Big Four firms (PwC &amp; Deloitte), represented companies before the NCLT, and coordinated directly with RBI officials during annual inspections.</p><p class="about-p">Cross-border experience includes serving as SPOC for group companies in the USA, Canada, and Sri Lanka, and leading a greenfield university project in Jaffna, Sri Lanka from concept to BOI approval.</p></div><div><p class="about-p">Now at DePaul\'s Kellstadt Graduate School of Business (GPA 3.8), bridging deep regulatory expertise with financial modeling, valuation, and capital markets. Currently serving as <strong style="color:var(--blue)">Student Assistant at DePaul\'s Business Advising Office</strong>, supporting 15 advisors and hundreds of students daily.</p><p class="about-p">Actively seeking <strong style="color:var(--blue)">Finance, Risk, Compliance, or Corporate Finance</strong> roles, on-site or hybrid, in Chicago.</p></div></div></div>', unsafe_allow_html=True)

# ── EDUCATION ────────────────────────────────────────────────────
st.markdown('<div class="sec" id="education"><div class="sec-label">Education</div><h2 class="sec-title">Academic Background</h2><div class="divider"></div><div class="edu-grid">', unsafe_allow_html=True)
st.markdown('<div class="edu-card"><div class="edu-icon">🎓</div><div class="edu-school">DePaul University · Kellstadt Graduate School of Business</div><div class="edu-degree">Master of Science in Finance (MSF)</div><div class="edu-detail">Chicago, Illinois · Expected June 2027</div><div class="edu-detail" style="margin-top:8px">Financial Management · Investment Analysis · Advanced Corporate Finance · Financial Statement Analysis · International Finance</div><div class="edu-gpa">GPA: 3.8 / 4.0</div></div>', unsafe_allow_html=True)
st.markdown('<div class="edu-card"><div class="edu-icon">⚖️</div><div class="edu-school">Institute of Company Secretaries of India (ICSI)</div><div class="edu-degree">Company Secretary (CS) · Associate Member</div><div class="edu-detail">Qualified January 2016</div><div class="edu-detail" style="margin-top:8px">Companies Act · SEBI Regulations · Corporate Governance · Tax Law · FEMA · M&amp;A</div></div>', unsafe_allow_html=True)
st.markdown('<div class="edu-card"><div class="edu-icon">🏫</div><div class="edu-school">Rajasthan University</div><div class="edu-degree">Bachelor of Business Administration (BBA)</div><div class="edu-detail">Jaipur, India · June 2011</div></div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── EXPERIENCE ───────────────────────────────────────────────────
st.markdown('<div class="sec-alt" id="experience"><div class="sec-label">Experience</div><h2 class="sec-title">Professional Journey</h2><div class="divider"></div><div class="tl">', unsafe_allow_html=True)

# Role 1
st.markdown('<div class="tl-item"><div class="tl-dot"></div><div class="tl-head"><div class="tl-icon" style="background:linear-gradient(135deg,#1B3A6B,#2563EB)">🎓</div><div><div class="tl-co">DePaul University · Business Advising Office</div><div class="tl-role">Student Assistant <span class="cur">● CURRENT</span></div><div class="tl-date">June 2026 – Present</div><div class="tl-loc">📍 Chicago, IL</div></div></div>', unsafe_allow_html=True)
st.markdown('<ul class="tl-desc"><li>Manage calendars of <strong>15 academic advisors</strong>, coordinating appointments for undergraduate and graduate students.</li><li>Serve as primary front-desk representative: enrollment, course selection, Campus Connect issues, probation policies, and academic concerns.</li><li>Support planning and execution of advising events, workshops, and student engagement activities.</li><li>Troubleshoot student issues by coordinating with Registrar, Financial Aid, and departmental teams.</li></ul><div><span class="tl-tag">Academic Advising</span><span class="tl-tag">Student Services</span><span class="tl-tag">Calendar Management</span><span class="tl-tag">Cross-functional Coordination</span></div></div>', unsafe_allow_html=True)

# Role 2
st.markdown('<div class="tl-item"><div class="tl-dot"></div><div class="tl-head"><div class="tl-icon" style="background:linear-gradient(135deg,#0f2a5c,#1B3A6B)">🏦</div><div><div class="tl-co">TVS Credit Services Limited · NBFC</div><div class="tl-role">Compliance Risk Analyst</div><div class="tl-date">Feb 2023 – May 2024</div><div class="tl-loc">📍 Chennai, India</div></div></div>', unsafe_allow_html=True)
st.markdown('<ul class="tl-desc"><li>Led company\'s <strong>first-ever organization-wide Compliance Risk Assessment</strong> across 40+ departments.</li><li>Monitored <strong>RBI, SEBI, MCA</strong> regulatory updates; translated complex regulations into actionable leadership guidance.</li><li>Served as <strong>Scrum Master</strong> for Monthly Compliance Report, presented directly to CEO and senior leadership.</li><li>Collaborated with <strong>Deloitte on ESG implementation</strong>: carbon surveys, stakeholder assessments, framework alignment.</li><li>Key role in <strong>RBI Annual Inspection</strong>, coordinating with RBI officials for 20 working days.</li></ul><div><span class="tl-tag">RBI Compliance</span><span class="tl-tag">Risk Assessment</span><span class="tl-tag">ESG · Deloitte</span><span class="tl-tag">Scrum Master</span></div></div>', unsafe_allow_html=True)

# Role 3
st.markdown('<div class="tl-item"><div class="tl-dot"></div><div class="tl-head"><div class="tl-icon" style="background:linear-gradient(135deg,#1B3A6B,#2563EB)">🌐</div><div><div class="tl-co">Magick Woods Exports Pvt Ltd · BSE-Listed</div><div class="tl-role">Corporate Governance Analyst</div><div class="tl-date">July 2020 – Feb 2023</div><div class="tl-loc">📍 Chennai, India</div></div></div>', unsafe_allow_html=True)
st.markdown('<ul class="tl-desc"><li>Collaborated with <strong>PwC</strong> on compliance case, representing company before the <strong>NCLT</strong>, successfully reducing a significant penalty.</li><li>Served as <strong>SPOC</strong> for group companies in the USA, Canada, and Sri Lanka.</li><li>Led the <strong>Sri Lanka University Project</strong>: CEO collaboration, BOI coordination, site visits, land lease negotiation, financial projections.</li><li>Prepared annual financial reports; signed off as Compliance Officer.</li></ul><div><span class="tl-tag">SEBI / LODR</span><span class="tl-tag">NCLT · PwC</span><span class="tl-tag">Cross-border Compliance</span><span class="tl-tag">Corporate Governance</span></div></div>', unsafe_allow_html=True)

# Role 4
st.markdown('<div class="tl-item"><div class="tl-dot"></div><div class="tl-head"><div class="tl-icon" style="background:linear-gradient(135deg,#2563EB,#60A5FA)">📋</div><div><div class="tl-co">Shri Kalyan Holdings Limited</div><div class="tl-role">Corporate Governance Associate</div><div class="tl-date">April 2017 – Jan 2019</div><div class="tl-loc">📍 Jaipur, India</div></div></div>', unsafe_allow_html=True)
st.markdown('<ul class="tl-desc"><li>Supported internal audits across <strong>10+ business units</strong>, contributing to a <strong>15% reduction in audit findings</strong>.</li><li>Prepared risk summaries and compliance briefs for senior leadership.</li></ul><div><span class="tl-tag">Internal Audit</span><span class="tl-tag">Risk Reporting</span><span class="tl-tag">Compliance Documentation</span></div></div>', unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# ── SKILLS ───────────────────────────────────────────────────────
st.markdown('<div class="sec" id="skills"><div class="sec-label">Skills</div><h2 class="sec-title">Core Competencies</h2><div class="divider"></div><div class="sk-grid">', unsafe_allow_html=True)
st.markdown('<div class="sk-cat"><div class="sk-title">📊 Finance &amp; Valuation</div><span class="sk-pill">💹 Financial Modeling</span><span class="sk-pill">📉 DCF Valuation</span><span class="sk-pill">⚖️ WACC / CAPM</span><span class="sk-pill">🏦 Capital Budgeting</span><span class="sk-pill">📈 Investment Analysis</span><span class="sk-pill">🎯 Scenario Modeling</span></div>', unsafe_allow_html=True)
st.markdown('<div class="sk-cat"><div class="sk-title">⚖️ Compliance &amp; Governance</div><span class="sk-pill">📋 SEBI / LODR</span><span class="sk-pill">🏛️ RBI Regulations</span><span class="sk-pill">📜 Companies Act 2013</span><span class="sk-pill">🔍 Compliance Risk</span><span class="sk-pill">🌱 ESG Reporting</span><span class="sk-pill">⚖️ NCLT Proceedings</span></div>', unsafe_allow_html=True)
st.markdown('<div class="sk-cat"><div class="sk-title">💻 Technical Tools</div><span class="sk-pill">🐍 Python</span><span class="sk-pill">⚡ Streamlit</span><span class="sk-pill">📊 Excel (Advanced)</span><span class="sk-pill">📡 Bloomberg Terminal</span><span class="sk-pill">📉 Plotly / Pandas</span><span class="sk-pill">🖥️ Complinity</span></div>', unsafe_allow_html=True)
st.markdown('<div class="sk-cat"><div class="sk-title">🤝 Leadership</div><span class="sk-pill">👥 Cross-functional Leadership</span><span class="sk-pill">🔄 Scrum / Project Mgmt</span><span class="sk-pill">🤝 Stakeholder Management</span><span class="sk-pill">📣 Public Relations</span><span class="sk-pill">✍️ Report Writing</span></div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── PROJECTS ─────────────────────────────────────────────────────
st.markdown('<div class="sec-alt" id="projects"><div class="sec-label">Projects</div><h2 class="sec-title">What I\'ve Built</h2><div class="divider"></div><div class="proj-grid">', unsafe_allow_html=True)

st.markdown('<div class="proj-card"><div class="proj-hdr" style="background:linear-gradient(135deg,#1B3A6B,#2563EB)">📈</div><div class="proj-body"><div class="proj-type">Finance · Data · Python</div><div class="proj-title">StockPro: Interactive Stock Dashboard</div><div class="proj-desc">Full-stack equity research platform with <strong>14 analytical modules</strong> covering the entire investment workflow. Candlestick charts, RSI/MACD, Monte Carlo simulation, stock screener, market sentiment analysis and more.</div><div class="proj-tech"><span>Python</span><span>Streamlit</span><span>yfinance</span><span>Plotly</span><span>Pandas</span><span>scikit-learn</span></div><a href="https://stock-dashboard-ufsydgw6ksqw2t5rmjmpn7.streamlit.app/" target="_blank" class="proj-link">View Live App →</a></div></div>', unsafe_allow_html=True)
st.markdown('<div class="proj-card"><div class="proj-hdr" style="background:linear-gradient(135deg,#0f2a5c,#1B3A6B)">💹</div><div class="proj-body"><div class="proj-type">Valuation · DCF · Finance</div><div class="proj-title">Universal DCF Valuation Model</div><div class="proj-desc">Institutional-grade DCF engine for any public company. Auto-fetches live financials, runs dual terminal value methods (Gordon Growth + Exit Multiple), blended fair value verdict, WACC/CAPM calculator, sensitivity matrix, and 4-sheet Excel export.</div><div class="proj-tech"><span>Python</span><span>Streamlit</span><span>yfinance</span><span>Plotly</span><span>openpyxl</span><span>DCF · WACC</span></div><a href="https://stock-dashboards-kz3rk9k8co9bnu7sl5gsse.streamlit.app/" target="_blank" class="proj-link">View Live App →</a></div></div>', unsafe_allow_html=True)
st.markdown('<div class="proj-card"><div class="proj-hdr" style="background:linear-gradient(135deg,#2563EB,#60A5FA)">🏆</div><div class="proj-body"><div class="proj-type">Case Competition · Strategy</div><div class="proj-title">DePaul Graduate Case Competition</div><div class="proj-desc">Participated in DePaul\'s Graduate Case Competition: Business for Social Good. Analyzed a real-world business case, evaluated strategic options, and presented findings before judges, including live Q&amp;A.</div><div class="proj-tech"><span>Strategic Analysis</span><span>Financial Modeling</span><span>Presentation</span></div></div></div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── CERTIFICATIONS ───────────────────────────────────────────────
st.markdown('<div class="sec" id="certifications"><div class="sec-label">Certifications &amp; Activities</div><h2 class="sec-title">Credentials</h2><div class="divider"></div><div class="cert-grid">', unsafe_allow_html=True)
st.markdown('<div class="cert-card"><div class="cert-icon">⚖️</div><div><div class="cert-name">Associate Member, Company Secretary</div><div class="cert-issuer">ICSI · Jan 2016</div></div></div>', unsafe_allow_html=True)
st.markdown('<div class="cert-card"><div class="cert-icon">📐</div><div><div class="cert-name">Financial Modeling &amp; Valuation</div><div class="cert-issuer">Professional Certification</div></div></div>', unsafe_allow_html=True)
st.markdown('<div class="cert-card"><div class="cert-icon">📊</div><div><div class="cert-name">Bloomberg Finance Fundamentals</div><div class="cert-issuer">Bloomberg for Education · 2025</div></div></div>', unsafe_allow_html=True)
st.markdown('<div class="cert-card"><div class="cert-icon">🌐</div><div><div class="cert-name">Bloomberg Market Concepts (BMC)</div><div class="cert-issuer">Bloomberg for Education</div></div></div>', unsafe_allow_html=True)
st.markdown('<div class="cert-card"><div class="cert-icon">🎙️</div><div><div class="cert-name">Director of Public Relations, KFA</div><div class="cert-issuer">Kellstadt Finance Association · 2025–Present</div></div></div>', unsafe_allow_html=True)
st.markdown('<div class="cert-card"><div class="cert-icon">🏆</div><div><div class="cert-name">Graduate Case Competition</div><div class="cert-issuer">DePaul University · 2025</div></div></div>', unsafe_allow_html=True)
st.markdown('<div class="cert-card"><div class="cert-icon">🏙️</div><div><div class="cert-name">Spring Break Career Treks</div><div class="cert-issuer">McDonald\'s · Exelon · CBRE · Wintrust · Aon · JLL</div></div></div>', unsafe_allow_html=True)
st.markdown('<div class="cert-card"><div class="cert-icon">🤝</div><div><div class="cert-name">Registered Volunteer, CPS</div><div class="cert-issuer">Chicago Public Schools · Jan 2026–Present</div></div></div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ── CONTACT ──────────────────────────────────────────────────────
st.markdown('<div class="sec-alt" id="contact"><div class="contact-wrap"><div class="sec-label" style="text-align:center">Contact</div><h2 class="sec-title" style="text-align:center">Let\'s Connect</h2><div class="divider" style="margin:12px auto 20px"></div><p style="font-size:0.92rem;color:var(--muted);max-width:400px;margin:0 auto 10px">Open to Finance, Risk, Compliance and Corporate Finance roles in Chicago, on-site or hybrid.</p><a href="mailto:pdhanuka@depaul.edu" class="contact-email">pdhanuka@depaul.edu</a><div class="soc-links"><a href="https://www.linkedin.com/in/poonam-dhanuka/" target="_blank" class="soc-link">🔗 LinkedIn</a><a href="https://stock-dashboard-ufsydgw6ksqw2t5rmjmpn7.streamlit.app/" target="_blank" class="soc-link">📈 Stock Dashboard</a><a href="https://stock-dashboards-kz3rk9k8co9bnu7sl5gsse.streamlit.app/" target="_blank" class="soc-link">💹 DCF Model</a><a href="tel:3126722460" class="soc-link">📞 (312) 672-2460</a></div></div></div>', unsafe_allow_html=True)

# ── FOOTER ───────────────────────────────────────────────────────
st.markdown('<div class="footer"><p>© 2026 <strong>Poonam Dhanuka</strong> &nbsp;·&nbsp; Chicago, IL &nbsp;·&nbsp; MS Finance · DePaul University</p></div>', unsafe_allow_html=True)
