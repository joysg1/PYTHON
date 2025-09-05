import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

# Datos de pérdidas materiales de Japón después de la Segunda Guerra Mundial
# (Valores aproximados basados en registros históricos)

# Pérdidas por categoría (en miles de millones de yenes de 1945)
categorias = [
    'Infraestructura Industrial',
    'Viviendas y Edificios',
    'Transporte y Comunicaciones',
    'Agricultura y Pesca',
    'Equipamiento Militar',
    'Instituciones Públicas',
    'Comercio y Servicios'
]

perdidas_valor = [850, 1200, 650, 400, 750, 300, 500]  # En miles de millones de yenes 1945

# Pérdidas por región (ciudades más afectadas)
ciudades = ['Tokio', 'Osaka', 'Yokohama', 'Kobe', 'Nagoya', 'Hiroshima', 'Nagasaki']
perdidas_ciudades = [25, 18, 12, 10, 15, 8, 6]  # Porcentaje de destrucción

# Evolución temporal de la reconstrucción (1945-1955)
años = list(range(1945, 1956))
nivel_reconstruccion = [0, 5, 15, 25, 40, 55, 68, 78, 85, 92, 100]

# Crear subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'Pérdidas Materiales por Categoría',
        'Nivel de Destrucción por Ciudad (%)',
        'Evolución de la Reconstrucción (1945-1955)',
        'Distribución de Pérdidas'
    ),
    specs=[[{"type": "bar"}, {"type": "bar"}],
           [{"type": "scatter"}, {"type": "pie"}]]
)

# Gráfico 1: Pérdidas por categoría
fig.add_trace(
    go.Bar(
        x=categorias,
        y=perdidas_valor,
        name='Pérdidas (Miles de Millones ¥)',
        marker_color=['#8B0000', '#A0522D', '#2F4F4F', '#006400', '#4B0082', '#8B4513', '#B22222'],
        text=[f'{val:,}' for val in perdidas_valor],
        textposition='auto'
    ),
    row=1, col=1
)

# Gráfico 2: Destrucción por ciudad
fig.add_trace(
    go.Bar(
        x=ciudades,
        y=perdidas_ciudades,
        name='% Destrucción',
        marker_color='darkred',
        text=[f'{val}%' for val in perdidas_ciudades],
        textposition='auto'
    ),
    row=1, col=2
)

# Gráfico 3: Evolución de reconstrucción
fig.add_trace(
    go.Scatter(
        x=años,
        y=nivel_reconstruccion,
        mode='lines+markers',
        name='Nivel de Reconstrucción (%)',
        line=dict(color='darkgreen', width=3),
        marker=dict(size=8, color='darkgreen'),
        fill='tonexty'
    ),
    row=2, col=1
)

# Gráfico 4: Distribución de pérdidas (pie chart)
fig.add_trace(
    go.Pie(
        labels=categorias,
        values=perdidas_valor,
        name="Distribución",
        marker_colors=['#8B0000', '#A0522D', '#2F4F4F', '#006400', '#4B0082', '#8B4513', '#B22222']
    ),
    row=2, col=2
)

# Actualizar layout
fig.update_layout(
    height=800,
    title={
        'text': '<b>Pérdidas Materiales de Japón después de la Segunda Guerra Mundial</b><br><sub>Impacto y Reconstrucción (1945-1955)</sub>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20}
    },
    showlegend=False,
    plot_bgcolor='white',
    paper_bgcolor='#f8f9fa'
)

# Personalizar ejes y títulos
fig.update_xaxes(title_text="Categorías", row=1, col=1, tickangle=45)
fig.update_yaxes(title_text="Miles de Millones de Yenes (1945)", row=1, col=1)

fig.update_xaxes(title_text="Ciudades", row=1, col=2, tickangle=45)
fig.update_yaxes(title_text="Porcentaje de Destrucción", row=1, col=2)

fig.update_xaxes(title_text="Año", row=2, col=1)
fig.update_yaxes(title_text="Nivel de Reconstrucción (%)", row=2, col=1)

# Añadir anotaciones informativas
fig.add_annotation(
    text="Pérdida total estimada: ~4.65 billones de yenes",
    xref="paper", yref="paper",
    x=0.5, y=-0.15,
    showarrow=False,
    font=dict(size=14, color="darkred"),
    bgcolor="white",
    bordercolor="darkred",
    borderwidth=1
)

# Mostrar el gráfico
fig.show()

# Opcional: Guardar como HTML
# fig.write_html("perdidas_japon_wwii.html")

print("Gráfico generado exitosamente!")
print(f"Pérdida total estimada: {sum(perdidas_valor):,} miles de millones de yenes (1945)")
print("El gráfico muestra múltiples perspectivas de las pérdidas materiales y la reconstrucción de Japón.")