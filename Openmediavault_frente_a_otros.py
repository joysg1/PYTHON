import matplotlib.pyplot as plt

# Datos
labels = ['Synology', 'QNAP', 'Western Digital', 'Seagate', 'OpenMediaVault', 'TrueNAS', 'Unraid', 'Otros']
sizes = [25, 20, 15, 10, 5, 5, 5, 15]
colors = ['#66b3ff', '#99ff99', '#ffcc99', '#ff9999', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#f0c2c2']

# Crear gráfico de pastel
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Participación de mercado de soluciones NAS (2024)')
plt.axis('equal')  # Para que el gráfico sea un círculo perfecto
plt.tight_layout()
plt.show()
