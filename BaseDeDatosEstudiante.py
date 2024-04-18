"""

Crea una tabla llamada Alumnos que constará de tres columnas: 
la columna id de tipo entero, la columna 
nombre que será de tipo texto y la columna 
notas de tipo entero. Usa funcion para insertar 
y mostrar datos. Una vez creada la tabla, 
tenéis que insertarle 3 datos mediante input dentro de un bucle.

"""

import sqlite3

def conectar():
    conexion = sqlite3.connect('alumnos.db')
    cursor = conexion.cursor()
    print('Conectado a la base de datos')
    return conexion, cursor

def cerrar_conexion(conexion):
    conexion.close()
    
def crear_tabla():
    conexion, cursor = conectar()
    cursor.execute('CREATE TABLE IF NOT EXISTS ALUMNO (IDENTIFICADOR INT PRIMARY KEY, NOMBRE VARCHAR(20), NOTAS INT)')
    cerrar_conexion(conexion) 
    print("Tabla creada")  
    
    
def insertar(alumno):
    conexion, cursor = conectar()
    cursor.execute('INSERT INTO ALUMNO VALUES (?,?,?)',alumno)
    conexion.commit()
    cerrar_conexion(conexion) 
    
    
def consultar(): 
    conexion, cursor = conectar()  
    cursor.execute('SELECT * FROM alumno')
    alumnos = cursor.fetchall()
    cerrar_conexion(conexion) 
    print("CONSULTA REALIZADA") 
    return alumnos      
    
if __name__=='__main__':    
 
 crear_tabla() 

 #Prueba de ingreso de datos

"""
 alumno1 = (1, "Carlos Garcia",5)
 insertar(alumno1)  
 
"""    
    
alumno2 = (2, "Raul Fernandez",10)
insertar(alumno2)     
    