import matplotlib.pyplot as plt

# Definir la cantidad de memoria disponible en el dispositivo
memoria_disponible = [8, 7, 6, 5, 4, 3, 2, 1]

# Definir la duración del proceso de la aplicación en función de la cantidad de memoria disponible
duracion_proceso = [120, 100, 80, 60, 40, 20, 10, 5]

# Crear un gráfico lineal
plt.figure(figsize=(8, 6))
plt.plot(memoria_disponible, duracion_proceso, marker='o')

# Agregar título y etiquetas de eje
plt.title('Duración del proceso de la aplicación en función de la cantidad de memoria disponible')
plt.xlabel('Memoria disponible (GB)')
plt.ylabel('Duración del proceso (segundos)')

# Agregar leyenda en la parte superior izquierda dentro del gráfico
plt.text(1, 110, '**La duración del proceso disminuye a medida que la memoria disponible disminuye.**', ha='left', va='top', fontsize=10)
plt.text(1, 100, '**Cuando la memoria disponible es baja, la aplicación puede experimentar problemas de rendimiento o cerrarse.**', ha='left', va='top', fontsize=10)

# Mostrar el gráfico
plt.show()









