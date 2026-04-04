import streamlit as st
from report_generator import generate_pdf

SUSPICIOUS_KEYWORDS = [
    "virus", "malware", "hack", "trojan", "payload", "keylogger"
]

def analyze_file_content(text):
    score = 0
    found = []

    for word in SUSPICIOUS_KEYWORDS:
        if word in text.lower():
            score += 1
            found.append(word)

    return score, found


def file_analysis_ui():
    st.title("📂 File Forensics Analysis")

    file = st.file_uploader("Upload a text file")

    if file:
        content = file.read().decode("utf-8", errors="ignore")

        score, found = analyze_file_content(content)

        st.write("### Analysis Result")
        st.write("Suspicious keywords found:", found)
        st.write("Threat Score:", score)

        # 🔥 DETAILED REPORT
        if score > 2:
            st.error("⚠️ High Risk File")

            st.subheader("🔍 Detailed Analysis")
            st.write("**Threat Level:** High")
            st.write("**Indicators:**", found)
            st.write("**Possible Attack Type:** Malware Injection / Trojan")
            st.write("**Risk Explanation:** File contains multiple malicious signatures commonly used in cyber attacks.")
            st.write("**Recommended Action:** Do NOT open. Isolate and scan with antivirus.")

        elif score > 0:
            st.warning("⚠️ Medium Risk File")

            st.subheader("🔍 Detailed Analysis")
            st.write("**Threat Level:** Medium")
            st.write("**Indicators:**", found)
            st.write("**Possible Attack Type:** Suspicious Script / Potential Threat")
            st.write("**Risk Explanation:** Some suspicious patterns detected.")
            st.write("**Recommended Action:** Verify source before using.")

        else:
            st.success("✅ Safe File")

            st.subheader("🔍 Detailed Analysis")
            st.write("**Threat Level:** Low")
            st.write("**Indicators:** None")
            st.write("**Risk Explanation:** No suspicious activity detected.")
            st.write("**Recommended Action:** File is safe to use.")
            # 📄 PDF REPORT
        report_data = [
            f"Threat Score: {score}",
            f"Indicators: {found}"
        ]

        if score > 2:
            report_data += [
                "Threat Level: High",
                "Attack Type: Malware/Trojan",
                "Action: Do NOT open file"
            ]
        elif score > 0:
            report_data += [
                "Threat Level: Medium",
                "Attack Type: Suspicious Script",
                "Action: Verify before use"
            ]
        else:
            report_data += [
                "Threat Level: Low",
                "Status: Safe File"
            ]

        if st.button("📄 Download Report"):
            generate_pdf("file_report.pdf", "File Forensics Report", report_data)
            with open("file_report.pdf", "rb") as f:
                st.download_button("Download PDF", f, file_name="file_report.pdf")