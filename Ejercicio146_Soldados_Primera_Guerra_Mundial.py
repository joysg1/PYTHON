import matplotlib.pyplot as plt

# Datos de la cantidad de soldados por nacionalidad en la Primera Guerra Mundial
# (Nota: Estos datos son aproximados y pueden variar según la fuente)
datos = {
    'Alemania': 11000000,
    'Austria-Hungría': 7800000,
    'Bélgica': 267000,
    'Bulgaria': 1200000,
    'Canadá': 630000,
    'Estados Unidos': 115000,
    'Francia': 8410000,
    'Imperio Británico': 5700000,
    'Imperio Otomano': 2850000,
    'Italia': 5600000,
    'Japón': 800000,
    'Reino Unido': 5700000,
    'Rusia': 12000000,
    'Serbia': 707000
}

# Extraer las nacionalidades y la cantidad de soldados
nacionalidades = list(datos.keys())
cantidad_soldados = list(datos.values())

# Crear el gráfico de pastel
plt.figure(figsize=(10,8))  # Ajustar el tamaño del gráfico
plt.pie(cantidad_soldados, labels=nacionalidades, autopct='%1.1f%%', pctdistance=0.8)  # Ajustar la distancia de los porcentajes
plt.title('Cantidad de soldados por nacionalidad en la Primera Guerra Mundial')

# Crear la leyenda con las cantidades de soldados
leyenda = [f"{nacionalidad} ({cantidad/1000000:.1f} millones)" for nacionalidad, cantidad in zip(nacionalidades, cantidad_soldados)]
plt.legend(leyenda, loc='upper right', bbox_to_anchor=(1.3, 1))  # Agregar leyenda

plt.show()


