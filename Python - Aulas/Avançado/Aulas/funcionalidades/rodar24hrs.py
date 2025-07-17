import requests
from datetime import datetime

request = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

request_json = request.json()

cotacao_dolar = request_json['USDBRL']['bid']
cotacao_euro = request_json['EURBRL']['bid']
cotacao_btc = request_json['BTCBRL']['bid']

print(cotacao_btc)
print(cotacao_dolar)
print(cotacao_euro)
