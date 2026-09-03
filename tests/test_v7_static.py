from pathlib import Path
R=Path(__file__).resolve().parents[1]; A=(R/'app.py').read_text(); H=(R/'templates/index.html').read_text(); SW=(R/'static/sw.js').read_text()
def test_final_architecture():
 assert 'def _intraday_price_df_from_psx' in A and 'def fetch_psx_eod_history' in A
 assert 'screenerAlphabet' in H and 'psx-360-shell-v15' in SW
