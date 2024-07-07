import matplotlib.pyplot as plt
import pandas as pd

# Datos de ejemplo
data = {
    'Año': [2000, 2005, 2010, 2015, 2020, 2021],
    'Camarón Blanco (Toneladas)': [5000, 4500, 4200, 3500, 3000, 2750],
    'Camarón Tití (Toneladas)': [3000, 2700, 2550, 2100, 1800, 1650],
    'Camarón Rojo (Toneladas)': [2000, 1800, 1750, 1400, 1200, 1100]
}

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.25

# Posiciones de las barras
bar1 = range(len(df['Año']))
bar2 = [x + bar_width for x in bar1]
bar3 = [x + bar_width for x in bar2]

# Crear las barras
plt.bar(bar1, df['Camarón Blanco (Toneladas)'], color='b', width=bar_width, label='Camarón Blanco')
plt.bar(bar2, df['Camarón Tití (Toneladas)'], color='r', width=bar_width, label='Camarón Tití')
plt.bar(bar3, df['Camarón Rojo (Toneladas)'], color='g', width=bar_width, label='Camarón Rojo')

# Añadir títulos y etiquetas
plt.xlabel('Año')
plt.ylabel('Toneladas')
plt.title('Desembarques de Camarón por Especie en el Puerto de Vacamonte (2000-2021)')
plt.xticks([r + bar_width for r in range(len(df['Año']))], df['Año'])
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()