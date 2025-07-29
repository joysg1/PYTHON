import numpy as np
import matplotlib.pyplot as plt

# Años de proyección
años = np.arange(2024, 2031)

# Simulación de datos de concentración de gases nobles (en partes por millón, ppm)
# Estos son datos ficticios para la demostración
concentraciones = np.array([0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5])  # Ejemplo de datos

# Calcular el área bajo la curva usando la regla del trapecio
area = np.trapz(concentraciones, años)

# Graficar los datos
plt.figure(figsize=(10, 6))
plt.plot(años, concentraciones, marker='o', label='Concentración de Gases Nobles (ppm)')
plt.fill_between(años, concentraciones, alpha=0.3)

# Añadir los valores en cada punto
for i, valor in enumerate(concentraciones):
    plt.text(años[i], valor, f'{valor:.1f}', fontsize=10, ha='center', va='bottom')

plt.title('Proyección de Gases Nobles en el Aire (2024-2030)')
plt.xlabel('Año')
plt.ylabel('Concentración (ppm)')
plt.xticks(años)
plt.grid()
plt.legend()
plt.show()

# Imprimir el área bajo la curva
print(f'El área bajo la curva de gases nobles de 2024 a 2030 es: {area:.2f} ppm-año')
