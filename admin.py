import streamlit as st

def admin_panel():
    st.title("🛡️ Admin Panel")

    if st.button("View Logs"):
        try:
            with open("activity.log", "r") as f:
                logs = f.read()
            st.text_area("System Logs", logs, height=300)
        except:
            st.warning("No logs found")