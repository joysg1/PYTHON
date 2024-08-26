import matplotlib.pyplot as plt
import numpy as np

# Definimos la distribución discreta
valores = [1, 2, 3, 4, 5]
probabilidades = [0.1, 0.2, 0.3, 0.2, 0.2]

# Creamos el gráfico de barras
plt.bar(valores, probabilidades)

# Agregamos título y etiquetas
plt.title('Distribución Discreta')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')

# Mostramos el gráfico
plt.show()
