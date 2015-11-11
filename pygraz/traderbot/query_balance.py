"""
Print your private balances.
"""
import configparser
import json
import requests


def _without_utf8_bom(text):
    return text[3:] if text.startswith('\xef\xbb\xbf') else text

config = configparser.ConfigParser()
config.read('demobot.cfg')
api_key = config.get('demobot', 'api_key')

query = requests.get(
    'https://masterxchange.com/api/v2/private/balances.php',
    headers={'User-Agent': 'demobot/0.1'},
    params={'APIkey': api_key}
)
print('query.status_code =', query.status_code)
if query.status_code < 300:
    query_text = _without_utf8_bom(query.text)
    print('query_text = %r...' % query_text[:40])

    balances_result = json.loads(query_text)
    if balances_result['error_code'] == 0:
        balances = balances_result['balances']
        print('balances =', balances)
