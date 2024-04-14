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


def insertar(datos):
    conexion, cursor = conectar()

    sql = """
           INSERT INTO agenda(nombre,telefono) VALUES(?,?)
           


         """
    if(cursor.execute(sql,datos)):
        print("Datos guardados")
    else:
        print("No se pudieron guardar los datos ") 

    conexion.commit()      
    conexion.close()  

def consultar():
    conexion, cursor = conectar()
    cursor.execute("SELECT id,nombre,telefono from agenda")   
    for fila in cursor:
        print("ID = ", fila[0])
        print("Nombre ", fila[1])
        print("Telefono ", fila[2], '\n')
    conexion.close()  
    
    
def modificar(id, telefono):
    conexion, cursor = conectar()
    sql = f" UPDATE agenda SET telefono = {telefono}  WHERE ID = {id} "
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
                               
                    
    
    conexion.close()
    
    
def borrar(id):
    conexion, cursor = conectar()
    sql = f"DELETE from agenda WHERE ID = {id}"
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()    
    
"""          

crearTabla()
datos = "Luis", "6543-2188"
datos2 = "Jose", "6457-9821"
datos3 = "Hagi" , "6234-8711"
insertar(datos)
insertar(datos2)
insertar(datos3)

consultar()
modificar(2,1111)

"""


consultar()

