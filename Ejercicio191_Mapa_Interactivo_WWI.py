import pandas as pd
import plotly.express as px

# Datos de los eventos (agrega una columna "País")
data = """Año,Descripción,Latitud,Longitud,País
1914,Comienza la guerra el 28 de junio con el asesinato del archiduque Francisco Fernando,46.0516,14.4378,Austria-Hungría
1915,Se intensifican las batallas en el Frente Occidental; se introduce la guerra de trincheras y se producen importantes enfrentamientos como la Batalla de Gallipoli,39.9167,32.8333,Turquía
1916,La Batalla de Verdún y la Batalla del Somme marcan un alto costo en vidas; se estima que más de un millón de soldados mueren en estos combates,49.4167,5.5833,Francia
1917,EE. UU. entra en la guerra en abril; la Revolución Rusa lleva a la retirada de Rusia del conflicto tras el Tratado de Brest-Litovsk en diciembre,55.75,37.6167,Rusia
1918,La guerra termina el 11 de noviembre con la firma del armisticio; se producen cambios significativos en el mapa de Europa y la caída de varios imperios,48.8567,2.3508,Francia"""

# Crear un DataFrame de Pandas
df = pd.DataFrame([row.split(',') for row in data.splitlines()[1:]],
                   columns=[col for col in data.splitlines()[0].split(',')])

# Crear el mapa interactivo con texto sobre los puntos
fig = px.scatter_geo(df, lat="Latitud", lon="Longitud", color="Año",
                    hover_name="Descripción",
                    text="País",
                    projection="orthographic")

# Personalizar el mapa
fig.update_layout(title='Eventos de la Primera Guerra Mundial por País')
fig.update_traces(marker_size=10)

# Mostrar el mapa
fig.show()