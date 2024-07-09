import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Datos de ejemplo
data = {
    'Año': [2000, 2005, 2010, 2015, 2020, 2021],
    'CPUE Flota Industrial': [1.2, 1.1, 1.0, 0.9, 0.8, 0.7],
    'CPUE Flota Artesanal': [0.8, 1.0, 1.2, 1.5, 1.8, 2.0]
}

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Función para ajustar las predicciones y evitar valores negativos
def ajustar_predicciones(pred, min_values):
    return np.maximum(pred, min_values)

# Crear modelos lineales y hacer predicciones para cada serie
model_industrial = LinearRegression()
model_artesanal = LinearRegression()

# Ajustar el modelo para CPUE Flota Industrial
model_industrial.fit(df[['Año']], df['CPUE Flota Industrial'])
pred_industrial_base = model_industrial.predict(np.arange(2024, 2125).reshape(-1, 1))

# Introducir aleatoriedad por década para CPUE Flota Industrial
pred_industrial = []
std_dev_industrial = 0.1  # Desviación estándar inicial
for year in range(2024, 2125):
    if (year - 2024) % 10 == 0:
        std_dev_industrial += np.random.uniform(-0.02, 0.02)  # Cambio aleatorio en desviación estándar cada década
    pred_industrial.append(pred_industrial_base[year - 2024] + np.random.normal(0, std_dev_industrial))

# Convertir a numpy array
pred_industrial = np.array(pred_industrial)

# Obtener el valor mínimo histórico para CPUE Flota Industrial
min_industrial = df['CPUE Flota Industrial'].min()

# Ajustar predicciones para CPUE Flota Industrial
pred_industrial = ajustar_predicciones(pred_industrial, min_industrial)

# Ajustar el modelo para CPUE Flota Artesanal
model_artesanal.fit(df[['Año']], df['CPUE Flota Artesanal'])
pred_artesanal_base = model_artesanal.predict(np.arange(2024, 2125).reshape(-1, 1))

# Introducir aleatoriedad por década para CPUE Flota Artesanal
pred_artesanal = []
std_dev_artesanal = 0.15  # Desviación estándar inicial
for year in range(2024, 2125):
    if (year - 2024) % 10 == 0:
        std_dev_artesanal += np.random.uniform(-0.03, 0.03)  # Cambio aleatorio en desviación estándar cada década
    pred_artesanal.append(pred_artesanal_base[year - 2024] + np.random.normal(0, std_dev_artesanal))

# Convertir a numpy array
pred_artesanal = np.array(pred_artesanal)

# Obtener el valor mínimo histórico para CPUE Flota Artesanal
min_artesanal = df['CPUE Flota Artesanal'].min()

# Ajustar predicciones para CPUE Flota Artesanal
pred_artesanal = ajustar_predicciones(pred_artesanal, min_artesanal)

# Crear el gráfico de líneas
plt.figure(figsize=(10, 6))

# Gráfico de líneas para CPUE Flota Industrial histórico
plt.plot(df['Año'], df['CPUE Flota Industrial'], marker='o', color='b', label='CPUE Flota Industrial (Histórico)')

# Gráfico de líneas para CPUE Flota Artesanal histórico
plt.plot(df['Año'], df['CPUE Flota Artesanal'], marker='o', color='r', label='CPUE Flota Artesanal (Histórico)')

# Gráfico de líneas para predicciones futuras de CPUE Flota Industrial
plt.plot(np.arange(2024, 2125), pred_industrial, linestyle='--', color='b', label='CPUE Flota Industrial (Predicción)')

# Gráfico de líneas para predicciones futuras de CPUE Flota Artesanal
plt.plot(np.arange(2024, 2125), pred_artesanal, linestyle='--', color='r', label='CPUE Flota Artesanal (Predicción)')

# Añadir títulos y etiquetas
plt.title('Predicción de CPUE entre Flota Industrial y Artesanal en el Puerto de Vacamonte (2024-2124)')
plt.xlabel('Año')
plt.ylabel('CPUE (Toneladas/Esfuerzo)')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()

