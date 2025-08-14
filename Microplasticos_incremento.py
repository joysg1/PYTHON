import plotly.graph_objects as go
import numpy as np

# Años desde 1914 hasta 2025
years = np.arange(1914, 2026)
t = years - 1914  # años desde 1914

# Parámetros de crecimiento
P0 = 0.0001  # proporción inicial (fracción)
growth_rate = 0.10  # 10% anual

# Calcular proporción
proportion = P0 * (1 + growth_rate) ** t

# Convertir a partes por millón (ppm)
ppm = proportion * 1_000_000

# Crear gráfico solo con el área bajo la curva (color rojo)
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=np.concatenate([years, years[::-1]]),
    y=np.concatenate([ppm, np.zeros_like(ppm)]),
    fill='toself',
    fillcolor='rgba(255, 0, 0, 0.4)',  # rojo con transparencia
    line=dict(color='rgba(255,255,255,0)'),  # línea invisible
    hoverinfo="skip",
    showlegend=False,
    name='Área bajo la curva'
))

# Configurar el gráfico
fig.update_layout(
    title='Área bajo la Curva de Microplásticos (ppm) — 10% Anual',
    xaxis_title='Año',
    yaxis_title='Microplásticos (ppm)',
    template='plotly_white'
)

# Mostrar gráfico
fig.show()

