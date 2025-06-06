import pandas as pd

def run_vcp_scan():
    # For testing: return a dummy DataFrame
    data = {
        'symbol': ['RELIANCE', 'TCS', 'INFY', 'TATA MOTERS']
        'close': [2500, 3200, 1500],
        'volume': [1000000, 800000, 1200000]
    }
    df = pd.DataFrame(data)
    return df
