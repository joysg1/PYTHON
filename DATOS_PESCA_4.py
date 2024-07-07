
import matplotlib.pyplot as plt
import pandas as pd

# Datos
data = {
    'Año': [2000, 2005, 2010, 2015, 2020, 2021],
    'CPUE Antes de Regulaciones (Flota Industrial)': [1.2, 1.1, None, None, None, None],
    'CPUE Después de Regulaciones (Flota Industrial)': [None, None, 1.0, 0.9, 0.8, 0.7],
    'CPUE Antes de Regulaciones (Flota Artesanal)': [0.8, 1.0, None, None, None, None],
    'CPUE Después de Regulaciones (Flota Artesanal)': [None, None, 1.2, 1.5, 1.8, 2.0]
}

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Crear el gráfico de líneas
plt.figure(figsize=(10, 6))

# Gráfico de CPUE flota industrial antes y después de regulaciones
plt.plot(df['Año'], df['CPUE Antes de Regulaciones (Flota Industrial)'], label='Antes de Regulaciones (Industrial)', linestyle='--', color='blue')
plt.plot(df['Año'], df['CPUE Después de Regulaciones (Flota Industrial)'], label='Después de Regulaciones (Industrial)', linestyle='-', color='blue')

# Gráfico de CPUE flota artesanal antes y después de regulaciones
plt.plot(df['Año'], df['CPUE Antes de Regulaciones (Flota Artesanal)'], label='Antes de Regulaciones (Artesanal)', linestyle='--', color='red')
plt.plot(df['Año'], df['CPUE Después de Regulaciones (Flota Artesanal)'], label='Después de Regulaciones (Artesanal)', linestyle='-', color='red')

# Añadir títulos y etiquetas
plt.xlabel('Año')
plt.ylabel('CPUE (Toneladas/Esfuerzo)')
plt.title('Impacto de las Regulaciones en la CPUE (2000-2021)')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
