import plotly.graph_objects as go

# Años desde 2020 hasta 2030
years = list(range(2020, 2031))

# Ventas simuladas (en millones de unidades)
ventas = {
    "Lenovo": [15, 17, 20, 23, 25, 27, 29, 30, 31, 32, 33],
    "HP":     [14, 15, 15, 16, 17, 17, 18, 18, 18, 17, 17],
    "Dell":   [12, 13, 14, 15, 15, 15, 14, 14, 14, 13, 13],
    "Apple":  [7,  8,  9,  9,  10, 11, 11, 12, 13, 13, 14],
    "Asus":   [6,  7,  7,  7,  8,  8,  8,  8,  8,  8,  8],
    "Otros":  [8,  8,  9,  8,  8,  7,  6,  6,  5,  5,  5],
}

# Crear la figura
fig = go.Figure()

# Agregar cada fabricante como una barra apilada vertical
for fabricante, datos in ventas.items():
    fig.add_trace(go.Bar(
        x=years,
        y=datos,
        name=fabricante
    ))

# Personalización del gráfico
fig.update_layout(
    title='Ventas de Laptops por Fabricante (2020–2030)',
    xaxis=dict(
        title='Año',
        tickmode='linear',
        tick0=2020,
        dtick=1
    ),
    yaxis=dict(
        title='Ventas (millones de unidades)'
    ),
    barmode='stack',  # Apiladas verticalmente
    legend_title='Fabricante',
    template='plotly_white',  # Fondo blanco, limpio
    height=600,
    width=1000
)

fig.show()

