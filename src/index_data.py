import pandas as pd
import matplotlib.pyplot as plt
from elasticsearch import Elasticsearch

# Simulación de la conexión a Elasticsearch (pero no se usa realmente)
es = Elasticsearch("http://localhost:9200")

# Leer el CSV
df = pd.read_csv("data/iris.csv")

# Crear índice simulado (no hace nada en realidad)
index_name = "iris"

# Simulamos la creación del índice (aunque no se hace nada)
print(f"Conectando a Elasticsearch en {es.transport.hosts[0]['host']}...")
print(f"Índice '{index_name}' creado (simulado)")

# Simulación de "subir" los datos
for i, row in df.iterrows():
    doc = row.to_dict()
    # Aquí simplemente mostramos el documento en lugar de enviarlo a Elasticsearch
    print(f"Subiendo documento {i+1} a Elasticsearch... (simulado)")

# Generar un gráfico (de verdad, con los datos del CSV)
df.plot(kind="scatter", x="sepal_length", y="sepal_width")  # Asegúrate de que las columnas existan
plt.title("Gráfico de Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()

print("Datos procesados correctamente)

