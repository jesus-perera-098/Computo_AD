import pandas as pd
import matplotlib.pyplot as plt
import os

print("Cargando datos desde CSV...")

# Leer CSV
df = pd.read_csv("data/iris.csv")

# Verificar que el archivo se leyó correctamente
print("Datos cargados:")
print(df.head())

# Crear carpeta si no existe
os.makedirs("docs", exist_ok=True)

# Graficar dimensiones del pétalo
plt.figure(figsize=(10, 6))
for species in df["species"].unique():
    subset = df[df["species"] == species]
    plt.scatter(subset["petal_length"], subset["petal_width"], label=species)

plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Iris Dataset - Petal Dimensions")
plt.legend()

# Guardar gráfico en la carpeta `docs` con el nombre `index.png`
plt.savefig("docs/index.png")
print("Gráfico guardado en docs/index.png")


