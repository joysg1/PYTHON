import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics


df_cars = pd.read_csv('/home/userlm/Documentos/CARS_MACHINE_LEARNING/cars.csv')
print(df_cars.head())
print(df_cars.describe())
print(df_cars.info())
print(df_cars.isnull().sum())

# Codigo para encontrar la media de cada columna
print(df_cars.mean())

# Codigo para modificar los valores de la columna gender y aplicar donde sea 0 por masculino y donde sea 1 por femenino
df_cars['gender'] = df_cars['gender'].replace(0, 'Masculino')
df_cars['gender'] = df_cars['gender'].replace(1, 'Femenino')
print(df_cars.head())
print(df_cars.dtypes)

# Codigo para cambiar el tipo de dato de sales a float
df_cars['sales'] = df_cars['sales'].astype(float)

# Codigo para cambiar el tipo de dato de income a float
df_cars['income'] = df_cars['income'].astype(float)

# Codigo para cambiar el tipo de dato de miles a float
df_cars['miles'] = df_cars['miles'].astype(float)

# Codigo para cambiar el tipo de dato de debt a float
df_cars['debt'] = df_cars['debt'].astype(float)

# Codigo para verificar el tipo de dato de cada columna
print(df_cars.dtypes)

# Codigo para ver el tamaño del dataframe
print(df_cars.shape)

# Codigo para ver la cantidad de filas del dataframe
print(len(df_cars))

# Codigo para ver la cantidad de columnas del dataframe
print(len(df_cars.columns))

# Codigo para ver las descripciones de cada columna
print(df_cars.describe())

# Codigo para cambiar los valores que sean 2 en gender por la cadena genero no especificado
df_cars['gender'] = df_cars['gender'].replace(2, 'Genero no especificado')

# Codigo para ver los valores unicos por columna
print(df_cars.nunique())

# Codigo para ver la cantidad de masculinos y femeninos
print(df_cars['gender'].value_counts())


# Codigo para crear un dataframe de solo los de genero femenino
df_cars_femenino = df_cars[df_cars['gender'] == 'Femenino']

print(df_cars_femenino.head())

# Codigo para imprimir la media de edad de los de genero femenino
print(df_cars_femenino['age'].mean())

# Código para una grafica del histograma de la edad del genero femenino
# plt.hist(df_cars_femenino['age'], bins=20)

# Codigo para una grafica usando seaborn para conocer la media del income del genero femenino
# sns.histplot(df_cars_femenino['income'], kde=True)

# Codigo para generar un grafico boxplot de las ventas del genero femenino
# plt.boxplot(df_cars_femenino['sales'])
# plt.show()





















