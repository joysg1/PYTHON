import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Datos históricos
años = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024]).reshape(-1, 1)
desgaste = np.array([5, 12, 20, 30, 45, 60, 78])  # en %

# Regresión polinómica de grado 2
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(años)
modelo = LinearRegression()
modelo.fit(X_poly, desgaste)

# Años extendidos hasta 2030
años_todos = np.arange(2018, 2031).reshape(-1, 1)
X_todos_poly = poly.transform(años_todos)
desgaste_predicho = modelo.predict(X_todos_poly)

# Limitar desgaste al 100%
desgaste_predicho = np.clip(desgaste_predicho, 0, 100)

# Crear gráfico de área
plt.figure(figsize=(10, 6))
plt.fill_between(años_todos.flatten(), desgaste_predicho, color='darkred', alpha=0.6)

# Dibujar la curva encima del área
plt.plot(años_todos.flatten(), desgaste_predicho, color='black', linestyle='--', label='Tendencia proyectada')

# Etiquetas
plt.title('Predicción del Desgaste de Discos Duros por Corriente Eléctrica (2018–2030)')
plt.xlabel('Año')
plt.ylabel('Desgaste (%)')
plt.ylim(0, 105)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
