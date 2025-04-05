import streamlit as st
import time

ascii_banner = r"""
 __  __       _                            _   _       _     _       
|  \/  | __ _| | _____ _ __ ___   ___  ___| |_| |__   (_)___| |_ ___ 
| |\/| |/ _` | |/ / _ \ '_ ` _ \ / _ \/ __| __| '_ \  | / __| __/ __|
| |  | | (_| |   <  __/ | | | | |  __/\__ \ |_| | | | | \__ \ |_\__ \
|_|  |_|\__,_|_|\_\___|_| |_| |_|\___||___/\__|_| |_| |_|___/\__|___/
"""

sections = {
    "Professional Summary": "Dedicated and results-oriented professional with expertise in cloud computing, Windows admin, and cybersecurity. Skilled in designing scalable, secure hybrid cloud solutions. Passionate about innovation and learning.",
    "Experience": (
        "1. AWS Engineer – Directile\n   - Migrated 50+ apps to AWS, built CI/CD pipelines, optimized cloud cost by 20%\n"
        "2. Software Engineer – Touch 365\n   - Developed microservices, full-stack apps, RESTful APIs, led 6-person team\n"
        "3. Cybersecurity Analyst – TheITguys\n   - Improved response time, managed SIEM/EDR, conducted audits\n"
        "4. Software System Designer – REDSTAR\n   - Built systems with Azure, integrated APIs, agile methodology"
    ),
    "Skills & Expertise": (
        "Cloud: AWS, Azure | Automation: PowerShell, Terraform\n"
        "DevOps: Docker, K8s, Jenkins | Programming: Python, Java, C++\n"
        "Web: React, Angular, Node.js | Cybersecurity: SIEM, EDR\n"
        "DB: MySQL, PostgreSQL, DB2"
    ),
    "Education": "CTU Training Solutions – Computer Science Degree\nZeerust Hoërskool – Matric",
    "Certifications": (
        "- CompTIA Network+\n"
        "- Web Dev Bootcamp\n"
        "- Learn Python Masterclass\n"
        "- Ethical Hacking + Social Engineering\n"
        "- Network Hacking Intermediate"
    ),
    "Extracurricular": (
        "EA Software Engineering @ Forage\n- Proposed EA feature, wrote C++ code\n"
        "AIG Cybersecurity Program\n- Analyzed threats, wrote ethical hacking script\n"
        "Verizon Cloud Simulation\n- Built VPN product, tested for cloud-native traits"
    )
}

st.set_page_config(page_title="Mohammed Gulam Asif - CV", layout="centered")
st.markdown(f"""<pre style='font-size: 12px; color: green'>{ascii_banner}</pre>""", unsafe_allow_html=True)

st.title("Interactive CV - Mohammed Gulam Asif")

menu = list(sections.keys())
selection = st.selectbox("Select a section to view:", menu)

with st.spinner("Loading..."):
    time.sleep(1)
    st.subheader(selection)
    st.text(sections[selection])
