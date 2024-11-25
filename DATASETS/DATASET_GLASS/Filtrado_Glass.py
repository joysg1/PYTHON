import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("glass.csv")

# Seleccionar las características de interés para el análisis
features = ['Fe', 'Mg', 'K', 'Na']

# Filtrar el vidrio con el mayor porcentaje de cada característica por tipo de vidrio
max_elements = df[features].max()  # Encuentra el valor máximo de cada característica
max_elements_df = df.loc[df[features].idxmax()]  # Obtén la fila del vidrio con los máximos valores

# Agrupar por tipo de vidrio y tomar el vidrio con el valor máximo de cada elemento
df_grouped_max = df.groupby('Type')[features].max()

# Crear el gráfico de barras apiladas
ax = df_grouped_max.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='YlGnBu')

# Títulos y etiquetas
plt.title('Tendencia en la composición química por tipo de vidrio', fontsize=16)
plt.xlabel('Tipo de Vidrio', fontsize=12)
plt.ylabel('Porcentaje de Composición (%)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Características', bbox_to_anchor=(1.05, 1), loc='upper left')

# Mostrar el gráfico
plt.tight_layout()  # Para que las etiquetas no se corten
plt.show()


