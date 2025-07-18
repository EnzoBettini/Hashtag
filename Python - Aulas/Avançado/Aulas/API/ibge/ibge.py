import requests
import pprint

resposta = requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/10153/periodos/2022/variaveis/1643?localidades=N1[all]&classificacao=2[6794]|1568[120704]')
resposta_json = resposta.json()
pprint.pprint(resposta_json)
