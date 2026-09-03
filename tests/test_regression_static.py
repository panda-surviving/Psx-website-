from pathlib import Path
R=Path(__file__).resolve().parents[1]; A=(R/'app.py').read_text(); J=(R/'static/app.js').read_text()
def test_psx_data(): assert 'def fetch_psx_eod_history' in A and 'def _fetch_market_watch_table' in A
def test_announcements(): assert 'fetch_psx_company_announcements' in A and '/api/psx/announcements' in J
def test_crypto(): assert 'market_chart' in A and 'api.coingecko.com/api/v3/coins/{coin_id}/ohlc' in A
