import sqlite3

def conectar():
    conexion = sqlite3.connect('articulos.db')
    cursor = conexion.cursor()
    print('Conectado a la base de datos')
    return conexion, cursor

def cerrar_conexion(conexion):
    conexion.close()
    

def crear_tabla():
    conexion, cursor = conectar()
    cursor.execute('CREATE TABLE IF NOT EXISTS ARTICULOS (IDENTIFICADOR INT PRIMARY KEY, NOMBRE VARCHAR(20), CANTIDAD INT, IMPORTE FLOAT)')
    cerrar_conexion(conexion)
    print("Tabla creada")
    
def insertar(articulo):
    conexion, cursor = conectar()
    cursor.execute('INSERT INTO ARTICULOS VALUES (?,?,?,?)',articulo)
    conexion.commit()
    cerrar_conexion(conexion) 
    
    
def consultar(): 
    conexion, cursor = conectar()  
    cursor.execute('SELECT * FROM articulos')
    articulos = cursor.fetchall()
    cerrar_conexion(conexion) 
    print("CONSULTA REALIZADA") 
    return articulos



    



def actualizar(identificador, nombre, cantidad, importe):
    conexion, cursor = conectar() 
    
    cursor.execute(f" UPDATE ARTICULOS SET nombre = '{nombre}' , cantidad = {cantidad} , importe = {importe} WHERE IDENTIFICADOR = {identificador}")
    print("Articulo actualizado")
    conexion.commit()
    cerrar_conexion(conexion) 
    
    
def borrar(identificador):
    conexion, cursor = conectar() 
    cursor.execute(f"DELETE FROM ARTICULOS WHERE IDENTIFICADOR = {identificador}")
    
    conexion.commit()
    print("Articulo borrado")
    cerrar_conexion(conexion)   

def carga_inicial():
    conexion, cursor = conectar()
    articulos = [
        (1,'Cuaderno',20,2.36),
        (2, 'Lapiz',10,0.50),
        (3, 'Borrador',12,1.89),
        (4, 'Boligrafo',5,2.30)  
        
    ] 
    
    cursor.executemany('INSERT INTO ARTICULOS VALUES (?,?,?,?)',articulos)
    conexion.commit()
    cerrar_conexion(conexion)
 
if __name__=='__main__':    
 
 crear_tabla() 


 # carga_inicial()
 
 
 
 """
 articulo = (6, "Libreta",10,2.50)
 insertar(articulo)
 
 """
 

# actualizar(1,'Cuaderno Grande',10,1.50)


"""

borrar(5)
borrar(1)

"""

articulos = consultar() 

print("Lista de los nombres de los articulos")
for articulo in articulos:
    print(articulo[1])
 


