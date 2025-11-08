"""Test version checker in Streamlit"""
import streamlit as st
from utils.version_checker import get_version_info
from utils.constants import TESTED_CREWAI_VERSIONS, LATEST_TESTED_VERSION

st.title("Version Checker Test")

st.write("Testing version detection...")

version, is_compatible, message = get_version_info(
    TESTED_CREWAI_VERSIONS,
    LATEST_TESTED_VERSION
)

st.write(f"**Version detected:** {version}")
st.write(f"**Is compatible:** {is_compatible}")
st.write(f"**Message exists:** {bool(message)}")
st.write(f"**Message length:** {len(message) if message else 0}")

st.markdown("---")
st.write("**Sidebar test:**")

with st.sidebar:
    st.header("Sidebar Version Check")

    if message:
        if is_compatible:
            st.success(message)
        else:
            st.warning(message)
    else:
        st.info("No message (CrewAI not installed or version is in tested range)")

st.markdown("---")
st.write("**Raw message:**")
if message:
    st.code(message)
else:
    st.write("(No message)")
