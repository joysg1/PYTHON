import plotly.graph_objects as go
import pandas as pd

# Define un dataframe con las capitales de Europa
capitales = {
    'País': ['Albania', 'Austria', 'Bélgica', 'Bulgaria', 'Croacia', 'Chipre', 'República Checa', 'Dinamarca', 'Estonia', 'Finlandia', 'Francia', 'Alemania', 'Grecia', 'Hungría', 'Islandia', 'Irlanda', 'Italia', 'Letonia', 'Lituania', 'Luxemburgo', 'Macedonia', 'Malta', 'Moldavia', 'Mónaco', 'Montenegro', 'Países Bajos', 'Noruega', 'Polonia', 'Portugal', 'Rumania', 'Rusia', 'San Marino', 'Serbia', 'Eslovaquia', 'Eslovenia', 'España', 'Suecia', 'Suiza', 'Turquía', 'Ucrania', 'Reino Unido'],
    'Capital': ['Tirana', 'Viena', 'Bruselas', 'Sofía', 'Zagreb', 'Nicosia', 'Praga', 'Copenhague', 'Tallin', 'Helsinki', 'París', 'Berlín', 'Atenas', 'Budapest', 'Reikiavik', 'Dublín', 'Roma', 'Riga', 'Vilna', 'Luxemburgo', 'Skopje', 'La Valeta', 'Chisináu', 'Mónaco', 'Podgorica', 'Ámsterdam', 'Oslo', 'Varsovia', 'Lisboa', 'Bucarest', 'Moscú', 'San Marino', 'Belgrado', 'Bratislava', 'Liubliana', 'Madrid', 'Estocolmo', 'Berna', 'Ankara', 'Kiev', 'Londres'],
    'Latitud': [41.33, 48.21, 50.85, 42.70, 45.82, 35.17, 50.08, 55.67, 59.43, 60.17, 48.86, 52.52, 37.98, 47.50, 64.08, 53.35, 41.87, 56.95, 54.69, 49.61, 41.99, 35.90, 47.03, 43.73, 42.44, 52.37, 59.91, 52.23, 38.72, 44.43, 55.76, 43.93, 44.82, 48.15, 46.05, 40.42, 59.33, 46.95, 39.93, 50.08, 51.50],
    'Longitud': [19.82, 16.37, 4.35, 23.32, 15.98, 33.37, 14.42, 12.57, 24.73, 24.93, 2.35, 13.40, 23.73, 19.05, -21.94, -6.26, 12.49, 24.10, 25.28, 6.13, 21.43, 14.48, 28.85, 7.42, 19.27, 4.89, 10.75, 21.01, -9.14, 26.10, 37.62, 12.57, 20.45, 14.51, -3.70, 18.07, 7.45, 32.86, 30.52, 0.13]
}

df = pd.DataFrame(capitales)

# Crear un mapa de Europa
fig = go.Figure(go.Scattermapbox(
        lat=df['Latitud'],
        lon=df['Longitud'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9
        ),
        text=df['Capital'],
    ))

fig.update_layout(
    mapbox_style="open-street-map",
    mapbox_zoom=4,
    mapbox_center_lat=52.52,
    mapbox_center_lon=13.41,
    margin={"r":0,"t":0,"l":0,"b":0}
)

fig.show()



