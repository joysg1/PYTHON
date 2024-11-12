import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
# Reemplaza 'archivo.csv' con la ruta de tu archivo CSV
df = pd.read_csv('drug200.csv')

# Crear un nuevo campo para los grupos de edad
df['Age_group'] = pd.cut(df['Age'], bins=[20, 30, 40, 50, 60, 100], labels=['20-30', '30-40', '40-50', '50-60', '60+'])

# Calcular el promedio de Na_to_K por grupo de edad
mean_na_to_k_by_age = df.groupby('Age_group')['Na_to_K'].mean()

# Graficar
plt.figure(figsize=(8, 6))
ax = mean_na_to_k_by_age.plot(kind='line', marker='o', color='b', linestyle='-', linewidth=2)

# Mostrar el valor de Na_to_K en cada punto
for i, value in enumerate(mean_na_to_k_by_age):
    ax.annotate(f'{value:.2f}',  # Valor con dos decimales
                xy=(i, value),  # Coordenadas (x, y)
                xytext=(5, 0),  # Desplazar el texto un poco
                textcoords='offset points',  # Usar coordenadas relativas
                ha='center', va='bottom',  # Alinear el texto
                fontsize=10, color='black')

# Personalizar el gráfico
plt.title('Promedio de Na_to_K en función de la Edad')
plt.xlabel('Grupo de Edad')
plt.ylabel('Promedio de Na_to_K')
plt.xticks(rotation=45)
plt.grid(True)

# Mostrar el gráfico
plt.show()

