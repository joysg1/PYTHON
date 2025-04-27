import matplotlib.pyplot as plt
import numpy as np

# Funciones de auditoría
labels = [
    'Registro de accesos',
    'Detección de cambios en archivos',
    'Alertas de seguridad',
    'Historial de configuraciones',
    'Monitorización de servicios'
]

# Importancia (de 1 a 10)
importance = [10, 9, 9, 8, 7]

# Preparar los datos para un radar
num_vars = len(labels)

# Repetimos el primer valor para cerrar el gráfico
values = importance + [importance[0]]

# Ángulos para cada eje
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Crear el gráfico
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Dibujar
ax.plot(angles, values, color='mediumslateblue', linewidth=2)
ax.fill(angles, values, color='mediumslateblue', alpha=0.4)

# Ajustar etiquetas
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)

# Rango del radar
ax.set_ylim(0, 10)

# Título
plt.title('Importancia de funciones de auditoría en OpenMediaVault', size=16, y=1.08)

# Mostrar
plt.tight_layout()
plt.show()

