import plotly.graph_objects as go
import numpy as np

# Datos para el gráfico
dias = np.arange(1, 11)  # 10 días
azucar_en_sangre = np.array([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])  # niveles de azúcar en sangre (mg/dL)
energia = np.array([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])  # niveles de energía (porcentaje)
hambre = np.array([20, 30, 40, 50, 60, 70, 80, 90, 100, 110])  # niveles de hambre (porcentaje)

# Crear el gráfico
fig = go.Figure(data=[
    go.Bar(x=dias, y=azucar_en_sangre, name='Azúcar en sangre'),
    go.Bar(x=dias, y=energia, name='Energía'),
    go.Bar(x=dias, y=hambre, name='Hambre')
])

# Configurar el gráfico
fig.update_layout(
    title='Efecto de la privación de azúcar en el cuerpo humano',
    xaxis_title='Días',
    yaxis_title='Niveles',
    barmode='group',
    legend=dict(yanchor='top', y=0.99, xanchor='left', x=0.01)
)

# Mostrar el gráfico
fig.show()
