import streamlit as st
import re
from report_generator import generate_pdf

def detect_anomalies(logs):
    suspicious = []

    for line in logs.split("\n"):
        if re.search(r"failed|error|unauthorized|denied", line.lower()):
            suspicious.append(line)

    return suspicious


def log_analysis_ui():
    st.title("📜 Log Analysis Tool")

    logs = st.text_area("Paste system logs here")

    if st.button("Analyze"):
        results = detect_anomalies(logs)

        st.write("### Suspicious Events")
        st.write(results)
                # 📄 PDF REPORT
        report_data = [
            f"Total Suspicious Events: {len(results)}",
            f"Events: {results}"
        ]

        if len(results) > 5:
            report_data += [
                "Threat Level: High",
                "Attack Type: Brute Force"
            ]
        elif len(results) > 0:
            report_data += [
                "Threat Level: Medium",
                "Attack Type: Unauthorized Access"
            ]
        else:
            report_data += [
                "Threat Level: Low",
                "Status: Normal Logs"
            ]

        if st.button("📄 Download Report"):
            generate_pdf("log_report.pdf", "Log Analysis Report", report_data)
            with open("log_report.pdf", "rb") as f:
                st.download_button("Download PDF", f, file_name="log_report.pdf")

        # 🔥 DETAILED REPORT
        if len(results) > 5:
            st.error("⚠️ High Risk Activity")

            st.subheader("🔍 Detailed Analysis")
            st.write("**Threat Level:** High")
            st.write("**Detected Issues:** Multiple failed/unauthorized attempts")
            st.write("**Possible Attack Type:** Brute Force / Intrusion Attempt")
            st.write("**Risk Explanation:** Repeated failures indicate attack pattern.")
            st.write("**Recommended Action:** Block IP, check firewall logs.")

        elif len(results) > 0:
            st.warning("⚠️ Medium Risk Activity")

            st.subheader("🔍 Detailed Analysis")
            st.write("**Threat Level:** Medium")
            st.write("**Detected Issues:** Some suspicious entries")
            st.write("**Possible Attack Type:** Unauthorized Access Attempt")
            st.write("**Risk Explanation:** Irregular system behavior detected.")
            st.write("**Recommended Action:** Monitor system closely.")

        else:
            st.success("✅ No Suspicious Activity")

            st.subheader("🔍 Detailed Analysis")
            st.write("**Threat Level:** Low")
            st.write("**Risk Explanation:** Logs are normal.")
            st.write("**Recommended Action:** No action needed.")