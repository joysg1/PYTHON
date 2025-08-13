import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Datos de rendimiento basados en benchmarks actuales
# Tiempo en segundos para archivos de diferentes tamaños
tamaños_archivos_gb = np.array([0.1, 0.5, 1, 2, 5, 10, 20, 50, 100])

# Velocidades típicas (MB/s) basadas en datos de benchmarks 2024-2025
# SSD SATA: ~500-550 MB/s, NVMe: ~1500-7000 MB/s
# HDD 7200 RPM: ~80-160 MB/s
velocidad_ssd_sata = 520  # MB/s promedio
velocidad_ssd_nvme = 3500  # MB/s promedio NVMe
velocidad_hdd_7200 = 120  # MB/s promedio HDD 7200 RPM
velocidad_hdd_5400 = 80   # MB/s promedio HDD 5400 RPM

# Calcular tiempos de copiado (segundos)
tamaños_mb = tamaños_archivos_gb * 1024  # Convertir GB a MB

# Tiempos de copiado para cada tipo de disco
tiempo_ssd_sata = tamaños_mb / velocidad_ssd_sata
tiempo_ssd_nvme = tamaños_mb / velocidad_ssd_nvme
tiempo_hdd_7200 = tamaños_mb / velocidad_hdd_7200
tiempo_hdd_5400 = tamaños_mb / velocidad_hdd_5400

# Crear DataFrame
df = pd.DataFrame({
    'Tamaño_GB': tamaños_archivos_gb,
    'SSD_NVMe': tiempo_ssd_nvme,
    'SSD_SATA': tiempo_ssd_sata,
    'HDD_7200RPM': tiempo_hdd_7200,
    'HDD_5400RPM': tiempo_hdd_5400
})

# Crear la figura
fig = go.Figure()

# Configuración de colores y estilos
colores = {
    'SSD_NVMe': '#00FF7F',
    'SSD_SATA': '#1E90FF', 
    'HDD_7200RPM': '#FF6347',
    'HDD_5400RPM': '#DC143C'
}

# Añadir línea base en y=0 para las áreas
fig.add_trace(go.Scatter(
    x=tamaños_archivos_gb,
    y=[0] * len(tamaños_archivos_gb),
    mode='lines',
    line=dict(color='rgba(0,0,0,0)'),
    showlegend=False,
    hoverinfo='skip'
))

# Añadir curvas con área sombreada para cada tipo de disco
discos_data = {
    'SSD NVMe': {'tiempo': tiempo_ssd_nvme, 'color': colores['SSD_NVMe'], 'velocidad': velocidad_ssd_nvme},
    'SSD SATA': {'tiempo': tiempo_ssd_sata, 'color': colores['SSD_SATA'], 'velocidad': velocidad_ssd_sata},
    'HDD 7200 RPM': {'tiempo': tiempo_hdd_7200, 'color': colores['HDD_7200RPM'], 'velocidad': velocidad_hdd_7200},
    'HDD 5400 RPM': {'tiempo': tiempo_hdd_5400, 'color': colores['HDD_5400RPM'], 'velocidad': velocidad_hdd_5400}
}

for nombre, data in discos_data.items():
    fig.add_trace(go.Scatter(
        x=tamaños_archivos_gb,
        y=data['tiempo'],
        mode='lines+markers',
        name=f'{nombre} ({data["velocidad"]} MB/s)',
        line=dict(color=data['color'], width=3),
        marker=dict(size=8, color=data['color']),
        fill='tonexty',
        fillcolor=f'rgba{tuple(list(int(data["color"][1:][i:i+2], 16) for i in (0, 2, 4)) + [0.2])}',
        hovertemplate=f'<b>{nombre}</b><br>Tamaño: %{{x}} GB<br>Tiempo: %{{y:.1f}} segundos<br>Velocidad: {data["velocidad"]} MB/s<extra></extra>'
    ))

# Personalizar el diseño
fig.update_layout(
    title={
        'text': 'Rendimiento de Copiado: SSD vs HDD<br><sub>Tiempo de copiado vs Tamaño del archivo (Área bajo la curva = Tiempo total acumulado)</sub>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 18}
    },
    xaxis_title='Tamaño del Archivo (GB)',
    yaxis_title='Tiempo de Copiado (segundos)',
    template='plotly_white',
    width=1100,
    height=700,
    hovermode='x unified',
    font=dict(family="Arial, sans-serif", size=12),
    legend=dict(
        orientation="v",
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=1.02,
        bgcolor="rgba(255,255,255,0.8)",
        bordercolor="rgba(0,0,0,0.2)",
        borderwidth=1
    )
)

