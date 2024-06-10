import matplotlib.pyplot as plt
import numpy as np

# Generar datos de prueba de ventas (por ejemplo, 1000 ventas aleatorias)
num_ventas = 1000
ventas = np.random.normal(loc=100, scale=50, size=num_ventas)  # Distribución normal con media 100 y desviación estándar 50

# Crear histograma
plt.hist(ventas, bins=30, edgecolor='black')  # Histograma con 30 contenedores
plt.title('Histograma de Ventas')
plt.xlabel('Monto de Venta')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()


#video 101 min 6