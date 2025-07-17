import yfinance as yf
import pandas as pd

def fetch_price(symbol: str):
    ticker = yf.Ticker(symbol + ".BO")
    hist = ticker.history(period="35d")
    if len(hist) < 2:
        return None
    end = hist['Close'].iloc[-1]
    one_month_ago = hist['Close'].iloc[0]
    return one_month_ago, end

def fetch_microcaps_list(csv_path="microcaps.csv"):
    try:
        return pd.read_csv(csv_path)['Symbol'].tolist()
    except FileNotFoundError:
        return []
