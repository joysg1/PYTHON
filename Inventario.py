import plotly.graph_objects as go

# Datos simulados
tiempo = list(range(1, 13))  # Meses del año
costo_jit = [200, 180, 220, 210, 190, 230, 240, 200, 210, 220, 230, 240]
costo_reabastecimiento_periodico = [250, 240, 260, 250, 270, 280, 290, 300, 310, 320, 330, 340]
costo_reabastecimiento_continuo = [300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190]

# Crear la figura
fig = go.Figure()

# Agregar trazas para cada técnica
fig.add_trace(go.Scatter(x=tiempo, y=costo_jit, mode='lines+markers', name='Justo a Tiempo (JIT)', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=tiempo, y=costo_reabastecimiento_periodico, mode='lines+markers', name='Reabastecimiento Periódico', line=dict(color='orange')))
fig.add_trace(go.Scatter(x=tiempo, y=costo_reabastecimiento_continuo, mode='lines+markers', name='Reabastecimiento Continuo', line=dict(color='green')))

# Configurar el diseño
fig.update_layout(title='Comparación de Técnicas de Administración de Inventario',
                  xaxis_title='Meses',
                  yaxis_title='Costo (en unidades monetarias)',
                  legend_title='Técnicas',
                  template='plotly_white')

# Mostrar la figura
fig.show()
