import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios
data = np.random.rand(4, 4)

# Crear la gráfica de calor
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()  # Agregar barra de color para referencia
plt.show()