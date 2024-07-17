
import matplotlib.pyplot as plt

# Datos de ejemplo (amenazas web y su nivel de peligrosidad)
amenazas = ['Malware', 'Phishing', 'Ransomware', 'Inyección SQL', 'Cross-Site Scripting (XSS)',
            'Man-in-the-Middle (MitM) Attack', 'Drive-by Downloads', 'Cryptojacking', 'Botnets']
peligrosidad = [9, 8, 7, 6, 7, 7, 6, 8, 7]  # Niveles de peligrosidad (escala del 1 al 10)

# Crear el gráfico de barras verticales
plt.figure(figsize=(12, 8))  # Aumentar el tamaño de la figura
bars = plt.bar(amenazas, peligrosidad, color='red')  # Cambio de color a rojo
plt.ylabel('Nivel de peligrosidad')
plt.title('Amenazas Web Más Peligrosas')

# Rotar las etiquetas del eje x y ajustar la alineación
plt.xticks(rotation=45, ha='right', fontsize=10)  

# Agregar etiquetas en las barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 1), ha='center', va='bottom', fontsize=9)

plt.grid(axis='y')  # Agregar rejilla solo en el eje y
plt.tight_layout()  # Ajustar el diseño automáticamente
plt.show()
