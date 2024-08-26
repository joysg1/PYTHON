import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# Definimos la tasa media de sucesos
lambda_ = 5

# Generamos una serie de números enteros no negativos que siguen una distribución de Poisson
k = np.arange(0, 20)
probabilidades = poisson.pmf(k, lambda_)

# Creamos el gráfico de barras
sns.set()
plt.bar(k, probabilidades)

# Agregamos título y etiquetas
plt.title('Distribución de Poisson')
plt.xlabel('Número de sucesos')
plt.ylabel('Probabilidad')

# Mostramos el gráfico
plt.show()

