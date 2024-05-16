#pip install faker

from faker import Faker
import pandas as pd





def crear_datos(cantidad):
    datos = {}  
    datos_ficticios = Faker()

    for i in range(cantidad):
     nombre = datos_ficticios.name()
     direccion = datos_ficticios.address()
     datos[nombre]=direccion
 
    return datos   

def generar_df(diccionario):
    df =  pd.DataFrame([[clave, diccionario [clave]] for clave in diccionario.keys()], columns=['Nombre', 'Direccion'])
    return df

def crear_csv(df, fichero='datos'):
    nombre_fichero = fichero + '.csv'
    df.to_csv(nombre_fichero, encoding='utf-8', index=False)
    

if __name__=='__main__':
    
    datos = crear_datos(100) 
    df = generar_df((datos))
    print(df.head())
    crear_csv(df,"pruebas")
   
#Video 95 min 8.15 
    