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
        self.btn_detener_crono = tk.Button(ventana,text = "Detener Cronometro",command=self.detener_cronometro,state="disabled")
        self.btn_detener_crono.pack()
        
        self.btn_configurar_alarma = tk.Button(ventana,text="Configurar Alarma",command=self.configurar_alarma)
        self.btn_configurar_alarma.pack()
        
        self.btn_activar_alarma = tk.Button(ventana, text = 'Activar Alarma',command=self.activar_alarma, state = "disabled")
        self.btn_activar_alarma.pack()
        #Min 12.24 Video 94



