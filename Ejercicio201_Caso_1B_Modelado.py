import matplotlib.pyplot as plt
import numpy as np

# Datos
carreras = ['Ingeniería', 'Economía', 'Derecho']
correctas = [9, 10, 17]  # Instancias clasificadas correctamente
incorrectas = [4, 3, 0]   # Instancias clasificadas incorrectamente
porcentajes = [69.2, 76.9, 100]  # Porcentaje de precisión

# Configuración de las barras
x = np.arange(len(carreras))
width = 0.35  # Ancho de las barras

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
bars1 = plt.bar(x - width/2, correctas, width, label='Clasificaciones Correctas', color='#A8E6CF')
bars2 = plt.bar(x + width/2, incorrectas, width, label='Clasificaciones Incorrectas', color='#FF8C94')

# Agregar etiquetas y título
plt.ylabel('Número de Instancias')
plt.title('Clasificaciones por Carrera Universitaria', fontweight='bold')
plt.xticks(x, carreras)

# Crear leyenda con porcentajes de precisión
leyenda = [f"{carrera} (Precisión: {prec}% )" for carrera, prec in zip(carreras, porcentajes)]
plt.legend(leyenda)

# Agregar valores encima de las barras
for bar in bars1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, yval, ha='center', va='bottom', fontsize=12)

for bar in bars2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, yval, ha='center', va='bottom', fontsize=12)

# Agregar precisión al medio de las barras
for i in range(len(carreras)):
    plt.text(x[i], (correctas[i] + incorrectas[i]) / 2, f"{porcentajes[i]}%", ha='center', va='center', fontsize=14, fontweight='bold')

# Mostrar el gráfico
plt.tight_layout()
plt.show()


