import matplotlib.pyplot as plt
import numpy as np

# Definir las categorías de mejoras
categorias = ["Mejora en la planificación presupuestaria", "Optimización de recursos", "Mejora en la toma de decisiones", "Incremento en la eficiencia", "Mejora en la satisfacción del estudiante"]

# Definir los valores de las mejoras para cada año

valores_2024 = np.array([30, 35, 25, 20, 15])
valores_2025 = np.array([35, 40, 30, 25, 20])
valores_2026 = np.array([40, 45, 35, 30, 25])
valores_2027 = np.array([45, 50, 40, 35, 30])
valores_2028 = np.array([50, 55, 45, 40, 35])

# Crear el gráfico de línea

plt.plot(categorias, valores_2024, label='2024')
plt.plot(categorias, valores_2025, label='2025')
plt.plot(categorias, valores_2026, label='2026')
plt.plot(categorias, valores_2027, label='2027')
plt.plot(categorias, valores_2028, label='2028')

plt.xlabel("Categorías de mejoras")
plt.ylabel("Porcentaje de mejora")
plt.title("Proyección de mejoras a 5 años gracias a la aplicación del modelo de simulación")
plt.legend()
plt.show()




