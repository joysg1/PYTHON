import numpy as np
import matplotlib.pyplot as plt

# Datos de las distribuciones de Linux
distribuciones = ['Ubuntu', 'Fedora', 'Arch Linux', 'Debian', 'Linux Mint']
facilidad_de_uso = [8, 7, 4, 6, 9]  # Escala del 1 al 10

# Número de variables
num_vars = len(distribuciones)

# Crear un ángulo para cada variable
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Completar el círculo
facilidad_de_uso += facilidad_de_uso[:1]
angles += angles[:1]

# Crear el gráfico
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, facilidad_de_uso, color='blue', alpha=0.25)
ax.plot(angles, facilidad_de_uso, color='blue', linewidth=2)

# Añadir etiquetas
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(distribuciones)

# Título
plt.title('Comparación de Distribuciones de Linux según Facilidad de Uso', size=15, color='blue', weight='bold')

# Mostrar el gráfico
plt.show()
