from pathlib import Path
R=Path(__file__).resolve().parents[1]; A=(R/'app.py').read_text(); H=(R/'templates/index.html').read_text(); J=(R/'static/app.js').read_text(); SW=(R/'static/sw.js').read_text()
def test_final_chart_windows():
 for x in ['"1H": {"mode":"intraday"','"5H": {"mode":"intraday"','"1D": {"mode":"intraday"','"5D": {"mode":"daily"']: assert x in A
 assert 'def _intraday_price_df_from_psx' in A
def test_real_mufap_sources():
 assert 'MUFAP_RETURNS_URL' in A and 'MUFAP official NAV + Performance Summary' in A
def test_real_announcements_post():
 assert 'def fetch_psx_company_announcements' in A and '"type":"C"' in A and '.post(' in A
def test_alpha_screener():
 assert 'screenerAlphabet' in H and 'symbol_prefix' in A
def test_sw(): assert 'psx-360-shell-v15' in SW
