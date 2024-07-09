

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos originales con NaN
data = {
    'Año': [2000, 2005, 2010, 2015, 2020, 2021],
    'CPUE Antes de Regulaciones (Flota Industrial)': [1.2, 1.1, np.nan, np.nan, np.nan, np.nan],
    'CPUE Después de Regulaciones (Flota Industrial)': [np.nan, np.nan, 1.0, 0.9, 0.8, 0.7],
    'CPUE Antes de Regulaciones (Flota Artesanal)': [0.8, 1.0, np.nan, np.nan, np.nan, np.nan],
    'CPUE Después de Regulaciones (Flota Artesanal)': [np.nan, np.nan, 1.2, 1.5, 1.8, 2.0]
}

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Llenar NaN con la mediana
df_filled = df.copy()
df_filled.fillna(df.median(), inplace=True)

# Crear el modelo de regresión lineal para CPUE Industrial después de regulaciones
model_industrial_after = LinearRegression()
X_industrial = df_filled[['Año']]
y_industrial = df_filled['CPUE Después de Regulaciones (Flota Industrial)']
model_industrial_after.fit(X_industrial, y_industrial)

# Predecir para todos los años desde 2000 hasta 2124
pred_years = np.arange(2000, 2125)  # Rango extendido de años para predecir
pred_industrial_after = model_industrial_after.predict(pred_years.reshape(-1, 1))

# Crear el modelo de regresión lineal para CPUE Artesanal después de regulaciones
model_artesanal_after = LinearRegression()
X_artesanal = df_filled[['Año']]
y_artesanal = df_filled['CPUE Después de Regulaciones (Flota Artesanal)']
model_artesanal_after.fit(X_artesanal, y_artesanal)

# Predecir para todos los años desde 2000 hasta 2124
pred_artesanal_after = model_artesanal_after.predict(pred_years.reshape(-1, 1))

# Crear el gráfico de líneas
plt.figure(figsize=(12, 8))

# Gráfico de CPUE flota industrial después de regulaciones
plt.plot(df['Año'], df['CPUE Después de Regulaciones (Flota Industrial)'].fillna(method='ffill'), label='Datos reales (Industrial)', linestyle='-', color='blue')
plt.plot(pred_years, pred_industrial_after, label='Predicción (Industrial)', linestyle='--', color='blue')

# Gráfico de CPUE flota artesanal después de regulaciones
plt.plot(df['Año'], df['CPUE Después de Regulaciones (Flota Artesanal)'].fillna(method='ffill'), label='Datos reales (Artesanal)', linestyle='-', color='green')
plt.plot(pred_years, pred_artesanal_after, label='Predicción (Artesanal)', linestyle='--', color='green')

# Añadir títulos y etiquetas
plt.xlabel('Año')
plt.ylabel('CPUE (Toneladas/Esfuerzo)')
plt.title('Predicción de CPUE desde el 2024 hasta el 2124')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()



