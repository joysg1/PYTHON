import matplotlib.pyplot as plt

# Datos de los tanques ajustados
tanques = {
    'Potencias Centrales': {
        'A7V': 20
    },
    'Aliados': {
        'Mark IV': 6000,
        'Schneider CA1': 132,
        'Renault FT-17': 300  # Asumimos una cantidad para Renault FT-17, ya que no se especificó
    }
}

# Preparar los datos para el gráfico
modelos = []
cantidades = []
colores = []

for bando, modelos_tanques in tanques.items():
    for modelo, cantidad in modelos_tanques.items():
        modelos.append(modelo)
        cantidades.append(cantidad)
        colores.append('black' if bando == 'Potencias Centrales' else 'blue')

# Crear el gráfico de barras horizontales
plt.figure(figsize=(10, 6))
bars = plt.barh(modelos, cantidades, color=colores)

# Añadir texto en las barras
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, int(bar.get_width()), ha='left', va='center')

# Configurar el gráfico
plt.title('Tanques utilizados en la Primera Guerra Mundial')
plt.xlabel('Cantidad')
plt.ylabel('Modelos de Tanques')

# Añadir leyenda manualmente
plt.axvline(0, color='black', linewidth=0.5)  # Línea vertical para la leyenda
plt.scatter([], [], color='black', label='Potencias Centrales')  # Punto ficticio para la leyenda
plt.scatter([], [], color='blue', label='Aliados')  # Punto ficticio para la leyenda
plt.legend(loc='upper right', frameon=False)

# Mostrar el gráfico
plt.tight_layout()
plt.show()



