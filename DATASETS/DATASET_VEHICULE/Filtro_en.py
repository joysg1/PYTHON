import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset en un DataFrame
df = pd.read_csv('vehicule.csv')

# Agrupar los datos por la clase del vehículo y obtener el valor medio de 'ELONGATEDNESS'
elongatedness_means = df.groupby('Class')['ELONGATEDNESS'].mean()

# Ordenar los valores de 'ELONGATEDNESS' de menor a mayor
elongatedness_means = elongatedness_means.sort_values(ascending=True)

# Crear gráfico de líneas para comparar la 'ELONGATEDNESS' de cada vehículo
plt.figure(figsize=(10, 6))

# Plot de línea
ax = elongatedness_means.plot(kind='line', marker='o', color='b', linestyle='-', linewidth=2, markersize=8)

# Etiquetas y título
plt.title('Comparación de Elongatedness por Vehículo', fontsize=18)
plt.xlabel('Clase de Vehículo', fontsize=18)
plt.ylabel('Valor Promedio de Elongatedness', fontsize=18)

# Agregar los valores en las líneas en negrita
for x, y in enumerate(elongatedness_means):
    ax.text(x, y + 0.02, f'{y:.2f}', ha='center', fontweight='bold', color='black')

# Ajustar para que todo se vea bien
plt.tight_layout()
plt.show()
