import sqlite3

def conectar():
    conexion = sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    return conexion,cursor

def crearTabla():
    conexion,cursor = conectar()
    sql = "CREATE TABLE IF NOT EXISTS agenda(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre VARCHAR(20) NOT NULL, apellidos VARCHAR(20) NOT NULL, telefono VARCHAR(14) NOT NULL, email VARCHAR(20) NOT NULL)"
    if(cursor.execute(sql)):
        print("Tabla creada")
    else:
        print("Error al crear la tabla")
    conexion.close()
    
def insertar(datos):
    conexion,cursor = conectar()
    sql = "INSERT INTO agenda(nombre, apellidos, telefono, email) VALUES(?,?,?,?)"
    if(cursor.execute(sql,datos)):
        print("Datos guardados")
    else:
        print("Error al guardar")
    conexion.commit()
    conexion.close()
    
def consultar():
    conexion,cursor = conectar()
    cursor.execute("SELECT id,nombre,telefono from agenda")
    for fila in cursor:
        print("ID = ",fila[0])
        print("Nombre = ", fila[1])
        print("Telefono = ",fila[2], "\n")
    conexion.close()
    

#Video 119 minuto 20
        
    