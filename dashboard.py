import streamlit as st
import pandas as pd
from vcp_logic import run_vcp_scan

st.set_page_config(page_title="VCP Screener", layout="wide")

st.title("📈 VCP Screener (SwingAlgo Style)")

# Tabs like SwingAlgo
tabs = st.tabs(["📊 VCP", "🚀 IPO", "🔥 Rocket", "ℹ️ Info"])

with tabs[0]:
    st.header("VCP Swing Setup Finder")
    if st.button("🔍 Run Screener"):
        with st.spinner("Running VCP scan..."):
            result_df = run_vcp_scan()
            if result_df.empty:
                st.warning("No stocks matched VCP criteria today.")
            else:
                st.success(f"Found {len(result_df)} stocks matching VCP criteria.")
                st.dataframe(result_df, use_container_width=True)
    else:
        st.info("Click 'Run Screener' to see today's VCP setups.")

with tabs[1]:
    st.header("🚀 IPO Tab Coming Soon")
    st.write("This section will show IPO-based setups.")

with tabs[2]:
    st.header("🔥 Rocket Tab Coming Soon")
    st.write("This section will show high-momentum rockets.")

with tabs[3]:
    st.header("ℹ️ About this App")
    st.markdown("""
    - Built by [ChatGPT]
    - Auto-scans VCP setups from Nifty50, Midcap100, Smallcap100
    - Deployed using Streamlit Cloud
    """)
