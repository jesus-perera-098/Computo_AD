from elasticsearch import Elasticsearch
import pandas as pd
import matplotlib.pyplot as plt

# Conexión a Elasticsearch
es = Elasticsearch("http://localhost:9200")
index_name = "iris"

# Buscar todos los documentos
res = es.search(index=index_name, body={"query": {"match_all": {}}}, size=1000)

# Extraer los datos
data = [hit["_source"] for hit in res["hits"]["hits"]]
df = pd.DataFrame(data)

# Crear una gráfica simple
plt.figure(figsize=(8, 5))
for especie in df['species'].unique():
    subset = df[df['species'] == especie]
    plt.scatter(subset['sepal_length'], subset['sepal_width'], label=especie)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal Size por Especie")
plt.legend()

# Guardar imagen en la carpeta docs/
plt.savefig("docs/index.png")
print("Gráfica generada como docs/index.png")
