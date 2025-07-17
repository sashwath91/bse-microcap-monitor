import os
import pandas as pd

from fetch import fetch_price, fetch_microcaps_list
from notifier import send_alerts

MICROCAPS_CSV = "microcaps.csv"

def update_microcaps():
    pass  # Implement logic to update weekly list

def monitor():
    syms = fetch_microcaps_list(MICROCAPS_CSV)
    alerts = []

    for s in syms:
        res = fetch_price(s)
        if not res:
            continue
        old, new = res
        if old > 0 and new / old >= 2.0:
            alerts.append(f"🔔 {s} doubled: {old:.2f} → {new:.2f}")

    if alerts:
        send_alerts(alerts, os.getenv('TELEGRAM_BOT_TOKEN'), os.getenv('TELEGRAM_CHAT_ID'))

def main():
    update_microcaps()
    monitor()

from update_microcaps import scrape_microcaps

def update_microcaps():
    scrape_microcaps()


if __name__ == "__main__":
    main()
