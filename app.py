import streamlit as st

st.set_page_config(page_title="Digital Resolution Hub", layout="wide")

# --- CUSTOM STYLING ---
st.markdown("""
<style>
    .issue-button {
        background-color: #f7f7f9;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        text-align: center;
        transition: 0.2s;
        cursor: pointer;
        font-weight: 600;
        color: #333;
    }
    .issue-button:hover {
        background-color: #e8f0fe;
        transform: translateY(-3px);
        border-color: #b3c7ff;
    }
    .issue-container {
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.title("📱 Digital Resolution Hub")
st.write("Select an issue type below to view the resolution instantly — no scrolling needed.")

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

# --- TWO-COLUMN LAYOUT ---
left_col, right_col = st.columns([1, 2])

# LEFT SIDE = BUTTONS
with left_col:
    st.subheader("🧩 Issue Types")
    for issue in issues.keys():
        if st.button(issue, key=issue):
            st.session_state["selected_issue"] = issue

# RIGHT SIDE = DETAILS (SHOW IMMEDIATELY)
with right_col:
    if "selected_issue" in st.session_state:
        data = issues[st.session_state["selected_issue"]]

        st.markdown(f"## 🔍 {st.session_state['selected_issue']}")

        st.markdown("### 🛠 Digital Resolution Steps")
        st.code(data["steps"])

        c1, c2, c3 = st.columns(3)
        c1.metric("⏱ Expected Time", data["time"])
        c2.metric("⚠️ Escalate If", data["escalate"])
        c3.metric("🔗 Tools", data["tools"])
    else:
        st.info("Select an issue from the left to view details.")
