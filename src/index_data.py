# src/index_data.py
import pandas as pd
import matplotlib.pyplot as plt
import os

# Leer el archivo CSV local
data = pd.read_csv("data/iris.csv")

# Crear la gráfica de dispersión
plt.figure(figsize=(10, 6))
species = data["species"].unique()
colors = ["red", "green", "blue"]
for sp, color in zip(species, colors):
    subset = data[data["species"] == sp]
    plt.scatter(subset["sepal_length"], subset["sepal_width"], label=sp, color=color)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Distribución de largo vs ancho de sépalos por especie")
plt.legend()

# Asegurar que la carpeta docs/ exista
os.makedirs("docs", exist_ok=True)

# Guardar la gráfica en docs/index.png
plt.savefig("docs/index.png")
print("✅ Gráfica guardada en docs/index.png")

