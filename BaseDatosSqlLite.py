import sqlite3


def conectar():
    conexion = sqlite3.connect("miDB.db")
    cursor = conexion.cursor()
    return conexion, cursor

def crearTabla():
    conexion, cursor = conectar()
    sql = """
           CREATE TABLE IF NOT EXISTS agenda (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR (20) NOT NULL,
            telefono VARCHAR(14) NOT NULL

            )

         """
    
    if (cursor.execute(sql)):
        print("Tabla creada")
    else:
        print("No se pudo crear la tabla")    
    conexion.close()

crearTabla()

