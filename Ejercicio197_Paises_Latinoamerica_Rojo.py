import plotly.express as px
import pandas as pd

# Lista de países latinoamericanos
latin_american_countries = [
    'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominican Republic',
    'Ecuador', 'El Salvador', 'Guatemala', 'Honduras', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay',
    'Peru', 'Uruguay', 'Venezuela'
]

# Cargar el conjunto de datos incorporado en plotly
df = px.data.gapminder().query("year == 2007")

# Crear una columna de color basada en la lista de países latinoamericanos
df['color'] = df['country'].apply(lambda x: 'red' if x in latin_american_countries else 'grey')

# Crear el mapa con Plotly Express usando el conjunto de datos gapminder
fig = px.choropleth(
    df,
    locations='country',
    locationmode='country names',
    color='color',
    color_discrete_map={'red': 'red', 'grey': 'grey'},
    projection='natural earth',
    title="Países de América Latina en Rojo"
)

# Mostrar el mapa
fig.show()






