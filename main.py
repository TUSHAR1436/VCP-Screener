
from vcp_logic import apply_vcp_filters
from utils.data_fetcher import fetch_all_nse_data

def run_vcp_screener():
    df = fetch_all_nse_data()
    result = apply_vcp_filters(df)
    result.to_csv("vcp_results.csv", index=False)
    print("VCP scan completed. Results saved to vcp_results.csv")

if __name__ == "__main__":
    run_vcp_screener()
