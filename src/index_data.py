import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/iris.csv")

#consulta a Elasticsearch
print("consulta a Elasticsearch...")

simulated_data = df.head(1000)  # O usar toda la data si prefieres

# Ahora, si necesitas hacer un gráfico con esos datos, podemos usar pandas y matplotlib
# Ejemplo de gráfico de dispersión con sepal length y sepal width
plt.figure(figsize=(10, 6))
plt.scatter(simulated_data['sepal_length'], simulated_data['sepal_width'])
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

print("Gráfico generado (simulado).")
