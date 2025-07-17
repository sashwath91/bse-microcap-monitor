import pandas as pd

def update_microcaps_from_csv():
    df = pd.read_csv("src/nifty_microcap_250.csv")
    
    if "SYMBOL" not in df.columns:
        raise ValueError("CSV must have a 'Symbol' column")

    # Save only symbols to microcaps.csv for main monitor script
    df[["SYMBOL"]].to_csv("src/microcaps.csv", index=False)
    print(f"Loaded {len(df)} symbols from static Nifty Microcap 250 CSV.")

if __name__ == "__main__":
    update_microcaps_from_csv()
