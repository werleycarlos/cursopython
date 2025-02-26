import json
import requests as rq

resposta = rq.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes/werley')

dados_jason = json.loads(resposta.text)

print(dados_jason[0]['res'][0])
