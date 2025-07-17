# BSE Microcap Monitor

Tracks BSE microcap stocks and sends Telegram alerts when any doubles in the last month.

## ⚙️ Setup

1. Add secrets on GitHub:
   - `5200806540:AAHTnE2pe7PpvWJPu7ZVw2UqPmNoaA_BufU`
   - `1170695797`

2. Edit `src/main.py` to implement `update_microcaps()` or provide `microcaps.csv`.

3. Workflow schedules weekly runs; you can also trigger manually.

4. For backtesting:
   ```bash
   pip install -r requirements.txt
   python -c "from src.backtest import backtest; print(backtest('500112','2020-01-01','2025-07-17'))"
# bse-microcap-monitor
