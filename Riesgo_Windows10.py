import numpy as np
import matplotlib.pyplot as plt

# Definir las categorías de riesgo (meses del año)
categorias = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
              'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Definir los valores de riesgo para cada categoría (supongamos que son valores entre 0 y 100)
riesgo_valores = np.linspace(10, 90, len(categorias))  # El riesgo se incrementa de 10 a 90

# Calcular los ángulos para cada categoría
angulos = np.linspace(0, 2*np.pi, len(categorias), endpoint=False)

# Generar el gráfico radar
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
ax.plot(angulos, riesgo_valores, 'o-', linewidth=2, label='Riesgo de compilaciones antiguas')
ax.fill(angulos, riesgo_valores, alpha=0.3)

# Configurar el gráfico
ax.set_thetagrids(angulos * 180/np.pi, categorias)
ax.set_title('Riesgo de Compilaciones Antiguas de Windows 10 en 2025', va='bottom')
ax.set_rlabel_position(270)
ax.set_ylim(0, 100)  # Establecer el límite máximo del eje radial
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.show()
