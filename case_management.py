<<<<<<< HEAD
import streamlit as st
import json
import uuid
import os

CASE_FILE = "cases.json"
BIN_FILE = "bin.json"
EVIDENCE_FOLDER = "evidence"

os.makedirs(EVIDENCE_FOLDER, exist_ok=True)

# ---------------- FILE HANDLING ----------------
def load_cases():
    try:
        with open(CASE_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_cases(cases):
    with open(CASE_FILE, "w") as f:
        json.dump(cases, f)

def load_bin():
    try:
        with open(BIN_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_bin(bin_data):
    with open(BIN_FILE, "w") as f:
        json.dump(bin_data, f)


# ---------------- UI ----------------
def case_management_ui():
    st.title("📁 Case Management System")

    cases = load_cases()
    bin_cases = load_bin()

    tab1, tab2 = st.tabs(["➕ Create Case", "📂 View / Manage Cases"])

    # ➕ CREATE CASE
    with tab1:
        st.subheader("Create New Case")

        title = st.text_input("Case Title")
        description = st.text_area("Description")
        status = st.selectbox("Status", ["Open", "In Progress", "Closed"])

        if st.button("Create Case"):
            case = {
                "id": str(uuid.uuid4())[:8],
                "title": title,
                "description": description,
                "status": status,
                "evidence": []
            }
            cases.append(case)
            save_cases(cases)

            st.success(f"Case Created! ID: {case['id']}")

    # 📂 VIEW + MANAGE CASES
    with tab2:
        st.subheader("Manage Cases")

        if not cases:
            st.info("No cases found")
        else:
            for i, case in enumerate(cases):
                st.markdown(f"### 🧾 Case ID: {case['id']}")
                st.write("**Title:**", case["title"])
                st.write("**Description:**", case["description"])
                st.write("**Current Status:**", case["status"])

                # 📎 Upload Evidence
                uploaded_file = st.file_uploader(
                    f"Upload Evidence for Case {case['id']}",
                    key=case['id']
                )

                if uploaded_file:
                    file_path = os.path.join(EVIDENCE_FOLDER, uploaded_file.name)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.read())

                    case["evidence"].append(uploaded_file.name)
                    save_cases(cases)

                    st.success("Evidence uploaded successfully!")

                # 📋 Evidence list
                if case.get("evidence"):
                    st.write("**Evidence Files:**", case["evidence"])

                # 🔄 Status update
                new_status = st.selectbox(
                    f"Update Status for {case['id']}",
                    ["Open", "In Progress", "Closed"],
                    index=["Open", "In Progress", "Closed"].index(case["status"]),
                    key=f"status_{case['id']}"
                )

                # 🆕 ACTION BUTTONS
                col1, col2 = st.columns([3, 1])

                # 💾 SAVE
                with col1:
                    if st.button(f"💾 Save Changes {case['id']}"):
                        cases[i]["status"] = new_status
                        save_cases(cases)
                        st.success(f"Case {case['id']} updated!")

                # 🗑 DELETE → MOVE TO BIN
                with col2:
                    if st.button(f"🗑 Delete", key=f"delete_{case['id']}"):
                        bin_cases.append(case)
                        cases.pop(i)

                        save_cases(cases)
                        save_bin(bin_cases)

                        st.warning(f"Case moved to Bin!")
                        st.rerun()

                st.markdown("---")


# ---------------- BIN UI ----------------
def bin_ui():
    st.title("🗑 Bin (Deleted Cases)")

    bin_cases = load_bin()

    if not bin_cases:
        st.info("Bin is empty")
        return

    for i, case in enumerate(bin_cases):
        st.markdown(f"### 🧾 Case ID: {case['id']}")
        st.write("**Title:**", case["title"])
        st.write("**Status:**", case["status"])

        col1, col2 = st.columns(2)

        # ♻️ RESTORE
        with col1:
            if st.button(f"♻️ Restore {case['id']}", key=f"restore_{case['id']}"):
                cases = load_cases()
                cases.append(case)
                save_cases(cases)

                bin_cases.pop(i)
                save_bin(bin_cases)

                st.success("Case restored!")
                st.rerun()

        # ❌ PERMANENT DELETE
        with col2:
            if st.button(f"❌ Delete Permanently {case['id']}", key=f"perma_{case['id']}"):
                bin_cases.pop(i)
                save_bin(bin_cases)

                st.error("Case permanently deleted!")
                st.rerun()

=======
import streamlit as st
import json
import uuid
import os

CASE_FILE = "cases.json"
BIN_FILE = "bin.json"
EVIDENCE_FOLDER = "evidence"

os.makedirs(EVIDENCE_FOLDER, exist_ok=True)

# ---------------- FILE HANDLING ----------------
def load_cases():
    try:
        with open(CASE_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_cases(cases):
    with open(CASE_FILE, "w") as f:
        json.dump(cases, f)

def load_bin():
    try:
        with open(BIN_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_bin(bin_data):
    with open(BIN_FILE, "w") as f:
        json.dump(bin_data, f)


# ---------------- UI ----------------
def case_management_ui():
    st.title("📁 Case Management System")

    cases = load_cases()
    bin_cases = load_bin()

    tab1, tab2 = st.tabs(["➕ Create Case", "📂 View / Manage Cases"])

    # ➕ CREATE CASE
    with tab1:
        st.subheader("Create New Case")

        title = st.text_input("Case Title")
        description = st.text_area("Description")
        status = st.selectbox("Status", ["Open", "In Progress", "Closed"])

        if st.button("Create Case"):
            case = {
                "id": str(uuid.uuid4())[:8],
                "title": title,
                "description": description,
                "status": status,
                "evidence": []
            }
            cases.append(case)
            save_cases(cases)

            st.success(f"Case Created! ID: {case['id']}")

    # 📂 VIEW + MANAGE CASES
    with tab2:
        st.subheader("Manage Cases")

        if not cases:
            st.info("No cases found")
        else:
            for i, case in enumerate(cases):
                st.markdown(f"### 🧾 Case ID: {case['id']}")
                st.write("**Title:**", case["title"])
                st.write("**Description:**", case["description"])
                st.write("**Current Status:**", case["status"])

                # 📎 Upload Evidence
                uploaded_file = st.file_uploader(
                    f"Upload Evidence for Case {case['id']}",
                    key=case['id']
                )

                if uploaded_file:
                    file_path = os.path.join(EVIDENCE_FOLDER, uploaded_file.name)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.read())

                    case["evidence"].append(uploaded_file.name)
                    save_cases(cases)

                    st.success("Evidence uploaded successfully!")

                # 📋 Evidence list
                if case.get("evidence"):
                    st.write("**Evidence Files:**", case["evidence"])

                # 🔄 Status update
                new_status = st.selectbox(
                    f"Update Status for {case['id']}",
                    ["Open", "In Progress", "Closed"],
                    index=["Open", "In Progress", "Closed"].index(case["status"]),
                    key=f"status_{case['id']}"
                )

                # 🆕 ACTION BUTTONS
                col1, col2 = st.columns([3, 1])

                # 💾 SAVE
                with col1:
                    if st.button(f"💾 Save Changes {case['id']}"):
                        cases[i]["status"] = new_status
                        save_cases(cases)
                        st.success(f"Case {case['id']} updated!")

                # 🗑 DELETE → MOVE TO BIN
                with col2:
                    if st.button(f"🗑 Delete", key=f"delete_{case['id']}"):
                        bin_cases.append(case)
                        cases.pop(i)

                        save_cases(cases)
                        save_bin(bin_cases)

                        st.warning(f"Case moved to Bin!")
                        st.rerun()

                st.markdown("---")


# ---------------- BIN UI ----------------
def bin_ui():
    st.title("🗑 Bin (Deleted Cases)")

    bin_cases = load_bin()

    if not bin_cases:
        st.info("Bin is empty")
        return

    for i, case in enumerate(bin_cases):
        st.markdown(f"### 🧾 Case ID: {case['id']}")
        st.write("**Title:**", case["title"])
        st.write("**Status:**", case["status"])

        col1, col2 = st.columns(2)

        # ♻️ RESTORE
        with col1:
            if st.button(f"♻️ Restore {case['id']}", key=f"restore_{case['id']}"):
                cases = load_cases()
                cases.append(case)
                save_cases(cases)

                bin_cases.pop(i)
                save_bin(bin_cases)

                st.success("Case restored!")
                st.rerun()

        # ❌ PERMANENT DELETE
        with col2:
            if st.button(f"❌ Delete Permanently {case['id']}", key=f"perma_{case['id']}"):
                bin_cases.pop(i)
                save_bin(bin_cases)

                st.error("Case permanently deleted!")
                st.rerun()

>>>>>>> 937145374ef1cb54abd7cc95f7939691e2e304be
        st.markdown("---")