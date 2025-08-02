import plotly.graph_objects as go

# Categorías del contenido
categorias = [
    'Violencia gráfica',
    'Abuso infantil',
    'Discurso de odio',
    'Contenido sexual explícito',
    'Suicidio/autolesiones',
    'Drogas',
    'Desinformación'
]

# Niveles de exposición estimados (0 a 10)
niveles_exposicion = [9, 8, 7, 8, 6, 5, 7]

# Repetimos el primer valor para cerrar el radar
categorias += [categorias[0]]
niveles_exposicion += [niveles_exposicion[0]]

# Crear figura de radar con color azul
fig = go.Figure(
    data=[
        go.Scatterpolar(
            r=niveles_exposicion,
            theta=categorias,
            fill='toself',
            name='Nivel de exposición',
            line_color='blue',
            fillcolor='rgba(0, 0, 255, 0.3)'  # Azul con transparencia
        )
    ]
)

# Configuración del diseño
fig.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 10])
    ),
    title='Tipo de contenido al que están expuestos los moderadores',
    showlegend=False
)

fig.show()

