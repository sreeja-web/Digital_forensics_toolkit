import streamlit as st
from report_generator import generate_pdf

def is_suspicious_url(url):
    score = 0
    reasons = []

    if "@" in url:
        score += 1
        reasons.append("Contains '@' symbol (phishing trick)")

    if "-" in url:
        score += 1
        reasons.append("Hyphenated domain (common in fake sites)")

    if "http://" in url:
        score += 1
        reasons.append("Not secure (HTTP)")

    if len(url) > 75:
        score += 1
        reasons.append("Unusually long URL")

    return score, reasons


def url_check_ui():
    st.title("🌐 URL Threat Detector")

    url = st.text_input("Enter URL")

    # Initialize session state
    if "url_score" not in st.session_state:
        st.session_state.url_score = None
        st.session_state.url_reasons = []

    # 🔍 CHECK BUTTON
    if st.button("Check"):
        score, reasons = is_suspicious_url(url)

        st.session_state.url_score = score
        st.session_state.url_reasons = reasons

    # ✅ SHOW RESULTS ONLY IF AVAILABLE
    if st.session_state.url_score is not None:
        score = st.session_state.url_score
        reasons = st.session_state.url_reasons

        st.write("Threat Score:", score)

        if score >= 3:
            st.error("❌ Malicious URL")

            st.subheader("🔍 Detailed Analysis")
            st.write("**Threat Level:** High")
            st.write("**Indicators:**", reasons)
            st.write("**Possible Attack Type:** Phishing / Fake Website")
            st.write("**Risk Explanation:** URL matches known phishing patterns.")
            st.write("**Recommended Action:** Do NOT open the link.")

        elif score == 2:
            st.warning("⚠️ Suspicious URL")

            st.subheader("🔍 Detailed Analysis")
            st.write("**Threat Level:** Medium")
            st.write("**Indicators:**", reasons)
            st.write("**Possible Attack Type:** Suspicious Domain")
            st.write("**Risk Explanation:** Some risk indicators found.")
            st.write("**Recommended Action:** Proceed with caution.")

        else:
            st.success("✅ Safe URL")

            st.subheader("🔍 Detailed Analysis")
            st.write("**Threat Level:** Low")
            st.write("**Indicators:** None")
            st.write("**Risk Explanation:** No suspicious patterns.")
            st.write("**Recommended Action:** Safe to browse.")

        # 📄 PDF REPORT
        report_data = [
            f"URL: {url}",
            f"Threat Score: {score}",
            f"Indicators: {reasons}"
        ]

        if score >= 3:
            report_data += ["Threat Level: High", "Attack Type: Phishing"]
        elif score == 2:
            report_data += ["Threat Level: Medium", "Attack Type: Suspicious URL"]
        else:
            report_data += ["Threat Level: Low", "Status: Safe URL"]

        if st.button("📄 Download Report"):
            generate_pdf("url_report.pdf", "URL Forensics Report", report_data)
            with open("url_report.pdf", "rb") as f:
                st.download_button("Download PDF", f, file_name="url_report.pdf")