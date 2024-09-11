import plotly.express as px
import pandas as pd

# Crear un DataFrame con datos de ejemplo de la población por continente.
data = {
    'Continent': ['Asia', 'Africa', 'Europe', 'North America', 'South America', 'Oceania'],
    'Population': [4660000000, 1340000000, 748000000, 579000000, 430000000, 43000000]
}

df = pd.DataFrame(data)

# Crear el gráfico de barras usando Plotly Express
fig = px.bar(
    df,
    x='Continent',
    y='Population',
    color='Population',
    color_continuous_scale=px.colors.sequential.Plasma,
    title="Población Mundial por Continente",
    labels={'Population': 'Población'},
    template="plotly_dark"
)

# Mostrar el gráfico
fig.show()

