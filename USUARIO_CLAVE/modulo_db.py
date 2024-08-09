import sqlite3
from cryptography.fernet import Fernet
from modulo_cripto import obtener_clave


class Database:
    def __init__(self, nombre_base_datos):
        self.conn = sqlite3.connect(nombre_base_datos)
        self.cursor = self.conn.cursor()
        self.crear_tabla()
        
        
        

    def crear_tabla(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                url TEXT NOT NULL,
                                usuario TEXT NOT NULL,
                                clave TEXT NOT NULL,
                                nota TEXT)
                            
                            ''')
        self.conn.commit()

    def insertar_registro(self, url, usuario, clave, nota):
        
        self.cursor.execute("INSERT INTO usuarios (url, usuario, clave, nota) VALUES (?, ?, ?, ?)", (url, usuario,clave, nota))
        self.conn.commit()
     
    
    def borrar_registro(self, id):
        self.cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        self.conn.commit()

    def buscar_registro(self, id):
        self.cursor.execute("SELECT *from usuarios WHERE id = ?",(id,))
        return self.cursor.fetchone()
    
    def actualizar_registro(self, id, url, usuario, clave, nota):
        
        self.cursor.execute("UPDATE usuarios SET url = ?, usuario = ?, clave = ?, nota = ? WHERE id = ?", (url, usuario, clave, nota, id))
        self.conn.commit()
    
    
    def cerrar_conexion(self):
        self.conn.close()


