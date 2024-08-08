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


print(df2.head()) # Primeros 5 registros
print(df2.tail()) # Ultimos 5 registros
print(df2.shape) # Total de registros y columnas
print(df2.dtypes) # Tipo de datos de cada columna
print(df2.describe()) # Proporciona estadisticas descriptivas de las columnas numericas
print(df2.count()) #Cuenta el numero de valores no nulos en cada columna
print(df2.info()) # Informacion general sobre el dataframe
a = df2['Nombre'].unique() # Valores unicos de una columna
print(a)
df2.dropna() # Elimina filas con valores nulos
df2.drop_duplicates(inplace=True) # Elimina filas duplicadas
df2.fillna(value=0) # Rellena los valores nulos con 0
df2['Edad'] = df2['Edad'].astype('int') # Cambia el tipo de dato de una columna
# df2.rename(columns={'columna1': 'nuevo_nombre'}, inplace=True) # Cambia el nombre de una columna



# 5 Manipulacion de datos

# Seleccion y filtrado

print(df2['Nombre']) # Selecciona una columna
print(df2[df2['Edad'] > 30]) # Filtra por una condicion
print(df2[(df2['Edad'] > 30) & (df2['Ciudad'] == 'Madrid')]) # Filtra por multiples condiciones
print(df2.groupby('Ciudad').agg({'Edad': 'sum'})) # Agrupa por una columna y aplica una funcion





 # https://codigofacilito.com/videos/clase-completa-pyhton-para-ciencias-de-datos-pandas




