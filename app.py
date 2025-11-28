import streamlit as st

st.set_page_config(page_title="Digital Resolution Hub", layout="wide")

st.title("📱 Digital Resolution Hub")
st.write("Select an issue type below to view the resolution process.")

# --- DATA STORE ---
issues = {
    "Forgot Password": {
        "steps": """1. Go to App login screen → Tap 'Forgot Password'
2. Enter ID number
3. Confirm OTP
4. Reset password and confirm login""",
        "time": "5 mins",
        "escalate": "OTP not received after 3 attempts",
        "tools": "Internet banking & App"
    },

    "Forgot all login credentials": {
        "steps": """1. Go to App login screen → Tap 'Forgot all login credentials'
2. Verify ID number
3. Reset username & password via OTP
4. Confirm login""",
        "time": "6 mins",
        "escalate": "Verification fails 3 times",
        "tools": "App"
    },

    "Pin Blocked": {
        "steps": """1. Open app → Select 'Unblock PIN'
2. Validate ID & DOB
3. Confirm OTP
4. Set new PIN""",
        "time": "3 mins",
        "escalate": "App unresponsive or validation fails",
        "tools": "Internet banking"
    },

    "Sim Override (For Branch)": {
        "steps": """1. Verify ID number
2. Use self-service device change portal
3. Confirm via OTP""",
        "time": "10 mins",
        "escalate": "ID mismatch or OTP fails",
        "tools": "-"
    },

    "App Slow Response": {
        "steps": """1. Clear app cache
2. Restart device
3. If issue persists, escalate to technical support""",
        "time": "5 mins",
        "escalate": "Issue persists after cache clear & restart",
        "tools": "Client's device (Help navigate)"
    },

    "Unable to Register (Profile deleted)": {
        "steps": """1. Confirm if account is deleted
2. Guide client to re-register
3. Assist with verification via OTP""",
        "time": "8 mins",
        "escalate": "Database mismatch or account not found",
        "tools": "-"
    },

    "Registration": {
        "steps": """1. Open registration page
2. Enter ID & personal details
3. Confirm OTP
4. Activate account""",
        "time": "8 mins",
        "escalate": "System rejects ID or verification error",
        "tools": "-"
    }
}

# --- UI Buttons ---
st.subheader("Select an Issue Type")
cols = st.columns(3)

issue_list = list(issues.keys())

for i, issue in enumerate(issue_list):
    if cols[i % 3].button(issue):
        selected_issue = issue
        st.session_state["selected_issue"] = selected_issue

# --- DISPLAY SELECTED ISSUE DETAILS ---
if "selected_issue" in st.session_state:
    data = issues[st.session_state["selected_issue"]]

    st.markdown(f"## 🔍 {st.session_state['selected_issue']}")
    st.markdown("### 🛠 Digital Resolution Steps")
    st.code(data["steps"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("⏱ Expected Resolution Time", data["time"])

    with col2:
        st.metric("⚠️ Escalate If…", data["escalate"])

    with col3:
        st.metric("🔗 Tools / Links", data["tools"])
