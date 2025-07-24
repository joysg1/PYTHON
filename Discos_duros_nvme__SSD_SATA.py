import plotly.graph_objects as go

# Datos de rendimiento (en MB/s)
discos = ['NVMe', 'SSD SATA']
lectura = [3500, 550]  # Velocidades de lectura
escritura = [3000, 500]  # Velocidades de escritura

# Crear el gráfico de barras apiladas
fig = go.Figure()

# Añadir las barras de lectura
fig.add_trace(go.Bar(
    x=discos,
    y=lectura,
    name='Lectura',
    marker_color='blue',
    text=lectura,  # Añadir los valores de lectura
    textposition='inside'  # Posición del texto
))

# Añadir las barras de escritura
fig.add_trace(go.Bar(
    x=discos,
    y=escritura,
    name='Escritura',
    marker_color='orange',
    text=escritura,  # Añadir los valores de escritura
    textposition='inside'  # Posición del texto
))

# Configuración del diseño
fig.update_layout(
    title='Comparación de Rendimiento: NVMe vs SSD SATA',
    xaxis_title='Tipo de Disco',
    yaxis_title='Velocidad (MB/s)',
    barmode='stack'
)

# Mostrar el gráfico
fig.show()




