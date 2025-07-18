import requests
import json

cotacoes = requests.get('https://3446fbdd-859a-4d67-b36c-02f159667da7-00-1jkokrhmknobv.kirk.replit.dev:3000/outra_pagina')
cotacao_json = cotacoes.json()
print(cotacao_json)
