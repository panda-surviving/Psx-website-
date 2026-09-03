from pathlib import Path
R=Path(__file__).resolve().parents[1]; A=(R/'app.py').read_text(); H=(R/'templates/index.html').read_text(); J=(R/'static/app.js').read_text()
def test_sources():
 for x in ['PSX_EOD_URL','PSX_ANNOUNCEMENTS_URL','MUFAP_RETURNS_URL','run_crypto_technical_scan','CoinGecko OHLC (real market data)']: assert x in A
def test_timeframes():
 assert 'data-tf="1H"' in H and 'data-tf="5H"' in H and 'data-tf="1D"' in H
def test_ticker_states(): assert 'PSX • CLOSED • LAST SESSION' in J and 'market_state==="LIVE"' in J
