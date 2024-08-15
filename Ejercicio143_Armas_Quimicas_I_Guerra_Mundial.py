import matplotlib.pyplot as plt

# Datos históricos
total_afectados = 1300000
muertos = 90000

# Porcentaje de soldados afectados por armas químicas por bando
potencias_centrales = 0.55  # 55% de los soldados afectados pertenecían a las Potencias Centrales
aliados = 0.45  # 45% de los soldados afectados pertenecían a los Aliados

# Número de soldados afectados por bando
potencias_centrales_afectados = potencias_centrales * total_afectados
aliados_afectados = aliados * total_afectados

# Gráfico de barras
plt.bar(['Potencias Centrales'], [potencias_centrales_afectados], color='black')
plt.bar(['Aliados'], [aliados_afectados], color='blue')

# Agregar etiquetas de cantidad en las barras
plt.text(0, potencias_centrales_afectados + 10000, f"{int(potencias_centrales_afectados):,}", ha='center')
plt.text(1, aliados_afectados + 10000, f"{int(aliados_afectados):,}", ha='center')

plt.xlabel('Bando')
plt.ylabel('Número de soldados afectados')
plt.title('Soldados afectados por armas químicas en la Primera Guerra Mundial')
plt.show()

