import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset en un DataFrame
df = pd.read_csv('vehicule.csv')

# Agrupar los datos por la clase del vehículo y obtener el valor medio de 'COMPACTNESS'
# Esto nos da un resumen de cómo varía el atributo 'COMPACTNESS' por cada clase de vehículo
compactness_means = df.groupby('Class')['COMPACTNESS'].mean()

# Crear gráfico de barras apiladas para comparar la 'COMPACTNESS' de cada vehículo
plt.figure(figsize=(10, 6))

# Plot de barras
ax = compactness_means.plot(kind='bar', stacked=False, color=['skyblue', 'salmon', 'lightgreen', 'lightcoral'])

# Etiquetas y título
plt.title('Comparación de Compactness por Vehículo', fontsize=16)
plt.xlabel('Clase de Vehículo', fontsize=14)
plt.ylabel('Valor Promedio de Compactness', fontsize=14)

# Agregar los valores en las barras en negrita
for i in ax.patches:
    ax.annotate(f'{i.get_height():.2f}',  # Mostrar valor con dos decimales
                (i.get_x() + i.get_width() / 2, i.get_height()),  # Coordenadas
                xytext=(0, 5),  # Mover el texto hacia arriba
                textcoords='offset points', 
                ha='center', va='bottom', fontweight='bold', color='black')  # Formato en negrita

# Ajustar para que todo se vea bien
plt.tight_layout()
plt.show()
