import plotly.graph_objects as go

# Datos de ejemplo: años y niveles de contaminación (en microgramos por litro)
años = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
# Incremento del 200% cada 5 años
contaminacion = [10, 35, 65, 95, 105, 150,170]  # Proyección de contaminación

# Crear el gráfico de área
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=años,
    y=contaminacion,
    fill='tozeroy',  # Rellenar hacia el eje y
    mode='lines+markers',
    name='Contaminación',
    line=dict(color='Slateblue', width=2),
    marker=dict(size=8, color='Slateblue')
))

# Añadir título y etiquetas
fig.update_layout(
    title='Proyección de Contaminación por Metales Pesados (2024-2030)',
    xaxis_title='Año',
    yaxis_title='Contaminación (µg/L)',
    xaxis=dict(tickmode='linear'),
    yaxis=dict(range=[0, 200]),  # Ajustar el rango del eje y según sea necesario
    template='plotly_white'
)

# Mostrar el gráfico
fig.show()

