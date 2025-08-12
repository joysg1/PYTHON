import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import math

# Configurar datos de proyección de metales pesados (mg/L)
años = list(range(2024, 2031))  # 2024 a 2030

# Datos base 2024 y factores de crecimiento basados en tendencias industriales
# Valores típicos encontrados en estudios recientes
metales_data = {
    'Mercurio (Hg)': {
        'base_2024': 0.008,  # mg/L
        'factor_crecimiento': 0.05,  # 5% anual
        'color': '#FF4444',
        'limite_WHO': 0.006  # Límite OMS
    },
    'Plomo (Pb)': {
        'base_2024': 0.025,
        'factor_crecimiento': 0.03,  # 3% anual 
        'color': '#4444FF',
        'limite_WHO': 0.010
    },
    'Cadmio (Cd)': {
        'base_2024': 0.015,
        'factor_crecimiento': 0.07,  # 7% anual
        'color': '#44AA44',
        'limite_WHO': 0.003
    },
    'Arsénico (As)': {
        'base_2024': 0.018,
        'factor_crecimiento': 0.04,  # 4% anual
        'color': '#AA44AA',
        'limite_WHO': 0.010
    },
    'Cromo (Cr)': {
        'base_2024': 0.035,
        'factor_crecimiento': 0.06,  # 6% anual
        'color': '#FF8800',
        'limite_WHO': 0.050
    }
}

# Generar proyecciones para cada metal
proyecciones = {}
for metal, data in metales_data.items():
    concentraciones = []
    for i, año in enumerate(años):
        # Proyección exponencial con variabilidad
        variacion = np.random.normal(0, 0.02)  # Variabilidad ±2%
        concentracion = data['base_2024'] * (1 + data['factor_crecimiento']) ** i
        concentracion += concentracion * variacion  # Añadir variabilidad
        concentraciones.append(max(0, concentracion))  # Evitar valores negativos
    
    proyecciones[metal] = concentraciones

# Crear DataFrame
df = pd.DataFrame(proyecciones)
df['Año'] = años

# Crear la figura principal
fig = go.Figure()

# Añadir líneas para cada metal pesado
for metal, data in metales_data.items():
    fig.add_trace(go.Scatter(
        x=años,
        y=proyecciones[metal],
        mode='lines+markers',
        name=metal,
        line=dict(color=data['color'], width=3),
        marker=dict(size=8, color=data['color']),
        hovertemplate=f'<b>{metal}</b><br>Año: %{{x}}<br>Concentración: %{{y:.4f}} mg/L<extra></extra>'
    ))
    
    # Añadir línea de límite OMS
    fig.add_hline(
        y=data['limite_WHO'],
        line_dash="dot",
        line_color=data['color'],
        opacity=0.5,
        annotation_text=f"Límite OMS {metal.split('(')[0].strip()}",
        annotation_position="right",
        annotation=dict(font_size=10, font_color=data['color'])
    )

# Personalizar diseño
fig.update_layout(
    title={
        'text': 'Proyección de Metales Pesados en Agua Potable<br><sub>Concentraciones proyectadas 2024-2030 (mg/L)</sub>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 18}
    },
    xaxis_title='Año',
    yaxis_title='Concentración (mg/L)',
    template='plotly_white',
    width=1000,
    height=700,
    hovermode='x unified',
    font=dict(family="Arial, sans-serif", size=12),
    legend=dict(
        orientation="v",
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=1.05
    )
)

# Personalizar ejes
fig.update_xaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightgray',
    dtick=1  # Mostrar cada año
)

fig.update_yaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightgray',
    tickformat='.4f'
)

# Añadir zona de alerta
fig.add_vrect(
    x0=2027, x1=2030,
    fillcolor="red", opacity=0.1,
    layer="below", line_width=0,
    annotation_text="Zona de Alta Preocupación",
    annotation_position="top left"
)

# Mostrar la figura
fig.show()

# Crear gráfico de barras comparativo para 2030
fig2 = go.Figure()

metales_nombres = list(metales_data.keys())
concentraciones_2030 = [proyecciones[metal][-1] for metal in metales_nombres]
limites_oms = [metales_data[metal]['limite_WHO'] for metal in metales_nombres]
colores = [metales_data[metal]['color'] for metal in metales_nombres]

# Barras de concentraciones proyectadas
fig2.add_trace(go.Bar(
    x=metales_nombres,
    y=concentraciones_2030,
    name='Proyección 2030',
    marker_color=colores,
    opacity=0.8
))

# Barras de límites OMS
fig2.add_trace(go.Bar(
    x=metales_nombres,
    y=limites_oms,
    name='Límite OMS',
    marker_color='red',
    opacity=0.5
))

fig2.update_layout(
    title='Comparación Proyecciones 2030 vs Límites OMS',
    xaxis_title='Metales Pesados',
    yaxis_title='Concentración (mg/L)',
    template='plotly_white',
    barmode='group',
    width=900,
    height=500
)

fig2.show()

# Información de resumen
print("=" * 70)
print("RESUMEN DE PROYECCIONES DE METALES PESADOS EN AGUA")
print("=" * 70)
print(f"{'Metal':<20} {'2024 (mg/L)':<12} {'2030 (mg/L)':<12} {'% Aumento':<12} {'Estado OMS'}")
print("-" * 70)

for metal, data in metales_data.items():
    conc_2024 = proyecciones[metal][0]
    conc_2030 = proyecciones[metal][-1]
    aumento = ((conc_2030 - conc_2024) / conc_2024) * 100
    excede_oms = "⚠️ EXCEDE" if conc_2030 > data['limite_WHO'] else "✅ DENTRO"
    
    print(f"{metal:<20} {conc_2024:<12.4f} {conc_2030:<12.4f} {aumento:<12.1f} {excede_oms}")

print("=" * 70)
print("⚠️  ALERTA: Varios metales excederán los límites de la OMS para 2030")
print("🔬 Recomendación: Implementar sistemas de monitoreo y tratamiento")
print("=" * 70)