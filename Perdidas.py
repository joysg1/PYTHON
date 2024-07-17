import matplotlib.pyplot as plt

# Datos de ejemplo (pérdidas globales por falta de auditoría disminuyendo y luego estabilizándose)
years = list(range(2000, 2024))  # Años desde 2000 hasta el año actual
perdidas_globales = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 18, 16, 14, 12, 10, 8, 6]

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(years, perdidas_globales, color='r', marker='o', s=100, alpha=0.8, label='Pérdidas Globales por Falta de Auditoría')
plt.xlabel('Año')
plt.ylabel('Pérdidas Globales (en millones de dólares)')
plt.title('Pérdidas Globales por Falta de Auditoría (2000-2023)')
plt.xticks(years, rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
