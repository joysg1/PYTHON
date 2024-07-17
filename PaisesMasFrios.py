
import matplotlib.pyplot as plt

# Datos de ejemplo: países más fríos con sus temperaturas promedio (en grados Celsius)
paises = ['Antártida', 'Rusia', 'Canadá', 'Groenlandia', 'Kazajistán', 'Islandia', 'Noruega']
temperaturas_promedio = [-49, -5.5, -5, -9, -6.8, 1.2, 3.7]  # Ejemplo de temperaturas en grados Celsius

# Colores para cada barra
colores = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta']

# Crear el gráfico de barras horizontales
plt.figure(figsize=(10, 8))  # Tamaño del gráfico

# Graficar los países y sus temperaturas
bars = plt.barh(paises, temperaturas_promedio, color=colores)

# Añadir etiquetas con los valores de temperatura al lado de cada barra
for bar, temp in zip(bars, temperaturas_promedio):
    plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, str(temp) + '°C',
             ha='center', va='center', color='black', fontsize=10)

# Personalización del gráfico
plt.xlabel('Temperatura promedio anual (°C)')
plt.ylabel('Países')
plt.title('Países más fríos del mundo')
plt.xlim(-50, 5)  # Establecer límites para el eje x
plt.grid(True)  # Habilitar cuadrícula

# Mostrar el gráfico
plt.tight_layout()  # Ajustar diseño
plt.show()
