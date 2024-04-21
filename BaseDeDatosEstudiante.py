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

def actualizar(identificador, nombre, notas):
    conexion, cursor = conectar() 
    
    cursor.execute(f" UPDATE ALUMNO SET nombre = '{nombre}' , NOTAS = {notas} WHERE IDENTIFICADOR = {identificador}")
    print("Alumno actualizado")
    conexion.commit()
    cerrar_conexion(conexion)   
    
    
def borrar(identificador):
    conexion, cursor = conectar() 
    cursor.execute(f"DELETE FROM ALUMNO WHERE IDENTIFICADOR = {identificador}")
    
    conexion.commit()
    print("Alumno borrado")
    cerrar_conexion(conexion)       
    
if __name__=='__main__':    
 
 crear_tabla() 

 #Prueba de ingreso de datos



# Bucle para ingresar tres registros a la base de datos



""""
i = 0

print("INGRESO DE 3 ALUMNOS A LA BASE DE DATOS\n")
print("*"*80)
while i <3:
 i = i + 1
 nombre = str(input(f"Ingrese el nombre del estudiante #{i}: "))
 calificacion = -1
 while calificacion <0:
  calificacion = int(input(f"Ingrese la calificacion del estudiante #{i}: "))
 alumno = (i,nombre,calificacion)
 insertar(alumno)

"""



# Consultar la base de datos tras el ingreso
 
consultar()
                    

Alumnos = consultar() 


print("Lista de los nombres de los alumnos")
for Alumno in Alumnos:
    print(f"Nombre del alumno: {Alumno[1]}, Calificacion: {Alumno[2]}")


# Modificar datos de la tabla alumno

actualizar(1,"Jorge",4) 


# Borrar al estudiante con id 1

# borrar(1) 




 
 