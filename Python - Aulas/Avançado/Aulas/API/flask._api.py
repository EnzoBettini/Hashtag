from flask import Flask
import pandas as pd

df = pd.read_excel(r'C:\Users\enzo.bettini\Documents\Hashtag\Python - Aulas\Avançado\Aulas\API\vendas.xlsx')

app = Flask(__name__)


@app.route("/")
def faturamento():
    total = df['Valor Final'].sum()
    return {'faturamento': float(total)}


@app.route("/vendas")
def vendas_produtos():
    df_vendas_produtos = df[['Produto', 'Valor Final']].groupby('Produto').sum()
    retorno_json = df_vendas_produtos.to_dict()
    return retorno_json

@app.route("/produto")
def produto_especifico():
    return {}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
