import matplotlib.pyplot as plt
import pandas as pd

# Datos
data = {
    'Año': [2000, 2005, 2010, 2015, 2020, 2021],
    'Desembarques Totales (Toneladas)': [10000, 9000, 8500, 7000, 6000, 5500],
    'CPUE Flota Industrial (Toneladas/Esfuerzo)': [1.2, 1.1, 1.0, 0.9, 0.8, 0.7],
    'CPUE Flota Artesanal (Toneladas/Esfuerzo)': [0.8, 1.0, 1.2, 1.5, 1.8, 2.0]
}

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Crear el gráfico
plt.figure(figsize=(10, 6))

# Gráfico de desembarques totales
plt.plot(df['Año'], df['Desembarques Totales (Toneladas)'], label='Desembarques Totales (Toneladas)', marker='o')

# Gráfico de CPUE flota industrial
plt.plot(df['Año'], df['CPUE Flota Industrial (Toneladas/Esfuerzo)'], label='CPUE Flota Industrial', marker='o')

# Gráfico de CPUE flota artesanal
plt.plot(df['Año'], df['CPUE Flota Artesanal (Toneladas/Esfuerzo)'], label='CPUE Flota Artesanal', marker='o')

# Añadir títulos y etiquetas
plt.title('Tendencias de Desembarques y Eficiencia de Captura de Camarón en el Puerto de Vacamonte (2000-2021)')
plt.xlabel('Año')
plt.ylabel('Toneladas / Toneladas por Esfuerzo')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()