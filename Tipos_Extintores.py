import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Datos de los diferentes tipos de extintores
extintores_data = {
    'Tipo': ['Agua', 'Espuma', 'Polvo ABC', 'CO2', 'Agente Limpio'],
    'Clase_A': [5, 4, 5, 2, 3],  # Sólidos combustibles (madera, papel, tela)
    'Clase_B': [1, 5, 4, 5, 4],  # Líquidos inflamables
    'Clase_C': [1, 2, 5, 5, 5],  # Gases inflamables
    'Clase_D': [1, 1, 2, 1, 1],  # Metales combustibles
    'Clase_K': [2, 3, 1, 2, 3],  # Aceites vegetales/animales
    'Electrico': [1, 1, 3, 5, 5], # Equipos eléctricos
    'Costo': [2, 3, 3, 4, 5],    # 1=Bajo, 5=Alto
    'Toxicidad': [5, 4, 3, 4, 5], # 1=Alta toxicidad, 5=Baja toxicidad
    'Residuo': [5, 2, 1, 5, 4]   # 1=Mucho residuo, 5=Sin residuo
}

df = pd.DataFrame(extintores_data)

# Configurar el estilo
plt.style.use('default')
fig = plt.figure(figsize=(16, 12))

# 1. Gráfico de radar para efectividad por clase de fuego
ax1 = plt.subplot(2, 3, 1, projection='polar')

# Preparar datos para el gráfico de radar
categories = ['Clase A\n(Sólidos)', 'Clase B\n(Líquidos)', 'Clase C\n(Gases)', 
              'Eléctrico', 'Clase K\n(Aceites)']
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]  # Cerrar el círculo

colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']

for i, extintor in enumerate(df['Tipo']):
    values = [df.loc[i, 'Clase_A'], df.loc[i, 'Clase_B'], df.loc[i, 'Clase_C'], 
              df.loc[i, 'Electrico'], df.loc[i, 'Clase_K']]
    values += values[:1]
    ax1.plot(angles, values, 'o-', linewidth=2, label=extintor, color=colors[i], alpha=0.7)
    ax1.fill(angles, values, alpha=0.1, color=colors[i])

ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, fontsize=8)
ax1.set_ylim(0, 5)
ax1.set_title('Efectividad por Tipo de Fuego\n(1=Baja, 5=Alta)', fontsize=10, fontweight='bold')
ax1.legend(bbox_to_anchor=(1.1, 1.1), fontsize=8)
ax1.grid(True)

# 2. Gráfico de barras para comparación de características
ax2 = plt.subplot(2, 3, 2)
x = np.arange(len(df['Tipo']))
width = 0.25

bars1 = ax2.bar(x - width, df['Costo'], width, label='Costo', color='#FF6B6B', alpha=0.8)
bars2 = ax2.bar(x, df['Toxicidad'], width, label='Seguridad', color='#4ECDC4', alpha=0.8)
bars3 = ax2.bar(x + width, df['Residuo'], width, label='Limpieza', color='#45B7D1', alpha=0.8)

ax2.set_xlabel('Tipo de Extintor')
ax2.set_ylabel('Puntuación (1-5)')
ax2.set_title('Características Generales', fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(df['Tipo'], rotation=45, ha='right')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Añadir valores en las barras
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax2.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)

# 3. Mapa de calor para efectividad
ax3 = plt.subplot(2, 3, 3)
effectiveness_data = df[['Clase_A', 'Clase_B', 'Clase_C', 'Clase_D', 'Electrico']].values
im = ax3.imshow(effectiveness_data, cmap='RdYlGn', aspect='auto', vmin=1, vmax=5)

ax3.set_xticks(range(5))
ax3.set_xticklabels(['Clase A', 'Clase B', 'Clase C', 'Clase D', 'Eléctrico'], rotation=45)
ax3.set_yticks(range(len(df['Tipo'])))
ax3.set_yticklabels(df['Tipo'])
ax3.set_title('Mapa de Efectividad', fontweight='bold')

# Añadir valores en el mapa de calor
for i in range(len(df['Tipo'])):
    for j in range(5):
        ax3.text(j, i, effectiveness_data[i, j], ha="center", va="center", color="black", fontweight='bold')

# Barra de color
cbar = plt.colorbar(im, ax=ax3, shrink=0.6)
cbar.set_label('Efectividad (1-5)', rotation=270, labelpad=15)

