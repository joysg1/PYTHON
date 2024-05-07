import tkinter as tk

from tkinter import messagebox

import time

class relojDigital():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title = "Reloj Digital"
        self.ventana.geometry("300x200")
        self.label_hora = tk.label(ventana,text="",font=("Arial",20))
        self.label_hora.pack(pady=20)
        self.btn_inicio_crono =tk.Button(ventana, text = "Iniciar Cronometro",command=self.iniciar_cronometro)
        self.btn_inicio_crono.pack()

        #Min 8.21 Video 94



