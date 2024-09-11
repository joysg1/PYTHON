import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Definir las áreas críticas a mejorar
areas_criticas = ["Planificación y gestión de la infraestructura", "Uso de recursos", "Experiencia del estudiante y docente", "Sostenibilidad", "Capacidad de respuesta a cambios"]

# Definir la importancia de cada área crítica (en una escala de 1 a 5)
importancia = [4, 4, 5, 4, 3]

# Definir la urgencia de cada área crítica (en una escala de 1 a 5)
urgencia = [5, 4, 5, 4, 3]

# Crear un heatmap de áreas críticas a mejorar
sns.set()
plt.figure(figsize=(12, 6))
sns.heatmap(np.array([importancia, urgencia]), cmap="coolwarm", annot=True, fmt="d", xticklabels=areas_criticas, yticklabels=["Importancia", "Urgencia"], cbar_kws={"shrink": 0.5})
plt.title("Heatmap de áreas críticas a mejorar en el Centro Regional de Panamá Oeste")
plt.xlabel("Áreas críticas")
plt.ylabel("")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

