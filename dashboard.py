import streamlit as st
import requests
import pandas as pd
import time

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="SentinelAI Command Center",
    layout="wide"
)

st.title("🛡️ SentinelAI - Security Command Center")
st.caption("AI-Powered SSH Threat Intelligence Platform")

# Auto refresh every 5 seconds
refresh = st.empty()

def fetch_data():
    try:
        threats = requests.get(f"{API_URL}/threats").json()
        summary = requests.get(f"{API_URL}/dashboard-summary").json()
        return threats, summary
    except:
        return [], {}

threats, summary = fetch_data()

if not threats:
    st.warning("No threats detected yet. Run /analyze first.")
    st.stop()

# ---------- TOP METRICS ----------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total IPs", summary.get("total_ips", 0))
col2.metric("High Risk", summary.get("high_risk", 0))
col3.metric("Medium Risk", summary.get("medium_risk", 0))
col4.metric("Anomalies", summary.get("anomalies_detected", 0))

st.divider()

# ---------- THREAT TABLE ----------
df = pd.DataFrame(threats)

def color_risk(val):
    if val == "HIGH":
        return "background-color: #ff4b4b; color: white"
    elif val == "MEDIUM":
        return "background-color: #ffa500; color: black"
    elif val == "LOW":
        return "background-color: #4caf50; color: white"
    return ""

styled_df = df.style.applymap(color_risk, subset=["risk_level"])

st.subheader("🚨 Active Threat Intelligence")
st.dataframe(styled_df, use_container_width=True)

st.divider()

st.caption("Auto-refreshing every 5 seconds")

time.sleep(5)
st.rerun()
