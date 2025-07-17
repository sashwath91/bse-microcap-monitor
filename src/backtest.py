import yfinance as yf
import pandas as pd

def backtest(symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    ticker = yf.Ticker(symbol + ".BO")
    hist = ticker.history(start=start_date, end=end_date)
    hist['Pct_30d'] = hist['Close'].pct_change(periods=30)
    doubled = hist[hist['Pct_30d'] >= 1.0]
    return doubled[['Close', 'Pct_30d']]
