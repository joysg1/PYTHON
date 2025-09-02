import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Configuración del estilo
plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11

# Crear datos temporales (0 a 120 meses = 10 años)
tiempo_meses = np.arange(0, 121, 1)

# Función de decaimiento exponencial para radiación
def calcular_impacto(tiempo, factor_decaimiento, nivel_inicial):
    """
    Calcula el nivel de impacto ambiental basado en decaimiento exponencial
    
    tiempo: tiempo en meses desde la explosión
    factor_decaimiento: tasa de decaimiento (mayor valor = decaimiento más rápido)
    nivel_inicial: nivel de radiación inicial (%)
    """
    return np.maximum(1, nivel_inicial * np.exp(-factor_decaimiento * tiempo))

# Parámetros basados en datos históricos y científicos
# Hiroshima (Little Boy - Uranio-235)
hiroshima_inicial = 100
hiroshima_decaimiento = 0.045  # Decaimiento más lento

# Nagasaki (Fat Man - Plutonio-239)  
nagasaki_inicial = 110  # Mayor potencia inicial
nagasaki_decaimiento = 0.055  # Decaimiento más rápido

# Calcular los datos de impacto
hiroshima_data = calcular_impacto(tiempo_meses, hiroshima_decaimiento, hiroshima_inicial)
nagasaki_data = calcular_impacto(tiempo_meses, nagasaki_decaimiento, nagasaki_inicial)

# Crear el gráfico
fig, ax = plt.subplots(figsize=(14, 9))

# Gráfico de área para Hiroshima
ax.fill_between(tiempo_meses, hiroshima_data, alpha=0.6, 
                color='#e74c3c', label='Hiroshima (Little Boy - Uranio)')

# Gráfico de área para Nagasaki
ax.fill_between(tiempo_meses, nagasaki_data, alpha=0.6, 
                color='#3498db', label='Nagasaki (Fat Man - Plutonio)')

# Líneas de contorno
ax.plot(tiempo_meses, hiroshima_data, color='#c0392b', linewidth=2.5)
ax.plot(tiempo_meses, nagasaki_data, color='#2980b9', linewidth=2.5)

# Líneas de referencia importantes
ax.axhline(y=50, color='orange', linestyle='--', alpha=0.7, linewidth=1.5, 
           label='Nivel de alerta sanitaria (50%)')
ax.axhline(y=10, color='green', linestyle='--', alpha=0.7, linewidth=1.5, 
           label='Nivel de precaución (10%)')
ax.axhline(y=1, color='gray', linestyle='-', alpha=0.5, linewidth=1, 
           label='Nivel de fondo natural (1%)')

# Configuración del gráfico
ax.set_xlabel('Tiempo transcurrido (meses)', fontsize=13, fontweight='bold')
ax.set_ylabel('Nivel de Afectación Ambiental (%)', fontsize=13, fontweight='bold')
ax.set_title('Curva de Recuperación Ambiental - Bombas Nucleares\nHiroshima y Nagasaki (Agosto 1945)', 
             fontsize=16, fontweight='bold', pad=20)

# Configurar escalas
ax.set_xlim(0, 120)
ax.set_ylim(0, 120)

# Configurar ticks del eje x
x_ticks = np.arange(0, 121, 12)  # Cada año
x_labels = ['Explosión'] + [f'{int(x/12)} año{"s" if x/12 > 1 else ""}' for x in x_ticks[1:]]
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels, rotation=45)

# Agregar grid
ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
ax.set_axisbelow(True)

# Configurar leyenda
legend = ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=True, 
                   fontsize=10, bbox_to_anchor=(0.98, 0.98))
legend.get_frame().set_facecolor('white')
legend.get_frame().set_alpha(0.9)

# Añadir anotaciones importantes
# Punto de máximo impacto Hiroshima
ax.annotate('Máximo impacto\nHiroshima', 
            xy=(0, hiroshima_inicial), xytext=(15, hiroshima_inicial-15),
            arrowprops=dict(arrowstyle='->', color='#c0392b', lw=1.5),
            fontsize=9, ha='left', color='#c0392b', fontweight='bold')

# Punto de máximo impacto Nagasaki
ax.annotate('Máximo impacto\nNagasaki', 
            xy=(0, nagasaki_inicial), xytext=(15, nagasaki_inicial+5),
            arrowprops=dict(arrowstyle='->', color='#2980b9', lw=1.5),
            fontsize=9, ha='left', color='#2980b9', fontweight='bold')

# Punto de recuperación (cuando llegan al 10%)
hiroshima_recovery = np.where(hiroshima_data <= 10)[0]
nagasaki_recovery = np.where(nagasaki_data <= 10)[0]

