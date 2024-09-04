import pandas as pd
import plotly.express as px
from io import StringIO

# Datos de los eventos con solo las columnas Año, Descripción, Latitud, Longitud, País
data = """Año,Descripción,Latitud,Longitud,País
1914,El archiduque Francisco Fernando es asesinado en Sarajevo,43.8567,18.4131,Austria-Hungría
1914,Austria-Hungría emite un ultimátum a Serbia,48.2082,16.3738,Austria-Hungría
1914,Austria-Hungría declara la guerra a Serbia,44.7894,20.4781,Serbia
1914,Rusia comienza a movilizar sus tropas en San Petersburgo,59.9343,30.3351,Rusia
1914,Alemania declara la guerra a Rusia y a Francia,52.52,13.405,Alemania
1914,Alemania declara la guerra a Francia desde Berlín,48.8566,2.3522,Francia
1914,Alemania invade Bélgica lo que lleva al Reino Unido a entrar en la guerra,50.6333,5.5667,Bélgica
1914,El Reino Unido declara la guerra a Alemania desde Londres,51.5074,0.1278,Reino Unido
1914,La Primera Batalla del Marne se convierte en un punto crucial,49,3.5,Francia
1915,La guerra de trincheras se establece en el Frente Occidental,50,3,Francia
1915,La Batalla de Gallipoli comienza en Turquía,40.2861,26.1028,Imperio Otomano
1915,Italia se une a la Triple Entente,41.9028,12.4964,Italia
1915,Alemania utiliza gas cloro en la Segunda Batalla de Ypres,50.9667,2.8833,Alemania
1916,Comienza la Batalla de Verdún,49.1167,5.35,Francia
1916,La Batalla del Somme se inicia,50.2,2.5,Francia
1916,La guerra de trincheras se consolida en el Frente Occidental,50,3,Francia
1917,Estados Unidos declara la guerra a Alemania desde Washington D.C.,38.8951,-77.0364,Estados Unidos
1917,La Revolución Rusa estalla en Petrogrado,59.9343,30.3351,Rusia
1918,Alemania lanza una serie de ofensivas en el Frente Occidental,50,3,Alemania
1918,Las fuerzas aliadas lanzan contraofensivas en Amiens,49.8917,2.3378,Francia
1918,Las fuerzas aliadas continúan su avance en el Frente Occidental,50,3,Alemania
1918,Alemania pide un armisticio en Compiègne,49.4403,2.8317,Francia"""

# Leer los datos usando StringIO para manejar correctamente las comillas y comas
data_io = StringIO(data)

# Leer el CSV asegurando que el delimitador es la coma y las comillas están correctamente manejadas
df = pd.read_csv(data_io, quotechar='"', delimiter=',')

# Convertir las columnas de latitud y longitud a tipo numérico
df['Latitud'] = pd.to_numeric(df['Latitud'], errors='coerce')
df['Longitud'] = pd.to_numeric(df['Longitud'], errors='coerce')

# Crear el mapa interactivo con texto sobre los puntos
fig = px.scatter_geo(df, lat="Latitud", lon="Longitud", color="Año",
                    hover_name="Descripción",
                    text="País",
                    projection="orthographic")

# Personalizar el mapa
fig.update_layout(title='Eventos de la Primera Guerra Mundial por País')

# Actualizar formato del eje de colores para mostrar años como enteros
fig.update_layout(coloraxis_colorbar=dict(
    tickmode='array',
    tickvals=df['Año'].unique(),
    ticktext=[str(year) for year in sorted(df['Año'].unique())]
))

# Personalizar el tamaño de los marcadores
fig.update_traces(marker_size=10)

# Mostrar el mapa
fig.show()







