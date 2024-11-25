import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset en un DataFrame
df = pd.read_csv('vehicule.csv')

# Calcular el valor medio de 'CIRCULARITY' por clase de vehículo
circularity_means = df.groupby('Class')['CIRCULARITY'].mean()

# Crear un gráfico de líneas
plt.figure(figsize=(10, 6))

# Graficar la línea con color rojo
plt.plot(circularity_means.index, circularity_means.values, marker='o', color='red', linewidth=2, markersize=8)

# Rellenar el área debajo de la línea con un rojo claro
plt.fill_between(circularity_means.index, circularity_means.values, color='red', alpha=0.3)

# Título y etiquetas
plt.title('Valor Promedio de Circularity por Vehículo', fontsize=16)
plt.xlabel('Clase de Vehículo', fontsize=14)
plt.ylabel('Valor Promedio de Circularity', fontsize=14)

# Mostrar los valores en los puntos de la línea
for i, value in enumerate(circularity_means.values):
    plt.text(i, value, f'{value:.2f}', ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

# Mostrar el gráfico
plt.tight_layout()
plt.show()



