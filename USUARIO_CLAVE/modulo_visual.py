import tkinter as tk
from tkinter import messagebox
from modulo_db import Database
from cryptography.fernet import Fernet
import random
import string


class Aplicacion:
    def __init__(self,root):
        self.root = root
        self.root.title("Almacenamiento de usuarios y contraseñas")
        self.db = Database("mi_base_de_datos.db")
        self.clave_encriptacion = Fernet.generate_key()
        self.cipher_suite = Fernet(self.clave_encriptacion)

        #etiquetas y cajas de texto

        lbl_id = tk.Label(root, text="ID")
        lbl_id.grid(row = 0, column =0)
        self.entry_id = tk.Entry(root)
        self.entry_id.grid(row = 0, column =1)

        lbl_url = tk.Label(root, text="URL")
        lbl_url.grid(row = 1, column =0)
        self.entry_url = tk.Entry(root)
        self.entry_url.grid(row = 1, column =1)

        lbl_usuario = tk.Label(root, text="USUARIO")
        lbl_usuario.grid(row = 2, column =0)
        self.entry_url = tk.Entry(root)
        self.entry_url.grid(row = 2, column =1)

        lbl_clave = tk.Label(root, text="CLAVE")
        lbl_clave.grid(row = 3, column =0)
        self.entry_clave = tk.Entry(root)
        self.entry_clave.grid(row = 3, column =1)

        lbl_nota = tk.Label(root, text="NOTA")
        lbl_nota.grid(row = 4, column =0)
        self.entry_nota = tk.Entry(root)
        self.entry_nota.grid(row = 4, column =1)


