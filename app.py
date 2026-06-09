import streamlit as st
from agents.troubleshooter import analyze_issue

st.set_page_config(
    page_title="KubeMind IQ",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 KubeMind IQ")
st.caption("Reason. Retrieve. Resolve.")

st.markdown("""
### AI-Powered AKS Troubleshooting Agent

KubeMind IQ leverages Foundry IQ-inspired knowledge retrieval and multi-step reasoning
to diagnose Kubernetes and AKS incidents.
""")

issue = st.text_area(
    "Describe your AKS issue",
    placeholder="Example: Pod is in CrashLoopBackOff"
)

if st.button("Analyze Incident"):

    result = analyze_issue(issue)

    st.subheader("📋 Incident Summary")
    st.info(result["summary"])

    st.subheader("🧠 Reasoning Process")

    for step in result["reasoning"]:
        st.write("✅", step)

    st.subheader("📚 Foundry IQ Knowledge")

    st.info("""
Retrieved Sources:
- AKS Runbooks
- Kubernetes Documentation
- Previous Incident Patterns
- Operational Knowledge Base
""")

    st.subheader("🚨 Root Cause")
    st.error(result["root_cause"])

    st.subheader("🔧 Recommendation")
    st.success(result["recommendation"])

    st.subheader("📊 Confidence Score")
    st.progress(int(result["confidence"].replace("%", "")))
    st.write(result["confidence"])