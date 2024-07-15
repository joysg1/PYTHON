
import matplotlib.pyplot as plt
import numpy as np

# Datos de las vulnerabilidades
vulnerabilidades = [
    "Inyección SQL",
    "Cross-Site Scripting (XSS)",
    "Cross-Site Request Forgery (CSRF)",
    "Configuración de seguridad débil",
    "Vulnerabilidades en plugins",
    "Autenticación insuficiente",
    "Error de configuración HTTPS",
    "Falta de monitoreo de seguridad",
    "Desbordamiento de búfer",
    "Sesiones inseguras"
]

impacto = [9, 9, 9, 9, 9, 9, 9, 9, 8, 9]  # Impacto en una escala de 1 a 10
probabilidad = [10, 10, 10, 10, 10, 10, 10, 7, 7, 10]  # Probabilidad en una escala de 1 a 10

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots(figsize=(12, 8))

# Crear un gráfico de barras para el impacto
bar_width = 0.4
index = np.arange(len(vulnerabilidades))

bars1 = ax.bar(index, impacto, bar_width, label='Impacto', alpha=0.7, color='b')
bars2 = ax.bar(index + bar_width, probabilidad, bar_width, label='Probabilidad', alpha=0.7, color='r')

# Añadir etiquetas y título
ax.set_xlabel('Vulnerabilidades')
ax.set_ylabel('Puntuación')
ax.set_title('Análisis de Vulnerabilidades de la Página Web de Panasystem')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(vulnerabilidades, rotation=45, ha='right')
ax.legend()

# Añadir valores encima de las barras
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)

# Ajustar diseño para evitar superposiciones
plt.tight_layout()
plt.show()
