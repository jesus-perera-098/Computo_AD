import pandas as pd


df = pd.read_csv("data/iris.csv")

# Simulación de conexión a Elasticsearch
print("Conectando a Elasticsearch...")
# Aquí se puede agregar un mensaje simulado, como si se estuviera conectando a Elasticsearch
# En realidad, no estamos haciendo nada, solo simulamos el proceso.

# Crear un índice simulado (sin interactuar con Elasticsearch)
index_name = "iris"
print(f"Índice '{index_name}' creado.")

# Subir los datos (en realidad, solo mostramos un mensaje)
for i, row in df.iterrows():
    doc = row.to_dict()
    print(f"Subiendo documento al índice {index_name}: {doc}")  # Simulamos la subida de datos

print("Datos 'cargados' a Elasticsearch.")

