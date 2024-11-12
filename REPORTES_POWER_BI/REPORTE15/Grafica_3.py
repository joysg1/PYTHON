import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
# Reemplaza 'archivo.csv' con la ruta de tu archivo CSV
df = pd.read_csv('drug200.csv')

# Filtrar los datos de personas mayores de 40 años con presión y colesterol altos
df_filtered = df[(df['Age'] > 40) & (df['BP'] == 'HIGH') & (df['Cholesterol'] == 'HIGH')]

# Contar el número de hombres y mujeres que cumplen con estos criterios
count_gender = df_filtered['Sex'].value_counts()

# Generar el gráfico de barras
plt.figure(figsize=(8, 6))
ax = count_gender.plot(kind='bar', color=['blue', 'orange'])

# Agregar etiquetas encima de las barras
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                xytext=(0, 9),  # Desplazamiento vertical hacia arriba
                textcoords='offset points',
                ha='center', 
                va='center')

# Títulos y etiquetas
plt.title('Número de Mujeres y Hombres mayores de 40 años con presión y colesterol altos')
plt.xlabel('Género')
plt.ylabel('Número de Personas')
plt.xticks(rotation=0)

# Mostrar el gráfico
plt.show()



