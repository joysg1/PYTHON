import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generamos una muestra de datos aleatorios
np.random.seed(0)
datos = np.random.normal(loc=0, scale=1, size=1000)

# Creamos el histograma de la distribución empírica
sns.set()
plt.hist(datos, bins=30, density=True)

# Agregamos título y etiquetas
plt.title('Distribución Empírica')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

# Mostramos el gráfico
plt.show()
