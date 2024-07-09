import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Datos históricos
data = {
    'Año': [2000, 2005, 2010, 2015, 2020, 2021],
    'Desembarques Totales (Toneladas)': [10000, 9000, 8500, 7000, 6000, 5500],
    'CPUE Flota Industrial (Toneladas/Esfuerzo)': [1.2, 1.1, 1.0, 0.9, 0.8, 0.7],
    'CPUE Flota Artesanal (Toneladas/Esfuerzo)': [0.8, 1.0, 1.2, 1.5, 1.8, 2.0]
}

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Crear el modelo lineal y hacer predicciones para cada serie
model_desembarques = LinearRegression()
model_industrial = LinearRegression()
model_artesanal = LinearRegression()

# Ajustar el modelo para Desembarques Totales
model_desembarques.fit(df[['Año']], df['Desembarques Totales (Toneladas)'])

# Predicciones para Desembarques Totales
pred_desembarques = model_desembarques.predict(np.arange(2024, 2125).reshape(-1, 1))
# Introducir aleatoriedad
pred_desembarques += np.random.normal(0, 1000, pred_desembarques.shape)  # Desviación estándar de 1000

# Asegurar que las predicciones no sean menores que el mínimo valor histórico
min_desembarques = df['Desembarques Totales (Toneladas)'].min()
pred_desembarques = np.maximum(pred_desembarques, min_desembarques)

# Ajustar el modelo para CPUE Flota Industrial
model_industrial.fit(df[['Año']], df['CPUE Flota Industrial (Toneladas/Esfuerzo)'])

# Predicciones para CPUE Flota Industrial
pred_industrial = model_industrial.predict(np.arange(2024, 2125).reshape(-1, 1))
# Introducir aleatoriedad
pred_industrial += np.random.normal(0, 0.2, pred_industrial.shape)  # Desviación estándar de 0.2

# Ajustar el modelo para CPUE Flota Artesanal
model_artesanal.fit(df[['Año']], df['CPUE Flota Artesanal (Toneladas/Esfuerzo)'])

# Predicciones para CPUE Flota Artesanal
pred_artesanal = model_artesanal.predict(np.arange(2024, 2125).reshape(-1, 1))
# Introducir aleatoriedad
pred_artesanal += np.random.normal(0, 0.3, pred_artesanal.shape)  # Desviación estándar de 0.3

# Crear el gráfico
plt.figure(figsize=(10, 6))

# Gráfico de desembarques totales (histórico y predicción)
plt.plot(df['Año'], df['Desembarques Totales (Toneladas)'], label='Desembarques Totales (Histórico)', marker='o')
plt.plot(np.arange(2024, 2125), pred_desembarques, linestyle='--', color='blue', label='Desembarques Totales (Predicción)')

# Gráfico de CPUE flota industrial (histórico y predicción)
plt.plot(df['Año'], df['CPUE Flota Industrial (Toneladas/Esfuerzo)'], label='CPUE Flota Industrial (Histórico)', marker='o')
plt.plot(np.arange(2024, 2125), pred_industrial, linestyle='--', color='orange', label='CPUE Flota Industrial (Predicción)')

# Gráfico de CPUE flota artesanal (histórico y predicción)
plt.plot(df['Año'], df['CPUE Flota Artesanal (Toneladas/Esfuerzo)'], label='CPUE Flota Artesanal (Histórico)', marker='o')
plt.plot(np.arange(2024, 2125), pred_artesanal, linestyle='--', color='green', label='CPUE Flota Artesanal (Predicción)')

# Añadir títulos y etiquetas
plt.title('Tendencias de Desembarques y Eficiencia de Captura de Camarón en el Puerto de Vacamonte (2024-2124)')
plt.xlabel('Año')
plt.ylabel('Toneladas / Toneladas por Esfuerzo')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()