# 4. Gráfico de dispersión: Costo vs Efectividad promedio
ax4 = plt.subplot(2, 3, 4)
efectividad_promedio = df[['Clase_A', 'Clase_B', 'Clase_C', 'Electrico']].mean(axis=1)

scatter = ax4.scatter(df['Costo'], efectividad_promedio, 
                     c=colors, s=200, alpha=0.7, edgecolors='black', linewidth=1)

for i, txt in enumerate(df['Tipo']):
    ax4.annotate(txt, (df['Costo'].iloc[i], efectividad_promedio.iloc[i]), 
                xytext=(5, 5), textcoords='offset points', fontsize=9)

ax4.set_xlabel('Costo (1=Bajo, 5=Alto)')
ax4.set_ylabel('Efectividad Promedio')
ax4.set_title('Costo vs Efectividad', fontweight='bold')
ax4.grid(True, alpha=0.3)

# 5. Gráfico de barras apiladas para aplicaciones
ax5 = plt.subplot(2, 3, 5)
aplicaciones = ['Hogar', 'Oficina', 'Industrial', 'Cocina', 'Laboratorio']
data_aplicaciones = {
    'Agua': [4, 3, 2, 1, 1],
    'Espuma': [3, 4, 5, 2, 2],
    'Polvo ABC': [5, 5, 4, 3, 3],
    'CO2': [2, 4, 3, 2, 5],
    'Agente Limpio': [3, 5, 4, 3, 5]
}

bottom = np.zeros(5)
for i, (extintor, valores) in enumerate(data_aplicaciones.items()):
    ax5.bar(aplicaciones, valores, bottom=bottom, label=extintor, color=colors[i], alpha=0.8)
    bottom += valores

ax5.set_ylabel('Idoneidad Acumulada')
ax5.set_title('Idoneidad por Aplicación', fontweight='bold')
ax5.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.setp(ax5.get_xticklabels(), rotation=45, ha='right')

# 6. Información textual
ax6 = plt.subplot(2, 3, 6)
ax6.axis('off')

info_text = """
GUÍA DE EXTINTORES

AGUA:
• Mejor para: Fuegos clase A (madera, papel)
• Evitar en: Equipos eléctricos, aceites
• Ventajas: Económico, no tóxico
• Desventajas: Limitado a clase A

ESPUMA:
• Mejor para: Líquidos inflamables (clase B)
• Ventajas: Efectivo en derrames grandes
• Desventajas: Deja residuo, corrosivo

POLVO ABC:
• Mejor para: Multiuso (A, B, C)
• Ventajas: Versátil, económico
• Desventajas: Residuo abrasivo, reduce visibilidad

CO2:
• Mejor para: Equipos eléctricos, precisión
• Ventajas: No deja residuo, no conductor
• Desventajas: Riesgo de asfixia en espacios cerrados

AGENTE LIMPIO:
• Mejor para: Equipos sensibles, laboratorios
• Ventajas: Sin residuo, no tóxico
• Desventajas: Más costoso
"""

ax6.text(0, 1, info_text, transform=ax6.transAxes, fontsize=9,
         verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", 
         facecolor='lightgray', alpha=0.5))

plt.tight_layout()
plt.suptitle('COMPARACIÓN DE TIPOS DE EXTINTORES', fontsize=16, fontweight='bold', y=0.98)
plt.show()

# Tabla resumen
print("\n" + "="*80)
print("TABLA RESUMEN - EFECTIVIDAD POR TIPO DE FUEGO")
print("="*80)
print(f"{'Extintor':<15} {'Clase A':<8} {'Clase B':<8} {'Clase C':<8} {'Eléctrico':<10} {'Costo':<6}")
print("-"*80)
for i, row in df.iterrows():
    efectividad_a = "★" * row['Clase_A'] + "☆" * (5 - row['Clase_A'])
    efectividad_b = "★" * row['Clase_B'] + "☆" * (5 - row['Clase_B'])
    efectividad_c = "★" * row['Clase_C'] + "☆" * (5 - row['Clase_C'])
    efectividad_e = "★" * row['Electrico'] + "☆" * (5 - row['Electrico'])
    costo = "$" * row['Costo']
    
    print(f"{row['Tipo']:<15} {efectividad_a:<8} {efectividad_b:<8} {efectividad_c:<8} {efectividad_e:<10} {costo:<6}")

print("\nLeyenda: ★ = Efectivo, ☆ = No efectivo, $ = Nivel de costo")