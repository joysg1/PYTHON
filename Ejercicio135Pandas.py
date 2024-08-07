import pandas as pd
print("Version de pandas: ",pd.__version__)

import numpy as np


#Estructura de datos en pandas 

# 1. Series: elementos del mismo tipo de una dimension, cada elemento tiene una etiqueta

s = pd.Series([1, 2, 3, 4, 5])
print(s)

# 2. Dataframe: estructura de datos bidimensional, cada columna es una serie. 
# Puede contener diferentes tipos de datos, cada columna tiene una etiqueta

df = pd.DataFrame({
    'Nombre': ['Juan', 'María', 'Pedro', 'Sofía'],
    'Edad': [25, 30, 35, 40],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
})

# 3. Carga y guardado de datos

# Cargar datos desde un archivo CSV
df2 = pd.read_csv('DataPersonasPandas.csv')
print(df2)

#4 Inspeccion y limpieza de datos

# -1:21:56  url: https://codigofacilito.com/videos/clase-completa-pyhton-para-ciencias-de-datos-pandas




