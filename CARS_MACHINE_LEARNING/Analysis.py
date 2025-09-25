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
# Codigo para verificar el tipo de dato de cada columna
print(df_cars.dtypes)
# Codigo para encontrar la media de cada columna
print(df_cars.mean())
# Codigo para modificar los valores de la columna gender y aplicar donde sea 0 por masculino y donde sea 1 por femenino
df_cars['gender'] = df_cars['gender'].replace(0, 'Masculino')
df_cars['gender'] = df_cars['gender'].replace(1, 'Femenino')
print(df_cars.head())


