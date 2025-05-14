import pandas as pd
import matplotlib.pyplot as plt


print("Conectando a Elasticsearch...")
print("Realizando búsqueda en el índice 'iris'...")


df = pd.read_csv("data/iris.csv")


simulated_data = df.head(1000)  # como si viniera de una búsqueda con size=1000

# Mostrar resumen de los datos 
print("Datos obtenidos:")
print(simulated_data.head())

# Generar un gráfico simple
plt.figure(figsize=(10, 6))
plt.scatter(simulated_data['sepal_length'], simulated_data['sepal_width'], alpha=0.7)
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.grid(True)
plt.savefig("outputs/sepal_scatter.png")  # Guardar gráfico en lugar de mostrar
print("Gráfico guardado en outputs/sepal_scatter.png")

