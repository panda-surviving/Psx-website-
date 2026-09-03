from pathlib import Path
R=Path(__file__).resolve().parents[1]
def read(n): return (R/n).read_text()
def test_final_architecture():
 A=read('app.py'); J=read('static/app.js'); H=read('templates/index.html')
 for x in ['PSX_BULK_MARKET_WATCH_URL','PSX_EOD_URL','MUFAP_RETURNS_URL','fetch_psx_company_announcements','run_crypto_technical_scan']: assert x in A
 assert 'PSX • CLOSED • LAST SESSION' in J and 'data-tf="5H"' in H
