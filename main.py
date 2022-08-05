import requests
import json
from datetime import date
import configparser
from azure.storage.blob import BlobServiceClient

def getJson(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

API_ENDPOINT = "https://app.neocrm.com.br/producao-painel-integration"
today = date.today()

data = { 
       "tokenEstrutura":"f9d1b75c-fd66-4367-baa8-e09cbb1e478a",
       "tokenUsuario":"282159ff-bcc4-4cfe-b441-d0dfe79c1848",
       "dataInicial":"2022-01-01",
       "dataFinal":str(today),
       "painelId":"14017"
    }

r = requests.post(url = API_ENDPOINT, json = data)
#print(r.text)

f = open('data.csv', "w")
f.write(r.text)
f.close()

