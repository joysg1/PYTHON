import plotly.graph_objects as go

# Años de 1914 a 1918
years = ['1914', '1915', '1916', '1917', '1918']

# Datos ficticios de millones de habitantes afectados por la guerra
# Estos datos son solo un ejemplo y deben ser reemplazados por datos reales
central_powers = [2.0, 3.0, 4.0, 3.5, 2.5]  # Potencias Centrales
allies = [1.5, 2.5, 3.5, 4.0, 3.0]           # Aliados

# Crear el gráfico de barras apiladas
fig = go.Figure()

# Agregar trazas para Potencias Centrales
fig.add_trace(go.Bar(
    x=years,
    y=central_powers,
    name='Potencias Centrales',
    marker_color='rgba(255, 0, 0, 0.6)',  # Color para Potencias Centrales
    text=central_powers,  # Etiquetas de texto
    textposition='inside'  # Posición del texto dentro de la barra
))

# Agregar trazas para Aliados
fig.add_trace(go.Bar(
    x=years,
    y=allies,
    name='Aliados',
    marker_color='rgba(0, 0, 255, 0.6)',  # Color para Aliados
    text=allies,  # Etiquetas de texto
    textposition='inside'  # Posición del texto dentro de la barra
))

# Configurar el diseño del gráfico
fig.update_layout(
    title='Habitantes Afectados por la Guerra (1914-1918)',
    xaxis_title='Año',
    yaxis_title='Millones de Habitantes Afectados',
    barmode='stack',  # Apilar las barras
    template='plotly_white'
)

# Mostrar el gráfico
fig.show()


