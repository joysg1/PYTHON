import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Definimos la función de densidad de probabilidad de la distribución normal
media = 0
desviacion_estandar = 1
x = np.linspace(media - 3*desviacion_estandar, media + 3*desviacion_estandar, 100)
y = norm.pdf(x, media, desviacion_estandar)

# Creamos el gráfico
plt.plot(x, y)

# Agregamos título y etiquetas
plt.title('Distribución Normal')
plt.xlabel('Valor')
plt.ylabel('Densidad de Probabilidad')

# Mostramos el gráfico
plt.show()
