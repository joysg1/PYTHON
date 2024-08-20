import matplotlib.pyplot as plt
import numpy as np

# Datos de los programas educativos
programas = ['Kig', 'KGeography', 'Kalzium', 'Tux Paint', 'GCompris', 'Scratch', 'GeoGebra', 'Stellarium', 'Celestia']
pesos = [10, 20, 30, 40, 50, 60, 80, 120, 200]

# Colores para las barras
colores = plt.cm.rainbow(np.linspace(0, 1, len(programas)))

# Crear el gráfico
plt.bar(programas, pesos, color=colores)

# Agregar etiquetas a las barras
for i, peso in enumerate(pesos):
    plt.text(i, peso + 5, str(peso) + ' MB', ha='center', va='bottom')

# Agregar título y etiquetas
plt.title('Relación de peso de los programas educativos de Edubuntu')
plt.xlabel('Programa')
plt.ylabel('Peso (MB)')

# Mostrar el gráfico
plt.show()
