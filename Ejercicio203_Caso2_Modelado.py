import matplotlib.pyplot as plt
import numpy as np

# Datos
marcas = ['Asics', 'Puma (Caballero)', 'Puma (Niño)', 'Puma (Mujer)', 'Fila (Mujer)', 'Converse (Mujer)']
compras = [4802, 2201, 800, 4000, 2500, 1800]
sexos = ['Caballero', 'Caballero', 'Niño', 'Mujer', 'Mujer', 'Mujer']
reabastecimiento = ['NO', 'NO', 'SI', 'NO', 'NO', 'SI']

# Crear gráfico de barras
plt.figure(figsize=(12, 6))

# Crear barras
bars = plt.bar(marcas, compras, color=['blue' if r == 'NO' else 'orange' for r in reabastecimiento])

# Añadir etiquetas y título
plt.title('Compras por Marca, Sexo y Criterio de Reabastecimiento', fontsize=16, fontweight='bold')
plt.xlabel('Marca y Sexo', fontsize=14, fontweight='bold')
plt.ylabel('Compras (uds)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, fontweight='bold')

# Añadir valores y criterios de reabastecimiento en las barras
for bar, compra, r in zip(bars, compras, reabastecimiento):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{compra} ({r})', ha='center', va='bottom', fontweight='bold')

plt.grid(axis='y')

# Mostrar gráfico
plt.tight_layout()
plt.show()



