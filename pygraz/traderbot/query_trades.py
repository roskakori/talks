"""
Print the top 3 maid coin trades.
"""
import json
import requests


def _without_utf8_bom(text):
    return text[3:] if text.startswith('\xef\xbb\xbf') else text


query = requests.get(
    'https://masterxchange.com/api/v2/trades.php', 
    headers={'User-Agent': 'demobot/0.1'},
    params={'currency': 'maid'}
)
print('query.status_code =', query.status_code)
if query.status_code < 400:
    query_text = _without_utf8_bom(query.text)
    print('query_text = %r...' % query_text[:40])

    trades = json.loads(query_text)
    print('trades =', trades[:3])
