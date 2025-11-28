import streamlit as st

# -------------------- PAGE STYLE --------------------
st.set_page_config(page_title="Digital Resolution Hub", layout="wide")

# Custom CSS for colours, 3D buttons & layout
st.markdown("""
<style>

body {
    background-color: #f5f7fa;
}

/* Title styling */
h1 {
    color: #1f3c88;
    font-weight: 900;
}

/* Subheader */
h3 {
    color: #0d1b2a;
    font-weight: 700;
}

/* Card container */
.issue-card {
    background: white;
    padding: 18px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    transition: transform 0.2s ease;
}

.issue-card:hover {
    transform: scale(1.02);
}

/* Trendy 3D buttons */
.stButton>button {
    background: linear-gradient(145deg, #ffffff, #dfe4ea);
    border-radius: 12px;
    padding: 12px 18px;
    width: 100%;
    color: #1f3c88;
    border: 2px solid #e1e5eb;
    font-weight: 700;
    box-shadow: 4px 4px 10px #cbd3dd, -4px -4px 10px #ffffff;
    transition: 0.3s;
}

.stButton>button:hover {
    background: #1f3c88;
    color: white;
    border: 2px solid #1f3c88;
    transform: translateY(-3px);
}

</style>
""", unsafe_allow_html=True)

# -------------------- TITLE --------------------
st.title("📱 Digital Resolution Hub")
st.write("Your quick, guided digital troubleshooting companion.Brought to you by 'The Digital Support Team'.")

st.write("---")

# -------------------- DATA --------------------
issues = {
    "Forgot Password": {
        "steps": """1. Tap **Forgot Password** on login
2. Enter **ID number**
3. Enter **OTP**
4. Reset password and login""",
        "time": "5 mins",
        "escalate": "OTP not received after 3 attempts",
        "tools": "App"
    },

    "Forgot all login credentials": {
        "steps": """1. Tap **Forgot all login credentials**
2. Enter **ID number**
3. Reset username & password
4. Login""",
        "time": "6 mins",
        "escalate": "Verification fails 3 times",
        "tools": "App"
    },

    "Pin Blocked": {
        "steps": """1. Tap **Unblock PIN**
2. Validate ID + DOB
3. Confirm OTP
4. Set new PIN""",
        "time": "3 mins",
        "escalate": "Validation fails",
        "tools": "Internet banking"
    },

    "Sim Override (For Branch)": {
        "steps": """1. Verify ID
2. Use device change portal
3. Confirm OTP""",
        "time": "10 mins",
        "escalate": "ID mismatch",
        "tools": "-"
    },

    "App Slow Response": {
        "steps": """1. Clear app cache
2. Restart device
3. If issue persists, escalate""",
        "time": "5 mins",
        "escalate": "Still slow after restart",
        "tools": "Device"
    },

    "Unable to Register (Profile deleted)": {
        "steps": """1. Check if profile deleted
2. Re-register
3. Confirm with OTP""",
        "time": "8 mins",
        "escalate": "Account not found",
        "tools": "-"
    },

    "Registration": {
        "steps": """1. Enter personal details
2. Confirm OTP
3. Activate account""",
        "time": "8 mins",
        "escalate": "Verification error",
        "tools": "-"
    }
}

# -------------------- ISSUE SELECTION --------------------
st.subheader("Select an Issue Type")

cols = st.columns(3)
issue_list = list(issues.keys())

for i, issue in enumerate(issue_list):
    if cols[i % 3].button(issue):
        st.session_state["selected_issue"] = issue

st.write("---")

# -------------------- DISPLAY INFORMATION --------------------
if "selected_issue" in st.session_state:
    data = issues[st.session_state["selected_issue"]]

    st.markdown(
        f"<div class='issue-card'>"
        f"<h2>🔍 {st.session_state['selected_issue']}</h2>"
        f"</div>",
        unsafe_allow_html=True
    )

    st.markdown("### 🛠 Digital Resolution Steps")
    st.code(data["steps"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("⏱ Expected Resolution Time", data["time"])

    with col2:
        st.metric("⚠️ Escalate If…", data["escalate"])

    with col3:
        st.metric("🔗 Tools / Links", data["tools"])
