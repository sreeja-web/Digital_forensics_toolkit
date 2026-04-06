import streamlit as st
import json
import hashlib

USER_FILE = "users.json"

def load_users():
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_user():
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users = load_users()
        if username in users and users[username] == hash_password(password):
            st.session_state.username = username
            return True
        else:
            st.error("Invalid credentials")

    return False


def signup_user():
    st.subheader("Signup")

    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type="password")

    if st.button("Signup"):
        users = load_users()
        if username in users:
            st.warning("User already exists")
        else:
            users[username] = hash_password(password)
            save_users(users)
            st.success("Account created!")