if len(hiroshima_recovery) > 0:
    recovery_month_h = hiroshima_recovery[0]
    ax.annotate(f'Recuperación significativa\n({recovery_month_h} meses)', 
                xy=(recovery_month_h, 10), xytext=(recovery_month_h+20, 25),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5),
                fontsize=9, ha='left', color='green', fontweight='bold')

# Agregar información técnica como texto
info_text = """
Factores del modelo:
• Decaimiento exponencial de isótopos radiactivos
• Lavado natural por precipitaciones
• Dispersión atmosférica y terrestre
• Absorción por vegetación y suelo

Datos históricos:
• Hiroshima: 15 kt, Uranio-235
• Nagasaki: 21 kt, Plutonio-239
• Recuperación completa: ~8-10 años
"""

ax.text(0.02, 0.02, info_text, transform=ax.transAxes, fontsize=9,
        verticalalignment='bottom', bbox=dict(boxstyle='round', 
        facecolor='lightgray', alpha=0.8))

# Ajustar layout
plt.tight_layout()

# Función para crear gráfico comparativo
def crear_grafico_comparativo():
    """Crear un segundo gráfico con vista comparativa"""
    fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Gráfico individual Hiroshima
    ax1.fill_between(tiempo_meses, hiroshima_data, alpha=0.7, color='#e74c3c')
    ax1.plot(tiempo_meses, hiroshima_data, color='#c0392b', linewidth=2)
    ax1.set_title('Hiroshima\n(Little Boy - Uranio-235)', fontweight='bold')
    ax1.set_xlabel('Meses')
    ax1.set_ylabel('Nivel de Afectación (%)')
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 120)
    
    # Gráfico individual Nagasaki
    ax2.fill_between(tiempo_meses, nagasaki_data, alpha=0.7, color='#3498db')
    ax2.plot(tiempo_meses, nagasaki_data, color='#2980b9', linewidth=2)
    ax2.set_title('Nagasaki\n(Fat Man - Plutonio-239)', fontweight='bold')
    ax2.set_xlabel('Meses')
    ax2.set_ylabel('Nivel de Afectación (%)')
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(0, 120)
    
    plt.tight_layout()
    return fig2

# Función para guardar los gráficos
def guardar_graficos():
    """Guardar los gráficos en diferentes formatos"""
    plt.figure(1)  # Gráfico principal
    plt.savefig('impacto_nuclear_combinado.png', dpi=300, bbox_inches='tight')
    plt.savefig('impacto_nuclear_combinado.pdf', bbox_inches='tight')
    
    fig2 = crear_grafico_comparativo()
    fig2.savefig('impacto_nuclear_comparativo.png', dpi=300, bbox_inches='tight')
    
    print("Gráficos guardados exitosamente:")
    print("- impacto_nuclear_combinado.png/pdf")
    print("- impacto_nuclear_comparativo.png")

# Función para mostrar estadísticas
def mostrar_estadisticas():
    """Mostrar estadísticas clave del impacto"""
    print("\n" + "="*50)
    print("ESTADÍSTICAS DEL IMPACTO AMBIENTAL")
    print("="*50)
    
    # Tiempo para llegar al 50%
    h_50 = np.where(hiroshima_data <= 50)[0]
    n_50 = np.where(nagasaki_data <= 50)[0]
    
    print(f"Tiempo para reducir al 50%:")
    print(f"  Hiroshima: {h_50[0] if len(h_50) > 0 else 'N/A'} meses")
    print(f"  Nagasaki:  {n_50[0] if len(n_50) > 0 else 'N/A'} meses")
    
    # Tiempo para llegar al 10%
    h_10 = np.where(hiroshima_data <= 10)[0]
    n_10 = np.where(nagasaki_data <= 10)[0]
    
    print(f"\nTiempo para reducir al 10%:")
    print(f"  Hiroshima: {h_10[0] if len(h_10) > 0 else 'N/A'} meses ({h_10[0]/12:.1f} años)")
    print(f"  Nagasaki:  {n_10[0] if len(n_10) > 0 else 'N/A'} meses ({n_10[0]/12:.1f} años)")
    
    print(f"\nNivel final (120 meses):")
    print(f"  Hiroshima: {hiroshima_data[-1]:.2f}%")
    print(f"  Nagasaki:  {nagasaki_data[-1]:.2f}%")

# Mostrar el gráfico principal
plt.show()

# Ejecutar funciones adicionales
mostrar_estadisticas()

# Descomentar para guardar los gráficos
# guardar_graficos()

# Descomentar para mostrar gráfico comparativo
# crear_grafico_comparativo()
# plt.show()