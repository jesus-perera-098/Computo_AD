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
os.makedirs("docs", exist_ok=True)  # Asegúrate de guardar aquí para GitHub Pages

# Calcular promedios por especie
means = df.groupby("species")[["petal_length", "petal_width"]].mean()

# Crear gráfico de barras
means.plot(kind="bar", figsize=(10, 6))
plt.title("Promedio de dimensiones del pétalo por especie")
plt.ylabel("Longitud / Ancho del pétalo")
plt.xlabel("Especie")
plt.xticks(rotation=0)
plt.legend(["Largo del pétalo", "Ancho del pétalo"])

# Guardar gráfico
plt.tight_layout()
plt.savefig("docs/index.png")  # Este archivo se publica en GitHub Pages
print("Gráfico guardado en docs/index.png")


