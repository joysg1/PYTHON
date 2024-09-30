import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargamos el dataset
dataset = pd.DataFrame({
    'Familia': ['DEPORTIVO', 'DEPORTIVO', 'DEPORTIVO', 'DEPORTIVO', 'DEPORTIVO', 'LONA'],
    'Sexo': ['CABALLERO', 'CABALLERO', 'NINO', 'MUJER', 'MUJER', 'MUJER'],
    'Marca': ['ASICS', 'PUMA', 'PUMA', 'PUMA', 'FILA', 'CONVERSE'],
    'Compras_Uds': [4802.0, 2201.0, 800.0, 4000.0, 2500.0, 1800.0],
    'Ventas_2017': [231.0, 2.0, 159.0, 50.0, 108.0, 65.0],
    'Nivel_de_stock': ['Altisimo', 'Alto', 'Medio', 'Altisimo', 'Alto', 'Medio'],
    'Criterio_de_reabastecimiento_en_6_meses': ['NO', 'NO', 'SI', 'NO', 'NO', 'SI']
})

# Calculamos la media de las compras por sexo y familia
compras_por_sexo = dataset.groupby('Sexo')['Compras_Uds'].mean()
compras_por_familia = dataset.groupby('Familia')['Compras_Uds'].mean()

# Calculamos la tasa de crecimiento anual
tasa_crecimiento = 0.05  # 5% de crecimiento anual

# Creamos un gráfico de barras que muestra la media de las compras por sexo y familia en cada año entre 2017 y 2022
anos = np.arange(2017, 2023)

# Graficamos las compras por sexo
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
bar_width = 0.2
for i, (sexo, valor) in enumerate(compras_por_sexo.items()):
    valores = [valor * (1 + tasa_crecimiento)**j for j in range(6)]
    plt.bar(anos + i * bar_width, valores, width=bar_width, label=sexo)
    for j, v in enumerate(valores):
        plt.text(anos[j] + i * bar_width, v + 10, str(round(v, 2)), ha='center')
plt.xlabel('Año')
plt.ylabel('Compras UDS')
plt.title('Media de las compras por sexo')
plt.legend()

# Graficamos las compras por familia
plt.subplot(1, 2, 2)
bar_width = 0.2
for i, (familia, valor) in enumerate(compras_por_familia.items()):
    valores = [valor * (1 + tasa_crecimiento)**j for j in range(6)]
    plt.bar(anos + i * bar_width, valores, width=bar_width, label=familia)
    for j, v in enumerate(valores):
        plt.text(anos[j] + i * bar_width, v + 10, str(round(v, 2)), ha='center')
plt.xlabel('Año')
plt.ylabel('Compras UDS')
plt.title('Media de las compras por familia')
plt.legend()

plt.tight_layout()
plt.show()






