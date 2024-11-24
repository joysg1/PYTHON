import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
# Reemplaza 'archivo.csv' con la ruta de tu archivo CSV
df = pd.read_csv('drug200.csv')

# Filtrar los datos de personas con presión arterial alta
df_filtered = df[df['BP'] == 'HIGH']

# Contar el número de mujeres y hombres que usan cada droga
drug_gender_count = df_filtered.groupby(['Drug', 'Sex']).size().unstack(fill_value=0)

# Generar el gráfico de barras horizontales
plt.figure(figsize=(10, 6))
ax = drug_gender_count.plot(kind='barh', stacked=False, 
                            color=['#FFB88C', '#A2C2E1'], edgecolor='black')

# Agregar etiquetas y título
plt.title('Número de Mujeres y Hombres que usan cada Droga y tienen Presión Alta')
plt.xlabel('Número de Personas')
plt.ylabel('Droga')
plt.xticks(rotation=0)
plt.legend(title='Género', loc='upper right', labels=['Mujeres', 'Hombres'])

# Agregar los números encima de cada barra
for p in ax.patches:
    ax.annotate(f'{p.get_width()}', 
                (p.get_x() + p.get_width(), p.get_y() + p.get_height() / 2), 
                xytext=(5, 0),  # Desplazamiento horizontal
                textcoords='offset points',
                ha='left', va='center', color='black')

# Mostrar el gráfico
plt.show()



