<<<<<<< HEAD
import streamlit as st

def admin_panel():
    st.title("🛡️ Admin Panel")

    if st.button("View Logs"):
        try:
            with open("activity.log", "r") as f:
                logs = f.read()
            st.text_area("System Logs", logs, height=300)
        except:
=======
import streamlit as st

def admin_panel():
    st.title("🛡️ Admin Panel")

    if st.button("View Logs"):
        try:
            with open("activity.log", "r") as f:
                logs = f.read()
            st.text_area("System Logs", logs, height=300)
        except:
>>>>>>> 937145374ef1cb54abd7cc95f7939691e2e304be
            st.warning("No logs found")