import os
import pandas as pd

#directroio actual 

directorio_actual = os.getcwd()

print(directorio_actual)

#directorio datos

directorio_datos = os.path.join(directorio_actual,'datos')
print(directorio_datos)

#comprobar si un directorio existe
print(f"Existe el directorio {directorio_datos}")
print(os.path.exists(directorio_datos))
print("*"*80)
#comprobar si se trata de un directorio
print(f"Es {directorio_datos} un directorio")
print(os.path.isdir(directorio_datos))
print("*"*80)


#comprobar la capacidad de no encontrar un directorio que no existe

directorio_datos = os.path.join(directorio_actual,'daos')
print(directorio_datos)

#comprobar si un directorio existe
print(f"Existe el directorio {directorio_datos}")
print(os.path.exists(directorio_datos))
print("*"*80)
#comprobar si se trata de un directorio
print(f"Es {directorio_datos} un directorio")
print(os.path.isdir(directorio_datos))
print("*"*80)


#listar archivos del directorio
directorio_datos = os.path.join(directorio_actual,'datos')

listado = [os.path.join(directorio_datos, item) for item in os.listdir(directorio_datos)]
print(listado)
print(os.listdir(directorio_datos))

#crear carpeta nueva
try:
 carpeta_nueva = os.mkdir(os.path.join(directorio_actual, 'datos2'))
 print(carpeta_nueva)
except FileExistsError:
 print("Disculpe la carpeta ya existe") 

 #Abrir fichero fuera de la carpeta datos

fichero_exterior = os.path.join(directorio_actual,"a.csv")
df_exterior = pd.read_csv(fichero_exterior)
print("Mostramos fichero exterior")
print(df_exterior)

print("*"*80)


#Abrir fichero dentro de la carpeta datos

fichero_interior = os.path.join(directorio_datos,"a.csv")
df_interior = pd.read_csv(fichero_interior)
print("Mostramos fichero interior")
print(df_interior)

print("*"*80)

#Abrimos sin indicar ruta

ficheroD = "a.csv"
df = pd.read_csv(ficheroD)
print("Fichero sin indicar ruta")
print(df)


