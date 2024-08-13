
import matplotlib.pyplot as plt

# Datos aproximados de civiles afectados por nación durante la Primera Guerra Mundial
datos = {
    'Alemania': 420000,
    'Austria-Hungría': 400000,
    'Bélgica': 23000,
    'Bulgaria': 100000,
    'Francia': 40000,
    'Imperio Británico': 107000,
    'Imperio Ruso': 300000,
    'Italia': 100000
}

# Definir los colores para cada bando
colores = {
    'Aliados': 'blue',
    'Potencias Centrales': 'black'
}

# Asignar un bando a cada nación
bandos = {
    'Alemania': 'Potencias Centrales',
    'Austria-Hungría': 'Potencias Centrales',
    'Bélgica': 'Aliados',
    'Bulgaria': 'Potencias Centrales',
    'Francia': 'Aliados',
    'Imperio Británico': 'Aliados',
    'Imperio Ruso': 'Aliados',
    'Italia': 'Aliados'
}

# Extraer las naciones y la cantidad de civiles afectados
naciones = list(datos.keys())
civiles_afectados = list(datos.values())

# Crear el gráfico
plt.figure(figsize=(10, 6))
for i, nacion in enumerate(naciones):
    plt.bar(nacion, civiles_afectados[i], color=colores[bandos[nacion]])
plt.xlabel('Nación')
plt.ylabel('Cantidad de civiles afectados')
plt.title('Civiles afectados por nación durante la Primera Guerra Mundial')
plt.xticks(rotation=45)  # Rotar las etiquetas de las naciones para que sean más legibles
plt.tight_layout()  # Ajustar el tamaño del gráfico para que las etiquetas no se corten

# Agregar una leyenda para explicar los colores
plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', label='Aliados', markerfacecolor='blue', markersize=10),
                      plt.Line2D([0], [0], marker='o', color='w', label='Potencias Centrales', markerfacecolor='black', markersize=10)],
           loc='upper right', title='Bandos')

plt.show()
