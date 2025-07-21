import requests

db_link = 'https://teste-hashtag-e83db-default-rtdb.firebaseio.com/'

# dados = {'cliente': 'carlos', 'quantidade': 712}
# requisicao = requests.post(f'{db_link}/Cliente/vendas/.json', json=dados)

# print(requisicao)
# print(requisicao.text)

dados2 = {'cliente': 'joao', 'quantidade': 712}
requisicao2 = requests.patch(f'{db_link}/Cliente/vendas/-OVVFTbQcuko59-jLq1q/.json', json=dados2)

print(requests.get(f'{db_link}/Cliente/vendas/-OVVFTbQcuko59-jLq1q/.json',))
print(requests.delete(f'{db_link}/Cliente/vendas/-OVVFTbQcuko59-jLq1q/.json',))
print(requests.get(f'{db_link}/Cliente/vendas/.json',))
