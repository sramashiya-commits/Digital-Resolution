import streamlit as st

st.set_page_config(page_title="FAQ...Our Solutions Hub", layout="wide")

# --- CUSTOM STYLING ---
st.markdown("""
<style>
    .hub-button {
        background-color: #f0f4ff;
        border-radius: 12px;
        padding: 25px;
        border: 2px solid #d0d7ff;
        text-align: center;
        transition: 0.2s;
        cursor: pointer;
        font-weight: 700;
        color: #2c3e50;
        font-size: 18px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .hub-button:hover {
        background-color: #e1e8ff;
        transform: translateY(-3px);
        border-color: #8a9bff;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .issue-button {
        background-color: #f7f7f9;
        border-radius: 10px;
        padding: 15px;
        border: 1px solid #e0e0e0;
        text-align: left;
        transition: 0.2s;
        cursor: pointer;
        font-weight: 600;
        color: #333;
        margin: 8px 0;
    }
    .issue-button:hover {
        background-color: #e8f0fe;
        transform: translateY(-2px);
        border-color: #b3c7ff;
    }
    .issue-container {
        margin-bottom: 20px;
    }
    .title-container {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# --- MAIN TITLE ---
st.markdown('<div class="title-container"><h1>📱 Our Solutions Hub</h1><p>Select a solutions hub to access specific resolution guides</p></div>', unsafe_allow_html=True)

# --- DATA STORE FOR ALL HUBS ---
solutions_hubs = {
    "Digital Solutions Hub": {
        "description": "Digital banking, app, and online platform solutions",
        "issues": {
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
    },
    "Customer Services Solutions Hub": {
        "description": "Customer support, complaints, and service-related solutions",
        "issues": {
            "Coming Soon": {
                "steps": "Customer service solutions will be added here soon.",
                "time": "N/A",
                "escalate": "N/A",
                "tools": "N/A"
            }
        }
    },
    "Investment Solutions Hub": {
        "description": "Investment products, accounts, and portfolio management",
        "issues": {
            "Coming Soon": {
                "steps": "Investment solutions will be added here soon.",
                "time": "N/A",
                "escalate": "N/A",
                "tools": "N/A"
            }
        }
    },
    "Funeral Solutions Hub": {
        "description": "Funeral policies, claims, and related services",
        "issues": {
            "Coming Soon": {
                "steps": "Funeral solutions will be added here soon.",
                "time": "N/A",
                "escalate": "N/A",
                "tools": "N/A"
            }
        }
    },
    "My World Solutions Hub": {
        "description": "Personal accounts, profile management, and user settings",
        "issues": {
            "Coming Soon": {
                "steps": "My World solutions will be added here soon.",
                "time": "N/A",
                "escalate": "N/A",
                "tools": "N/A"
            }
        }
    }
}

# --- INITIALIZE SESSION STATE ---
if "selected_hub" not in st.session_state:
    st.session_state["selected_hub"] = None
if "selected_issue" not in st.session_state:
    st.session_state["selected_issue"] = None

# --- HUB SELECTION SECTION ---
st.markdown("## 🏢 Select a Solutions Hub")

# Create 5 buttons for the main hubs
cols = st.columns(5)

hub_names = [
    "Digital Solutions Hub",
    "Customer Services Solutions Hub", 
    "Investment Solutions Hub",
    "Funeral Solutions Hub",
    "My World Solutions Hub"
]

icons = ["💻", "📞", "📈", "⚰️", "🌍"]

for i, (hub_name, icon) in enumerate(zip(hub_names, icons)):
    with cols[i]:
        if st.button(f"{icon}\n\n{hub_name}", key=f"hub_{i}", use_container_width=True):
            st.session_state["selected_hub"] = hub_name
            st.session_state["selected_issue"] = None

# --- DISPLAY SELECTED HUB CONTENT ---
if st.session_state["selected_hub"]:
    selected_hub_data = solutions_hubs[st.session_state["selected_hub"]]
    
    st.markdown(f"---")
    st.markdown(f"## {icons[hub_names.index(st.session_state['selected_hub'])]} {st.session_state['selected_hub']}")
    st.markdown(f"*{selected_hub_data['description']}*")
    
    # Create two-column layout for issues and details
    left_col, right_col = st.columns([1, 2])
    
    # LEFT SIDE = ISSUE BUTTONS
    with left_col:
        st.markdown("### 🧩 Issue Types")
        for issue_name in selected_hub_data["issues"].keys():
            if st.button(issue_name, key=f"issue_{issue_name}"):
                st.session_state["selected_issue"] = issue_name
    
    # RIGHT SIDE = ISSUE DETAILS
    with right_col:
        if st.session_state["selected_issue"]:
            data = selected_hub_data["issues"][st.session_state["selected_issue"]]
            
            st.markdown(f"## 🔍 {st.session_state['selected_issue']}")
            
            st.markdown("### 🛠 Resolution Steps")
            st.code(data["steps"], language="markdown")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("⏱ Expected Time", data["time"])
            c2.metric("⚠️ Escalate If", data["escalate"])
            c3.metric("🔗 Tools", data["tools"])
            
            # Back button to return to hub selection
            if st.button("← Back to Hub Selection"):
                st.session_state["selected_hub"] = None
                st.session_state["selected_issue"] = None
                st.rerun()
        else:
            st.info("👈 Select an issue from the left to view detailed resolution steps.")
    
    # Add a clear button at the bottom
    if st.button("Clear Selection", type="secondary"):
        st.session_state["selected_hub"] = None
        st.session_state["selected_issue"] = None
        st.rerun()

else:
    # Initial state - show instructions
    st.markdown("---")
    st.markdown("### ℹ️ How to use this Solutions Hub:")
    st.markdown("""
    1. **Select a Hub** from the 5 options above
    2. **Choose an Issue** from the left sidebar
    3. **View Resolution Steps** on the right side
    
    Each hub contains specific solutions tailored to different service areas.
    """)
    
    # Optional: Show quick stats
    st.markdown("### 📊 Quick Stats")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Hubs", "5")
    with col2:
        st.metric("Digital Solutions", "7")
    with col3:
        st.metric("Coming Soon", "4")
