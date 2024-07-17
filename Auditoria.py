
import matplotlib.pyplot as plt

# Datos de ejemplo (impacto de la auditoría aumentando con los años)
years = list(range(2000, 2024))  # Años desde 2000 hasta el año actual
impacto = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5]

# Crear el gráfico de línea
plt.figure(figsize=(10, 6))
plt.plot(years, impacto, marker='o', linestyle='-', color='b', label='Impacto de la Auditoría')
plt.xlabel('Año')
plt.ylabel('Impacto (escala del 1 al 15)')
plt.title('Impacto de la Auditoría (2000-2023)')
plt.xticks(years, rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
