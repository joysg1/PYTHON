import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# URL del conjunto de datos de propinas
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

# Cargar el conjunto de datos desde la URL
tips_data = pd.read_csv(url)

# Crear una gráfica de calor de la relación entre el total de la cuenta y la propina por día y tamaño del grupo
heatmap_data = tips_data.pivot_table(index='day', columns='size', values='tip', aggfunc=np.mean)

# Crear una gráfica de calor
plt.figure(figsize=(10, 6))
plt.imshow(heatmap_data, cmap='YlGnBu', aspect='auto', interpolation='nearest', norm=mcolors.PowerNorm(gamma=0.5))
plt.colorbar(label='Propina ($)')
plt.title('Heatmap: Total de la cuenta vs Propina por Tamaño del Grupo')
plt.xlabel('Tamaño del Grupo')
plt.ylabel('Día de la Semana')
plt.xticks(ticks=np.arange(len(heatmap_data.columns)), labels=heatmap_data.columns)
plt.yticks(ticks=np.arange(len(heatmap_data.index)), labels=heatmap_data.index)
plt.show()

# Crear una gráfica de dispersión (puntos) de total de la cuenta vs propina
plt.figure(figsize=(10, 6))
plt.scatter(tips_data['total_bill'], tips_data['tip'], c=pd.factorize(tips_data['sex'])[0], cmap='Set1', alpha=0.6)
plt.colorbar(label='Sexo')
plt.title('Gráfico de Dispersión: Total de la cuenta vs Propina')
plt.xlabel('Total de la Cuenta ($)')
plt.ylabel('Propina ($)')
plt.show()
