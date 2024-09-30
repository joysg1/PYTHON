import numpy as np
import matplotlib.pyplot as plt

# Datos de instancias por cluster
clusters = ['Cluster 0', 'Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5']
instance_counts = [61, 55, 45, 38, 24, 26]

# Crear el gráfico de instancias por cluster
plt.figure(figsize=(10, 5))
bars = plt.bar(clusters, instance_counts, color='skyblue')

# Añadir números sobre las barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

plt.xlabel('Clusters')
plt.ylabel('Número de Instancias')
plt.title('Número de Instancias por Cluster')
plt.show()

# Datos de centroides para cada cluster
centroids = {
    'Cluster 0': [20.2459, 120.4918, 178.1967, 146.4262, 122.6393, 152.2295],
    'Cluster 1': [11.9273, 104.3091, 134.4, 125.4909, 102.5636, 124.3091],
    'Cluster 2': [3.8, 80.2667, 87.3778, 81.9111, 78.1111, 86.0444],
    'Cluster 3': [6.5263, 81.0263, 121.2105, 113.9737, 77.6053, 93.5263],
    'Cluster 4': [8.0833, 128.0417, 76.9583, 90.125, 139.0833, 106.375],
    'Cluster 5': [18.5, 172.4615, 90.6923, 114, 197.0385, 149.1538]
}

# Crear un gráfico de barras para los centroides
attribute_names = ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']
centroid_values = np.array(list(centroids.values()))

bar_width = 0.15  # Ancho de las barras
x = np.arange(len(attribute_names))  # Posiciones en el eje x

plt.figure(figsize=(12, 6))
for i in range(centroid_values.shape[0]):
    plt.bar(x + i * bar_width, centroid_values[i], width=bar_width, label=clusters[i])

# Añadir números sobre las barras
for i in range(centroid_values.shape[0]):
    for j, val in enumerate(centroid_values[i]):
        plt.text(j + i * bar_width, val + 5, round(val, 2), ha='center', va='bottom')

# Configuración del gráfico
plt.xlabel('Atributos')
plt.ylabel('Valores del Centroides')
plt.title('Centroides de Clusters')
plt.xticks(x + bar_width * (centroid_values.shape[0] - 1) / 2, attribute_names)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.ylim(0, 220)
plt.grid()
plt.tight_layout()  # Asegura que todo se ajuste bien en la figura
plt.show()



