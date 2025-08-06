import plotly.graph_objects as go

# Nombres de los cuerpos celestes
nombres = ['Sol', 'Júpiter', 'Saturno', 'Urano', 'Neptuno', 'Tierra', 'Marte']

# Áreas cuadradas aproximadas en millones de km²
areas = [6.087e12, 6.142e10, 4.272e10, 8.083e9, 7.618e9, 5.101e7, 1.443e7]

# Crear el gráfico de barras
fig = go.Figure()

fig.add_trace(go.Bar(
    x=nombres,
    y=areas,
    marker=dict(color='blue')
))

# Configurar el diseño del gráfico
fig.update_layout(
    title='Áreas Cuadradas de los Cuerpos Celestes Más Grandes Conocidos',
    xaxis_title='Cuerpos Celestes',
    yaxis_title='Área (millones de km²)',
    yaxis=dict(type='log', tickvals=[1e7, 1e8, 1e9, 1e10, 1e11, 1e12], 
               ticktext=['10M', '100M', '1B', '10B', '100B', '6.1T']),
    showlegend=False
)

# Mostrar el gráfico
fig.show()



