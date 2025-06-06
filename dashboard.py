
import streamlit as st
import pandas as pd

st.set_page_config(page_title="VCP Screener", layout="wide")
st.title("📈 SwingAlgo-Style VCP Screener")

# Load data
try:
    df = pd.read_csv("vcp_results.csv")
    st.success("Data loaded successfully.")
except:
    df = pd.DataFrame()
    st.warning("No data available. Run the screener first.")

# Tabs like IPO | VCP | Rocket | FNO
tabs = st.tabs(["IPO", "VCP", "Rocket", "FNO"])
with tabs[1]:
    st.subheader("VCP Scanned Stocks (Perfect Swing Setups)")
    if not df.empty:
        st.dataframe(df)
    else:
        st.write("No stocks matched VCP criteria today.")
