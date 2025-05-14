import pandas as pd

print("Cargando datos desde CSV...")

# Cargar datos desde archivo local
df = pd.read_csv("data/iris.csv")

print("Datos obtenidos:")
print(df.head())

# Crear carpeta si no existe
import os
os.makedirs("outputs", exist_ok=True)

# Graficar dimensiones del sépalo
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
for species in df["species"].unique():
    subset = df[df["species"] == species]
    plt.scatter(subset["sepal_length"], subset["sepal_width"], label=species)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Dataset - Sepal Dimensions")
plt.legend()

# Guardar imagen
plt.savefig("outputs/sepal_scatter.png")
print("Gráfico guardado en outputs/sepal_scatter.png")
