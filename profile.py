import streamlit as st
import json

PROFILE_FILE = "profile.json"

def load_profiles():
    try:
        with open(PROFILE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_profiles(data):
    with open(PROFILE_FILE, "w") as f:
        json.dump(data, f)

def profile_ui(username):
    st.title("👤 User Profile")

    profiles = load_profiles()

    if username not in profiles:
        profiles[username] = {
            "email": "",
            "gender": "",
            "dob": "",
            "address": ""
        }

    user_data = profiles[username]

    # View Mode
    if "edit_mode" not in st.session_state:
        st.session_state.edit_mode = False

    if not st.session_state.edit_mode:
        st.subheader("Profile Details")

        st.write("**Username:**", username)
        st.write("**Email:**", user_data["email"])
        st.write("**Gender:**", user_data["gender"])
        st.write("**Date of Birth:**", user_data["dob"])
        st.write("**Address:**", user_data["address"])

        if st.button("✏️ Edit Profile"):
            st.session_state.edit_mode = True
            st.rerun()

    # Edit Mode
    else:
        st.subheader("Edit Profile")

        email = st.text_input("Email", user_data["email"])
        gender = st.selectbox("Gender", ["Male", "Female", "Other"], 
                              index=["Male","Female","Other"].index(user_data["gender"]) 
                              if user_data["gender"] in ["Male","Female","Other"] else 0)

        dob = st.date_input("Date of Birth")
        address = st.text_area("Address", user_data["address"])

        if st.button("Save"):
            profiles[username] = {
                "email": email,
                "gender": gender,
                "dob": str(dob),
                "address": address
            }
            save_profiles(profiles)
            st.success("Profile Updated!")

            st.session_state.edit_mode = False
            st.rerun()