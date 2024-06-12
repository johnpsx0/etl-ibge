import requests
import pandas as pd

url = "https://servicodados.ibge.gov.br/api/v1/localidades/regioes/1|2|3|4|5/municipios"

r = requests.get(url)
jsonFull = r.json()

# Variaveis de listas para armazenamento dos dados
regiao = []
uf = []
mesoRegiao = []
microRegiao = []
municipio = []
codigoMunicipio = []

# Criou um varredor de itens
for item in jsonFull:
    regiao.append(item["microrregiao"]["mesorregiao"]["UF"]["regiao"]["nome"])
    uf.append(item["microrregiao"]["mesorregiao"]["UF"]["nome"])
    mesoRegiao.append(item["microrregiao"]["mesorregiao"]["nome"])
    microRegiao.append(item["microrregiao"]["nome"])
    municipio.append(item["nome"])
    codigoMunicipio.append(item["id"])

# Criar um DataFrame
dF = pd.DataFrame({
    "Regiao": regiao,
    "UF": uf,
    "Meso Regiao": mesoRegiao,
    "Micro Regiao": microRegiao,
    "Municipio": municipio,
    "Codigo do Municipio": codigoMunicipio
})

print(dF)

