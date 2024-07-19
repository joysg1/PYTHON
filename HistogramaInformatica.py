
import matplotlib.pyplot as plt
import numpy as np

# Datos ficticios de aportes de científicos a diferentes áreas de la informática
cientificos = ['Alan Turing', 'Grace Hopper', 'Tim Berners-Lee', 'Ada Lovelace']
areas = ['Algoritmos', 'Redes', 'Web', 'Programación']

# Matriz de aportes (valores ficticios para este ejemplo)
aportes = np.array([
    [5, 4, 3, 2],
    [3, 5, 2, 4],
    [4, 3, 5, 2],
    [2, 4, 3, 5]
])

fig, ax = plt.subplots()
im = ax.imshow(aportes, cmap='YlGn')

# Configuración de los ejes
ax.set_xticks(np.arange(len(areas)))
ax.set_yticks(np.arange(len(cientificos)))
ax.set_xticklabels(areas)
ax.set_yticklabels(cientificos)

# Rotación y alineación de etiquetas para que se vean mejor
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Crear anotaciones de texto
for i in range(len(cientificos)):
    for j in range(len(areas)):
        text = ax.text(j, i, aportes[i, j],
                       ha="center", va="center", color="black")

ax.set_title("Aportes de Científicos a la Informática")
fig.tight_layout()
plt.colorbar(im, ax=ax)
plt.show()
