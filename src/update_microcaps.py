import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_microcaps_screener():
    url = "https://www.screener.in/screens/1235/micro-cap/"  # Example screener page for microcaps

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MicrocapScraper/1.0)"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # The table of stocks is inside a table with class "data-table"
    table = soup.find("table", {"class": "data-table"})

    rows = table.find_all("tr")[1:]  # skip header row

    symbols = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2:
            symbol = cols[1].text.strip()
            symbols.append(symbol)

    # Save to CSV
    df = pd.DataFrame(symbols, columns=["Symbol"])
    df.to_csv("microcaps.csv", index=False)
    print(f"Scraped {len(symbols)} microcap symbols.")

if __name__ == "__main__":
    scrape_microcaps_screener()
