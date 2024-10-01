import matplotlib.pyplot as plt
import numpy as np

# Datos
metricas = [
    'Correctamente Clasificados', 
    'Incorrectamente Clasificados', 
    'Kappa', 
    'Error Absoluto Medio', 
    'Raíz del Error Cuadrático Medio'
]

entrenamiento = [36, 7, 0.7512, 0.1545, 0.2779]
prueba = [23, 5, 0.7282, 0.1472, 0.2749]

# Configuración de las barras
x = np.arange(len(metricas))
width = 0.35  # Ancho de las barras

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
bars1 = plt.bar(x - width/2, entrenamiento, width, label='Set de Entrenamiento', color='#A8E6CF')
bars2 = plt.bar(x + width/2, prueba, width, label='Set de Prueba', color='#FF8C94')

# Agregar etiquetas y título
plt.ylabel('Valores', fontsize=12, fontweight='bold')
plt.title('Comparación de Métricas entre Set de Entrenamiento y Set de Prueba', fontweight='bold', fontsize=14)
plt.xticks(x, metricas, fontsize=9, fontweight='bold', rotation=45, ha='right')
plt.legend(fontsize=10)

# Ajustar los límites del eje y
plt.ylim(0, 40)  # Ajustar el rango del eje y

# Agregar valores encima de las barras
for bar in bars1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 4), ha='center', va='bottom', fontsize=10, fontweight='bold')

for bar in bars2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 4), ha='center', va='bottom', fontsize=10, fontweight='bold')

# Ajustar el layout y mostrar el gráfico
plt.tight_layout()
plt.show()









