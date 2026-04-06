
import streamlit as st
from auth import login_user, signup_user
from file_analyzer import file_analysis_ui
from log_analyzer import log_analysis_ui
from url_checker import url_check_ui
from admin import admin_panel
from logger import log_activity
from profile import profile_ui
from case_management import case_management_ui
from steganography import stego_ui   # ✅ NEW (ADD THIS)

st.set_page_config(page_title="Digital Forensics Toolkit", layout="wide")

# 🎨 CUSTOM THEME
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1D2D44;
    }

    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }

    .stMarkdown, .stText, label {
        color: white !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #F0EBD8 !important;
    }

    section[data-testid="stSidebar"] * {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# SESSION STATE
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# LOGIN / SIGNUP
if not st.session_state.logged_in:
    choice = st.sidebar.selectbox("Login / Signup", ["Login", "Signup"])

    if choice == "Login":
        if login_user():
            st.session_state.logged_in = True
            log_activity("Login success")
            st.rerun()
    else:
        signup_user()

else:
    st.sidebar.success(f"Welcome {st.session_state.username}")

    # ✅ UPDATED SIDEBAR NAVIGATION
    page = st.sidebar.radio(
        "Navigation",
        ["Profile", "Admin Panel", "Modules", "Case Management", "Steganography"]  # ✅ ADDED
    )

    # 🔹 PROFILE
    if page == "Profile":
        profile_ui(st.session_state.username)

    # 🔹 ADMIN PANEL
    elif page == "Admin Panel":
        admin_panel()

    # 🔹 MODULES
    elif page == "Modules":
        menu = st.sidebar.selectbox(
            "Modules",
            ["File Analysis", "Log Analysis", "URL Checker"]
        )

        if menu == "File Analysis":
            file_analysis_ui()

        elif menu == "Log Analysis":
            log_analysis_ui()

        elif menu == "URL Checker":
            url_check_ui()

    # 🔹 CASE MANAGEMENT
    elif page == "Case Management":
        case_management_ui()

    # 🔹 STEGANOGRAPHY (NEW)
    elif page == "Steganography":
        stego_ui()   # ✅ ONLY DECODE LOGIC HANDLED INSIDE THIS FUNCTION

    # LOGOUT BUTTON
    st.sidebar.markdown("---")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
