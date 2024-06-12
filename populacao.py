import requests
import pandas as pd

url = "https://servicodados.ibge.gov.br/api/v3/agregados/4714/periodos/-6/variaveis/93?localidades=N6[all]"


r = requests.get(url)
jsonFull = r.json()
jsonBase = jsonFull[0]['resultados'][0]['series']

# Listas para armazenamento dos dados
codigoMunicipio = []
populacao = []


#  Localidade - ID
# Serie - 2022
# Criou um varredor de itens
for item in jsonBase:
    codigoMunicipio.append(item["localidade"]["id"]) #pegue item de localidade - 'ID'
    populacao.append(item["serie"]["2022"]) # pegue item de Serie - '2022'

# Criar um DataFrame
dF = pd.DataFrame({
    "Codigo do Municipio": codigoMunicipio,
    "Populacao": populacao
})

print(dF)