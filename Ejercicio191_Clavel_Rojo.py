import matplotlib.pyplot as plt
import numpy as np

def draw_clavel():
    fig, ax = plt.subplots(figsize=(8, 8))

    # Configura el área de la gráfica
    ax.set_xlim(-2, 2)
    ax.set_ylim(0, 3)
    ax.set_aspect('equal')
    ax.axis('off')

    # Función para dibujar un pétalo
    def draw_petal(center_x, center_y, radius, angle_shift):
        angles = np.linspace(0, 2 * np.pi, 100)
        petal_shape_x = radius * (0.5 * np.cos(angles) + 0.5)
        petal_shape_y = radius * np.sin(angles)
        x = center_x + petal_shape_x * np.cos(angle_shift) - petal_shape_y * np.sin(angle_shift)
        y = center_y + petal_shape_x * np.sin(angle_shift) + petal_shape_y * np.cos(angle_shift)
        ax.fill(x, y, color='red', edgecolor='black')

    # Dibuja múltiples pétalos
    num_petals = 8
    petal_radius = 0.7
    petal_center_x = 0
    petal_center_y = 1.5
    for i in range(num_petals):
        angle_shift = (2 * np.pi / num_petals) * i
        draw_petal(petal_center_x, petal_center_y, petal_radius, angle_shift)

    # Dibuja el centro del clavel
    center_circle = plt.Circle((0, 1.5), 0.3, color='black')
    ax.add_patch(center_circle)

    # Dibuja el tallo desde el final de los pétalos hacia abajo
    stem_x = np.array([0, 0])
    stem_y = np.array([0, 1.0])  # Ajusta para que el tallo comience justo al final de los pétalos
    ax.plot(stem_x, stem_y, color='green', linewidth=6)

    # Dibuja una hoja muy pequeña al lado del tallo
    def draw_leaf(center_x, center_y, width, height, angle):
        leaf_angles = np.linspace(0, 2 * np.pi, 100)
        leaf_shape_x = width * np.cos(leaf_angles)
        leaf_shape_y = height * np.sin(leaf_angles)
        x = center_x + leaf_shape_x * np.cos(angle) - leaf_shape_y * np.sin(angle)
        y = center_y + leaf_shape_x * np.sin(angle) + leaf_shape_y * np.cos(angle)
        ax.fill(x, y, color='green', edgecolor='black')

    # Parámetros de la hoja
    leaf_width = 0.2
    leaf_height = 0.4
    leaf_center_x = 0.3
    leaf_center_y = 0.5  # Ajustado para estar cerca del tallo
    leaf_angle = -np.pi / 6

    # Dibuja la hoja muy cerca del tallo
    draw_leaf(leaf_center_x, leaf_center_y, leaf_width, leaf_height, leaf_angle)

    plt.title("Lest we forget", fontsize=20, fontweight='bold', fontfamily="Palatino")

    plt.show()

if __name__ == "__main__":
    draw_clavel()




