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
    "Professional Summary": (
        "Versatile and results-driven professional with a multidisciplinary background in Network Engineering, Software Development, and Cybersecurity Analysis. "
        "Highly skilled in cloud architecture, full-stack development, and advanced security operations, with a strong foundation in automating workflows, enhancing system performance, and ensuring airtight digital defenses. "
        "Known for strategic problem-solving, adaptability, and a continuous drive to stay ahead of technological trends."
    ),
    "Experience": (
        "**AWS Engineer – Directile | Jun 2024 – Present**\n"
        "- Architected scalable, fault-tolerant infrastructure with AWS EC2, RDS, Auto Scaling, and ELB.\n"
        "- Reduced deployment time by 50% using Terraform and CloudFormation.\n"
        "- Migrated 50+ apps to AWS Cloud with zero downtime.\n"
        "- Saved 20% in cloud spend using AWS Cost Explorer and Trusted Advisor.\n"
        "- Built CI/CD pipelines with CodePipeline & CodeBuild, boosting deployment frequency by 40%.\n"
        "- Strengthened network security via VPC configurations, IAM policies, and compliance enforcement.\n"
        "- Led the deployment of real-time monitoring solutions and implemented infrastructure as code (IaC) best practices.\n\n"

        "**Software Engineer – Touch 365 Business Solutions | Jan 2023 – Dec 2023**\n"
        "- Built microservices architecture to improve scalability and uptime.\n"
        "- Migrated legacy apps to AWS using API Gateway, Lambda, and DynamoDB.\n"
        "- Developed apps in Python, Java, C++ with clean, testable code.\n"
        "- Created REST APIs to enhance healthcare system data flow.\n"
        "- Built a full-stack app using React & Node.js, increasing user engagement by 35%.\n"
        "- Led optimization of system performance via Kafka and AWS tools.\n"
        "- Integrated CI/CD workflows using GitHub Actions, improving code quality and reliability.\n\n"

        "**Cybersecurity Analyst – TheITguys | Jan 2022 – Oct 2024**\n"
        "- Enhanced real-time threat detection with SIEM and EDR tools.\n"
        "- Cut incident response time by 30% and improved SLA compliance by 20%.\n"
        "- Conducted security audits and enforced recommendations.\n"
        "- Investigated and remediated security incidents using advanced forensics.\n"
        "- Managed phishing simulations and end-user security awareness training.\n"
        "- Developed scripts to automate malware analysis and log correlation tasks.\n\n"

        "**Software System Designer – REDSTAR | Present**\n"
        "- Engineered cloud-native solutions with Azure Logic Apps, Functions, and Service Bus.\n"
        "- Integrated and customized off-the-shelf applications.\n"
        "- Applied Juristic Credit principles to system design.\n"
        "- Used NetBeans, SQL, PostgreSQL, DB2 for database development.\n"
        "- Delivered projects using Agile methodologies.\n"
        "- Designed secure APIs for credit and lending platforms, improving transaction efficiency."
    ),
    "Skills & Expertise": (
        "**Networking:** TCP/IP, DNS, DHCP, VPN, Routing & Switching, VLANs, Network Troubleshooting, Wireshark, Cisco Devices, LAN/WAN Design, Load Balancers, Network Security Policies\n"
        "**Cybersecurity:** SIEM (Splunk, AlienVault), EDR, Vulnerability Assessment, Incident Response, Threat Hunting, IDS/IPS, Firewalls, Encryption, Penetration Testing, Risk Assessment, Security Compliance (ISO 27001, NIST)\n"
        "**Cloud Platforms:** AWS (EC2, S3, RDS, IAM, VPC, CloudTrail), Azure (Logic Apps, Functions, AD Integration, Azure Monitor, Defender for Cloud)\n"
        "**Programming & Automation:** Python, JavaScript, Java, C++, PowerShell, Bash, Terraform, Ansible\n"
        "**Web Development:** React, Angular, Node.js, Express, HTML, CSS, RESTful APIs, WebSocket\n"
        "**DevOps & Tools:** Docker, Kubernetes, Jenkins, Git, GitHub Actions, CI/CD Pipelines, CloudFormation, Prometheus, Grafana\n"
        "**Database Management:** MySQL, PostgreSQL, MongoDB, DynamoDB, DB2, Data Modeling"
    ),
    "Education": (
        "🎓 CTU Training Solutions – Computer Science Degree\n"
        "🏫 Zeerust Hoërskool – Matric"
    ),
    "Certifications": (
        "- CompTIA Network+ (Udemy)\n"
        "- Web Development Bootcamp (Udemy)\n"
        "- Learn Python Programming Masterclass (Udemy)\n"
        "- Learn Ethical Hacking from Scratch (Udemy)\n"
        "- Learn Social Engineering from Scratch (Udemy)\n"
        "- Network Hacking Continued: Intermediate to Advanced (Udemy)\n"
        "- AWS Certified Solutions Architect – Associate *(In Progress)*\n"
        "- Microsoft Certified: Azure Fundamentals *(Planned)*"
    ),
    "Extracurricular": (
        "**Electronic Arts Software Engineering Virtual Experience (Forage)**\n"
        "- Proposed features and created C++ class diagrams for EA Sports.\n"
        "- Patched bugs and optimized data structures in a simulated codebase.\n\n"
        "**AIG Shields Up Cybersecurity Simulation (Forage)**\n"
        "- Performed threat analysis and vulnerability research.\n"
        "- Scripted brute-force decryption in Python to simulate ethical hacking.\n\n"
        "**Verizon Cloud Platform Simulation (Forage)**\n"
        "- Designed a VPN product and validated cloud-native traits.\n"
        "- Created a security-focused presentation and command-line testing scripts."
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
st.subheader("Web Developer | Software Developer | Network Engineer | Cybersecurity Analyst")
st.markdown("---")

# Contact info
st.markdown("📧 **Email:** mgulamasif@gmail.com &nbsp;&nbsp; 📍 **Location:** South Africa")
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
