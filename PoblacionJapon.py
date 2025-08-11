import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

# Datos históricos y proyecciones del envejecimiento poblacional de Japón
# Porcentaje de población mayor de 65 años
años = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2024, 2030, 2040, 2050, 2060]
porcentaje_65_mas = [4.9, 5.7, 7.1, 9.1, 12.1, 17.4, 23.0, 28.4, 29.8, 31.2, 35.3, 38.8, 40.5]

# Crear DataFrame
df = pd.DataFrame({
    'Año': años,
    'Porcentaje_65+': porcentaje_65_mas
})

# Crear la figura
fig = go.Figure()

# Añadir la curva con área sombreada
fig.add_trace(go.Scatter(
    x=df['Año'],
    y=df['Porcentaje_65+'],
    mode='lines+markers',
    name='% Población 65+ años',
    line=dict(color='#FF6B6B', width=3),
    marker=dict(size=8, color='#FF6B6B'),
    fill='tonexty',
    fillcolor='rgba(255, 107, 107, 0.3)',
    hovertemplate='<b>Año:</b> %{x}<br><b>Población 65+:</b> %{y}%<extra></extra>'
))

# Añadir línea base en y=0 para crear el área
fig.add_trace(go.Scatter(
    x=df['Año'],
    y=[0] * len(df),
    mode='lines',
    line=dict(color='rgba(0,0,0,0)'),
    showlegend=False,
    hoverinfo='skip'
))

# Añadir línea vertical para marcar el año actual
fig.add_vline(
    x=2024,
    line_dash="dash",
    line_color="gray",
    annotation_text="Actualidad",
    annotation_position="top"
)

# Personalizar el diseño
fig.update_layout(
    title={
        'text': 'Envejecimiento Poblacional de Japón<br><sub>Porcentaje de población mayor de 65 años</sub>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20}
    },
    xaxis_title='Año',
    yaxis_title='Porcentaje de la Población (%)',
    template='plotly_white',
    width=900,
    height=600,
    hovermode='x unified',
    font=dict(family="Arial, sans-serif", size=12),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Personalizar ejes
fig.update_xaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightgray',
    range=[1945, 2065]
)

fig.update_yaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightgray',
    range=[0, 45],
    ticksuffix='%'
)

# Añadir anotaciones para puntos clave
fig.add_annotation(
    x=2024,
    y=29.8,
    text="29.8% en 2024<br>(Casi 30% actual)",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#FF6B6B",
    ax=20,
    ay=-40,
    bgcolor="white",
    bordercolor="#FF6B6B",
    borderwidth=1,
    font=dict(size=11)
)

fig.add_annotation(
    x=2060,
    y=40.5,
    text="40.5% proyectado<br>para 2060",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#FF6B6B",
    ax=-30,
    ay=-30,
    bgcolor="white",
    bordercolor="#FF6B6B",
    borderwidth=1,
    font=dict(size=11)
)

# Mostrar la figura
fig.show()

# Información adicional
print("=" * 50)
print("DATOS CLAVE DEL ENVEJECIMIENTO EN JAPÓN")
print("=" * 50)
print(f"• Porcentaje actual (2024): {porcentaje_65_mas[-4]}%")
print(f"• Proyección 2060: {porcentaje_65_mas[-1]}%")
print(f"• Población 80+ años: Más del 10% (2024)")
print(f"• Japón es el país más 'viejo' del mundo")
print("=" * 50)