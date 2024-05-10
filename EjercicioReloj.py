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
        self.cronometro_activo = False
        
    def iniciar_reloj(self):
        hora_actual = time.strftime("%H:%M:%S")
        self.lbl_hora.config(text=hora_actual)
        self.lbl_hora.after(1000,self.iniciar_reloj)
        
    def iniciar_cronometro(self):
        self.tiempo_inicio = time.time()
        self.btn_iniciar_cronometro.config(state="disabled")
        self.btn_detener_cronometro.config(state="normal")
        self.cronometro_activo = True
        self.actualizar_cronometro()
    
    def detener_cronometro(self):
        self.btn_iniciar_cronometro.config(state="normal")
        self.btn_detener_cronometro.config(state="disabled")
        self.cronometro_activo = False
        
    def actualizar_cronometro(self):
        if self.cronometro_activo:
            tiempo_transcurrido = time.time - self.tiempo_inicio
            tiempo_formato = time.strftime("%H:%M:%S",time.gm(tiempo_transcurrido)) 
            self.lbl_hora.config(text=tiempo_formato) 
            self.lbl_hora.after(1000,self.actualizar_cronometro) 
            
        #Min 20.14 Video 94



