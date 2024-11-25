import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("glass.csv")

# Definir un umbral para considerar un "alto porcentaje de magnesio"
umbral_magnesium = 3  # Puedes ajustar este valor según lo que consideres un porcentaje alto

# Filtrar los registros donde el porcentaje de magnesio es mayor al umbral
df_high_magnesium = df[df['Mg'] > umbral_magnesium]

# Contar cuántos registros por tipo de vidrio tienen un alto porcentaje de magnesio
magnesium_counts = df_high_magnesium['Type'].value_counts()

# Crear un gráfico de barras
plt.figure(figsize=(10, 6))
ax = magnesium_counts.plot(kind='bar', color='lightcoral')

# Añadir título y etiquetas
plt.title(f'Número de Registros con Alto Porcentaje de Magnesio (> {umbral_magnesium}%)', fontsize=16)
plt.xlabel('Tipo de Vidrio', fontsize=12)
plt.ylabel('Número de Registros', fontsize=12)
plt.xticks(rotation=45)

# Colocar los números en las barras
for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 0.1, 
            str(int(i.get_height())), ha='center', va='bottom', fontsize=12, fontweight='bold')

# Mostrar el gráfico
plt.tight_layout()
plt.show()

