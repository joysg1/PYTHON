
import matplotlib.pyplot as plt
import pandas as pd

# Datos
data = {
    'Año': [2000, 2005, 2010, 2015, 2020, 2021],
    'CPUE Flota Industrial': [1.2, 1.1, 1.0, 0.9, 0.8, 0.7],
    'CPUE Flota Artesanal': [0.8, 1.0, 1.2, 1.5, 1.8, 2.0]
}

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Crear el gráfico de barras agrupadas
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35

# Posiciones de las barras
bar1 = range(len(df['Año']))
bar2 = [x + bar_width for x in bar1]

# Crear las barras
plt.bar(bar1, df['CPUE Flota Industrial'], color='b', width=bar_width, label='CPUE Flota Industrial')
plt.bar(bar2, df['CPUE Flota Artesanal'], color='r', width=bar_width, label='CPUE Flota Artesanal')

# Añadir títulos y etiquetas
plt.xlabel('Año')
plt.ylabel('CPUE (Toneladas/Esfuerzo)')
plt.title('Comparación de CPUE entre Flota Industrial y Artesanal (2000-2021)')
plt.xticks([r + bar_width/2 for r in range(len(df['Año']))], df['Año'])
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
