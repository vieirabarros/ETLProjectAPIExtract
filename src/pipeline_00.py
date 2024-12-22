import time
import requests
from tinydb import TinyDB
from datetime import datetime


def extract_dados_bitcoin():
    url = "https://api.coinbase.com/v2/prices/spot" #endpoint, cada url é um endpoint
    response = requests.get(url) #fazendo a requisição
    dados = response.json() #transformando a resposta em json
    return dados

def transform_dados_bitcoin(dados):
    valor= dados["data"]["amount"]
    criptomoeda= dados["data"]["base"]
    moeda= dados["data"]["currency"]
    timestamp= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dados_transformados= {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp
    }
    return dados_transformados

def salvar_dados_tinydb(dados, db_name="bitcoin.json"):
    db = TinyDB(db_name)
    db.insert(dados)
    print("Dados salvos com sucesso!")
    

if __name__ == "__main__":
    while True:
        dados= extract_dados_bitcoin()
        dados_transformados= transform_dados_bitcoin(dados)
        salvar_dados_tinydb(dados_transformados)
        time.sleep(15)