import requests
import json
from datetime import date
import configparser
from azure.storage.blob import BlobServiceClient

def getJson(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

config = configparser.ConfigParser()
config.read("credentials.ini")

ACCKEY  = config["AZURE"]["ACCKEY"]
CONTAINER = config["AZURE"]["CONTAINER"]
TOKENESTRUTURA = config["API"]["TOKENESTRUTURA"]
TOKENUSUARIO = config["API"]["TOKENUSUARIO"]
PAINEL = config["API"]["PAINEL"]
API_ENDPOINT = config["API"]["API_ENDPOINT"]

blob_service_client = BlobServiceClient.from_connection_string(ACCKEY)
container_client = blob_service_client.get_container_client(CONTAINER)

today = date.today()

data = { 
       "tokenEstrutura":TOKENESTRUTURA,
       "tokenUsuario":TOKENUSUARIO,
       "dataInicial":"2022-01-01",
       "dataFinal":str(today),
       "painelId":PAINEL
    }

r = requests.post(url = API_ENDPOINT, json = data)

#Save data into blob storage
print("Saving data...")
blob_client = container_client.get_blob_client("API_DATA.csv")
blob_client.upload_blob(r.text, blob_type="BlockBlob", overwrite=True)
print('Saved.')

