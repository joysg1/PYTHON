import plotly.graph_objects as go
import pandas as pd

# Datos
meses = ['Julio 2025', 'Agosto 2025', 'Septiembre 2025', 'Octubre 2025', 'Noviembre 2025', 'Diciembre 2025']
gb_por_mes = 25  # GB de actualizaciones por mes
acumulado_gb = []
total_actual = 0

for _ in meses:
    total_actual += gb_por_mes
    acumulado_gb.append(total_actual)

# Crear DataFrame para Plotly
df = pd.DataFrame({
    'Mes': meses,
    'GB Acumulados': acumulado_gb
})

# Crear el gráfico de área
fig = go.Figure(go.Scatter(
    x=df['Mes'],
    y=df['GB Acumulados'],
    mode='lines',
    fill='tozeroy',  # Rellenar el área bajo la curva
    line_shape='spline', # Suavizar la línea
    name='GB Acumulados'
))

# Personalizar el diseño del gráfico
fig.update_layout(
    title='Total Acumulado de GB de Actualizaciones de Windows 11 (Julio - Diciembre 2025)',
    xaxis_title='Mes',
    yaxis_title='Gigabytes (GB) Acumulados',
    hovermode='x unified', # Muestra la información del hover en una sola caja para el eje X
    template='plotly_white' # Un tema limpio para el gráfico
)

# Mostrar el gráfico
fig.show()

print(f"El total acumulado de GB de actualizaciones desde Julio 2025 hasta Diciembre 2025 (a un ritmo de 25 GB/mes) es: {acumulado_gb[-1]} GB.")

