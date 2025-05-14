from elasticsearch import Elasticsearch
import pandas as pd

# Leer el CSV
df = pd.read_csv("data/iris.csv")

# Conectar a Elasticsearch (localhost:9200 por defecto)
es = Elasticsearch("http://localhost:9200")

# Crear índice si no existe
index_name = "iris"

if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

# Subir los datos
for i, row in df.iterrows():
    doc = row.to_dict()
    es.index(index=index_name, body=doc)

print("Datos cargados a Elasticsearch")
