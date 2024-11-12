import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('drug200.csv')

# Crear una columna para los grupos de edad
df['Age_group'] = pd.cut(df['Age'], bins=[20, 30, 40, 50, 60, 100], labels=['20-30', '30-40', '40-50', '50-60', '60+'])

# Crear la columna para los niveles de colesterol
df['Cholesterol_level'] = df['Cholesterol']

# Crear la tabla de contingencia
contingency = pd.crosstab(index=[df['Age_group'], df['Cholesterol_level']], columns=df['Sex'])

# Graficar las barras apiladas
ax = contingency.plot(kind='bar', stacked=True, figsize=(10, 7), color=['#FFF9C4', '#D1C4E9'], width=0.8)

# Personalizar el gráfico
plt.title('Distribución de Sexo, Edad y Nivel de Colesterol')
plt.xlabel('Grupo de Edad y Nivel de Colesterol')
plt.ylabel('Cantidad de Personas')
plt.xticks(rotation=45)
plt.legend(title='Sexo', loc='upper left', labels=['Mujeres', 'Hombres'])
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Añadir los números encima de las barras apiladas
for p in ax.patches:
    height = p.get_height()  # Altura de la barra (valor de la barra)
    width = p.get_width()  # Ancho de la barra (en caso de barras horizontales)
    x = p.get_x() + p.get_width() / 2  # Posición X para el texto
    y = p.get_y() + p.get_height() / 2  # Posición Y para el texto

    # Mostrar el número en el gráfico
    ax.text(x, y, str(int(height)), ha='center', va='center', fontsize=10, color='black')

# Mostrar el gráfico
plt.tight_layout()
plt.show()

