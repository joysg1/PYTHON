import matplotlib.pyplot as plt

# Datos de ejemplo: países y número de afectados
paises = ['Alemania', 'Rusia', 'Francia', 'Reino Unido', 'Imperio Austrohúngaro']
afectados = [2000000, 1750000, 1400000, 1200000, 1000000]

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.barh(paises, afectados, color='skyblue')
plt.xlabel('Número de afectados')
plt.title('Países más afectados en la Primera Guerra Mundial')
plt.gca().invert_yaxis()  # Invertir el eje y para ordenar de mayor a menor

# Mostrar el gráfico
plt.show()



