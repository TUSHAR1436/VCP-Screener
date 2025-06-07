
import pandas as pd
import requests
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "application/json",
    "Referer": "https://www.nseindia.com/"
}

INDEX_ENDPOINTS = {
    "NIFTY 50": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050",
    "NIFTY MIDCAP 100": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20MIDCAP%20100",
    "NIFTY SMALLCAP 100": "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20SMALLCAP%20100",
}

def fetch_index_stocks():
    session = requests.Session()
    session.get("https://www.nseindia.com", headers=HEADERS)
    all_stocks = []
    for index, url in INDEX_ENDPOINTS.items():
        try:
            response = session.get(url, headers=HEADERS)
            data = response.json()
            stocks = [item['symbol'] for item in data['data']]
            all_stocks.extend(stocks)
            time.sleep(1)
        except Exception as e:
            print(f"Error fetching {index}: {e}")
    return list(set(all_stocks))

def fetch_stock_data(symbol):
    url = f"https://www.nseindia.com/api/chart-databyindex?index={symbol}"
    session = requests.Session()
    session.get("https://www.nseindia.com", headers=HEADERS)
    try:
        response = session.get(url, headers=HEADERS)
        data = response.json()
        prices = data['grapthData'][symbol]
        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        return df
    except:
        return pd.DataFrame()
