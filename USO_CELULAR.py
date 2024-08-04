import matplotlib.pyplot as plt

# Datos ficticios: Años y número de usuarios (en millones)
años = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
usuarios = [1500, 1600, 1700, 1800, 2000, 2200, 2400, 2600, 2800]  # En millones

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(años, usuarios, marker='o', linestyle='-', color='b', label='Número de Usuarios (millones)')
plt.title('Aumento del Uso de Smartphones desde 2015')
plt.xlabel('Año')
plt.ylabel('Número de Usuarios (millones)')
plt.grid(True)
plt.legend()
plt.xticks(años, rotation=45)
plt.tight_layout()

# Mostrar el gráfico
plt.show()