# Personalizar ejes
fig.update_xaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightgray',
    range=[0, 110]
)

fig.update_yaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightgray',
    range=[0, max(tiempo_hdd_5400) * 1.1]
)

# Añadir anotaciones comparativas
fig.add_annotation(
    x=50,
    y=tiempo_ssd_nvme[7],
    text=f"SSD NVMe: {tiempo_ssd_nvme[7]:.1f}s",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor=colores['SSD_NVMe'],
    ax=0,
    ay=-40,
    bgcolor="white",
    bordercolor=colores['SSD_NVMe'],
    borderwidth=1
)

fig.add_annotation(
    x=50,
    y=tiempo_hdd_5400[7],
    text=f"HDD 5400 RPM: {tiempo_hdd_5400[7]:.0f}s<br>({tiempo_hdd_5400[7]/tiempo_ssd_nvme[7]:.1f}x más lento)",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor=colores['HDD_5400RPM'],
    ax=0,
    ay=-40,
    bgcolor="white",
    bordercolor=colores['HDD_5400RPM'],
    borderwidth=1
)

# Mostrar la figura
fig.show()

# Crear gráfico de área acumulada para mostrar la diferencia total
fig2 = go.Figure()

# Calcular áreas bajo la curva (tiempo total acumulado)
area_ssd_nvme = np.trapz(tiempo_ssd_nvme, tamaños_archivos_gb)
area_ssd_sata = np.trapz(tiempo_ssd_sata, tamaños_archivos_gb)
area_hdd_7200 = np.trapz(tiempo_hdd_7200, tamaños_archivos_gb)
area_hdd_5400 = np.trapz(tiempo_hdd_5400, tamaños_archivos_gb)

# Gráfico de barras con áreas
tipos_disco = ['SSD NVMe', 'SSD SATA', 'HDD 7200 RPM', 'HDD 5400 RPM']
areas = [area_ssd_nvme, area_ssd_sata, area_hdd_7200, area_hdd_5400]
colores_barras = [colores['SSD_NVMe'], colores['SSD_SATA'], colores['HDD_7200RPM'], colores['HDD_5400RPM']]

fig2.add_trace(go.Bar(
    x=tipos_disco,
    y=areas,
    marker_color=colores_barras,
    text=[f'{area:.0f}s' for area in areas],
    textposition='outside',
    name='Área bajo la curva (Tiempo total acumulado)'
))

fig2.update_layout(
    title='Comparación de Áreas Bajo la Curva<br><sub>Tiempo total acumulado para copiar archivos de 0.1GB a 100GB</sub>',
    xaxis_title='Tipo de Disco',
    yaxis_title='Área Bajo la Curva (segundos × GB)',
    template='plotly_white',
    width=900,
    height=600,
    showlegend=False
)

fig2.show()

# Análisis de eficiencia
print("=" * 80)
print("ANÁLISIS DE RENDIMIENTO DE COPIADO - SSD vs HDD")
print("=" * 80)
print(f"{'Tipo de Disco':<20} {'Velocidad (MB/s)':<15} {'100GB (min)':<12} {'Área Total':<15} {'Eficiencia'}")
print("-" * 80)

for i, (tipo, area) in enumerate(zip(tipos_disco, areas)):
    velocidades = [velocidad_ssd_nvme, velocidad_ssd_sata, velocidad_hdd_7200, velocidad_hdd_5400]
    tiempo_100gb = tamaños_mb[-1] / velocidades[i] / 60  # en minutos
    eficiencia = "⚡ EXCELENTE" if velocidades[i] > 1000 else "✅ BUENA" if velocidades[i] > 300 else "⚠️ LENTA"
    
    print(f"{tipo:<20} {velocidades[i]:<15} {tiempo_100gb:<12.1f} {area:<15.0f} {eficiencia}")

print("=" * 80)
print("📊 CONCLUSIONES:")
print(f"• SSD NVMe es {velocidad_ssd_nvme/velocidad_hdd_5400:.1f}x más rápido que HDD 5400 RPM")
print(f"• SSD SATA es {velocidad_ssd_sata/velocidad_hdd_7200:.1f}x más rápido que HDD 7200 RPM")
print(f"• Para archivos grandes (>50GB), la diferencia es dramática")
print("• El área bajo la curva representa el 'costo temporal' total de las operaciones")
print("=" * 80)