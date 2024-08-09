import sqlite3
from cryptography.fernet import Fernet

class Database:
    def __init__(self, nombre_base_datos):
        self.conn = sqlite3.connect(nombre_base_datos)
        self.cursor = self.conn.cursor()
        self.crear_tabla()
        #clave de encriptacion
        self.clave_encriptacion = Fernet.generate_key()
        self.cipher_suite = Fernet(self.clave_encriptacion)

    def crear_tabla(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                url TEXT NOT NULL,
                                usuario TEXT NOT NULL,
                                clave TEXT NOT NULL)
                                nota TEXT
                            
                            ''')
        self.conn.commit()

    def insertar_registro(self, url, usuario, clave, nota):
        clave_encriptada = self.encriptar(clave)
        self.cursor.execute("INSERT INTO usuarios (url, usuario, clave, nota) VALUES (?, ?, ?, ?)", (url, usuario, clave_encriptada, nota))
        self.cursor.commit()
    
    def encriptar(self, texto_plano):
        texto_encriptado = self.cipher_suite.encrypt(texto_plano.encode())
        return texto_encriptado.decode()
    
    def borrar_registro(self, id):
        self.cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        self.conn.commit()

    def buscar_registro(self, id):
        self.cursor.execute("SELECT *from usuarios WHERE id = ?",(id,))
        return self.cursor.fetchone()
    
    def desencriptar(self, texto_encriptado):
        texto_plano = self.cipher_suite.decrypt(texto_encriptado.encode()).decode()
        return texto_plano.decode()
    
    def cerrar_conexion(self):
        self.conn.close()


if __name__ == "__main__":
    db = Database("base_datos.db")
    db.cerrar_conexion()
    print("Conexion cerrada")