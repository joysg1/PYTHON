import plotly.graph_objects as go

# Carga los datos
datos = {
    "País": ["Alemania*", "Turquía*", "Rusia*", "Francia", "Austria-Hungría*", "Gran Bretaña e Irlanda*", "Italia", "Serbia", "Rumania*", "Bulgaria", "Colonias británicas", "Estados Unidos*", "Bélgica", "Colonias francesas", "Grecia", "Montenegro", "Portugal", "Japón"],
    "Bajas Militares": [2037000, 325000, 1811000, 1327000, 1460000, 750000, 460000, 275000, 250000, 88000, 180000, 117000, 38000, 78000, 25000, 13000, 7000, 1000],
    "Bajas Civiles": [700000, 2000000, 500000, 600000, 400000, 600000, 700000, 300000, 300000, 300000, 0, 0, 50000, 0, 0, 0, 0, 0]
}

# Crea el gráfico de barras
fig = go.Figure(data=[
    go.Bar(name="Bajas Militares", x=datos["País"], y=datos["Bajas Militares"], marker_color="green"),
    go.Bar(name="Bajas Civiles", x=datos["País"], y=datos["Bajas Civiles"], marker_color="pink")
])

# Configura el gráfico
fig.update_layout(
    title="Bajas en la Primera Guerra Mundial (1914-1918)",
    xaxis_title="País",
    yaxis_title="Número de bajas",
    barmode="group",
    yaxis=dict(type="log"),
    plot_bgcolor="#ADD8E6",  # Cambia el fondo a un celeste pastel
    paper_bgcolor="#ADD8E6",  # Cambia el fondo del papel a un celeste pastel
    font=dict(
        family="Arial",
        size=14,
        color="#333333"  # Cambia el color de la fuente a un gris oscuro
    ),
    title_font=dict(
        family="Arial",
        size=18,
        color="#333333"  # Cambia el color del título a un gris oscuro
    )
)

# Muestra el gráfico en un navegador web
fig.show()
