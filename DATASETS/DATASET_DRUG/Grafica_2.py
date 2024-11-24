import matplotlib.pyplot as plt
import numpy as np

# Definir las clases
classes = ['DrugY', 'drugC', 'drugX', 'drugA', 'drugB']

# Tasa de aciertos (TP Rate) por clase (todas son 1.0 según el resumen proporcionado)
tp_rate = [1.0, 1.0, 1.0, 1.0, 1.0]

# Crear un gráfico de barras para mostrar la tasa de aciertos (TP Rate) por clase
plt.figure(figsize=(8, 6))
plt.bar(classes, tp_rate, color='skyblue', alpha=0.7)

# Añadir detalles al gráfico
plt.title('Tasa de Aciertos por Clase (TP Rate)', fontsize=16)
plt.xlabel('Clase', fontsize=14)
plt.ylabel('Tasa de Aciertos (TP Rate)', fontsize=14)
plt.ylim(0, 1.1)  # Limitar el rango del eje y entre 0 y 1

# Mostrar el valor de la tasa de aciertos en cada barra
for i in range(len(tp_rate)):
    plt.text(i, tp_rate[i] + 0.02, f'{tp_rate[i]:.2f}', ha='center', va='bottom', fontsize=12)

# Mostrar el gráfico
plt.show()


