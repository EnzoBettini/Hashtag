import requests

#cep_busca = input("Digite o cep para realizar a busca: ")

# Corrigindo o esquema da URL
resposta = requests.get(f'https://viacep.com.br/ws/87013250/json/')
dados = resposta.json()

# Verifica se o CEP é válido
if "erro" in dados:
    print("CEP não encontrado.")
else:
    print(f"""
CEP: {dados['cep']}
Logradouro: {dados['logradouro']}
Bairro: {dados['bairro']}
Cidade: {dados['localidade']}
Estado: {dados['uf']}
""")
