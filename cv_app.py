import streamlit as st
import time
from datetime import datetime

# ASCII banner (optional)
ascii_banner = r"""
 __  __       _                            _   _       _     _       
|  \/  | __ _| | _____ _ __ ___   ___  ___| |_| |__   (_)___| |_ ___ 
| |\/| |/ _` | |/ / _ \ '_ ` _ \ / _ \/ __| __| '_ \  | / __| __/ __|
| |  | | (_| |   <  __/ | | | | |  __/\__ \ |_| | | | | \__ \ |_\__ \
|_|  |_|\__,_|_|\_\___|_| |_| |_|\___||___/\__|_| |_| |_|___/\__|___/
"""

# Sections
sections = {
    "Professional Summary": "Dedicated and results-oriented professional with expertise in cloud computing, Windows admin, and cybersecurity. Skilled in designing scalable, secure hybrid cloud solutions. Passionate about innovation and learning.",
    "Experience": (
        "1. **AWS Engineer – Directile**\n   - Migrated 50+ apps to AWS, built CI/CD pipelines, optimized cloud cost by 20%\n"
        "2. **Software Engineer – Touch 365**\n   - Developed microservices, full-stack apps, RESTful APIs, led 6-person team\n"
        "3. **Cybersecurity Analyst – TheITguys**\n   - Improved response time, managed SIEM/EDR, conducted audits\n"
        "4. **Software System Designer – REDSTAR**\n   - Built systems with Azure, integrated APIs, agile methodology"
    ),
    "Skills & Expertise": (
        "🖥️ Cloud: AWS, Azure  | ⚙️ Automation: PowerShell, Terraform\n"
        "🚀 DevOps: Docker, K8s, Jenkins  | 👨‍💻 Programming: Python, Java, C++\n"
        "🌐 Web: React, Angular, Node.js | 🔐 Cybersecurity: SIEM, EDR\n"
        "🗄️ DB: MySQL, PostgreSQL, DB2"
    ),
    "Education": "🎓 CTU Training Solutions – Computer Science Degree\n🏫 Zeerust Hoërskool – Matric",
    "Certifications": (
        "- 📜 CompTIA Network+\n"
        "- 💻 Web Dev Bootcamp\n"
        "- 🐍 Learn Python Masterclass\n"
        "- 🛡️ Ethical Hacking + Social Engineering\n"
        "- 🔌 Network Hacking Intermediate"
    ),
    "Extracurricular": (
        "🛠️ EA Software Engineering @ Forage\n- Proposed EA feature, wrote C++ code\n"
        "🔍 AIG Cybersecurity Program\n- Analyzed threats, wrote ethical hacking script\n"
        "☁️ Verizon Cloud Simulation\n- Built VPN product, tested for cloud-native traits"
    )
}

# Streamlit config
st.set_page_config(page_title="Mohammed Gulam Asif - CV", layout="wide")

# Sidebar Navigation
st.sidebar.image("https://avatars.githubusercontent.com/u/9919?s=200&v=4", width=100)  # Optional: Replace with your avatar
st.sidebar.title("Navigation")
section_choice = st.sidebar.radio("Jump to section:", list(sections.keys()))

# Main content
st.markdown(f"<pre style='font-size: 12px; color: green'>{ascii_banner}</pre>", unsafe_allow_html=True)
st.title("Mohammed Gulam Asif")
st.subheader("Web Developer | Software Engineer | Network Engineer")
st.markdown("---")

# Contact info
st.markdown("📧 **Email:** your.email@example.com &nbsp;&nbsp; 📍 **Location:** South Africa")
st.markdown("---")

# Display selected section
with st.spinner("Loading..."):
    time.sleep(0.5)
    st.header(section_choice)
    st.markdown(sections[section_choice], unsafe_allow_html=True)

# Optional: Download CV as PDF (placeholder for actual logic)
st.sidebar.download_button(
    label="📄 Download PDF",
    data="PDF export coming soon!",
    file_name="Mohammed_Gulam_Asif_CV.pdf",
    mime="application/pdf"
)

# Footer
st.markdown("---")
st.markdown(
    f"<div style='text-align: center; color: gray;'>© {datetime.now().year} Mohammed Gulam Asif. All rights reserved.</div>",
    unsafe_allow_html=True
)
