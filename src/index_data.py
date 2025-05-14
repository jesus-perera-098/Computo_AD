import os
import pandas as pd
import matplotlib.pyplot as plt

# Crear carpeta outputs si no existe
os.makedirs("outputs", exist_ok=True)

print("Conectando a Elasticsearch...")
print("Realizando búsqueda en el índice 'iris'...")

df = pd.read_csv("data/iris.csv")
simulated_data = df.head(1000)

print("Datos obtenidos:")
print(simulated_data.head())

plt.figure(figsize=(10, 6))
plt.scatter(simulated_data['sepal_length'], simulated_data['sepal_width'], alpha=0.7)
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.grid(True)

# Guardar en outputs/
plt.savefig("outputs/sepal_scatter.png")
print("Gráfico guardado en outputs/sepal_scatter.png")

