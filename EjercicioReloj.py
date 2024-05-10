import tkinter as tk

from tkinter import messagebox, simpledialog    

import time

class relojDigital():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title = "Reloj Digital"
        self.ventana.geometry("300x200")
        self.label_hora = tk.Label(ventana,text="",font=("Arial",20))
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
        self.label_hora.config(text=hora_actual)
        self.label_hora.after(1000,self.iniciar_reloj)
        
    def iniciar_cronometro(self):
        self.tiempo_inicio = time.time()
        self.btn_inicio_crono.config(state="disabled")
        self.btn_detener_crono.config(state="normal")
        self.cronometro_activo = True
        self.actualizar_cronometro()
    
    def detener_cronometro(self):
        self.btn_inicio_crono.config(state="normal")
        self.btn_detener_crono.config(state="disabled")
        self.cronometro_activo = False
        
    def actualizar_cronometro(self):
        if self.cronometro_activo:
            tiempo_transcurrido = time.time() - self.tiempo_inicio
            tiempo_formato = time.strftime("%H:%M:%S",time.gmtime(tiempo_transcurrido)) 
            self.label_hora.config(text=tiempo_formato) 
            self.label_hora.after(1000,self.actualizar_cronometro) 
            
    
    def configurar_alarma(self):
        self.hora_alarma =tk.simpledialog.askstring("Configurar Alarma", "Ingrese la hora de la alarma (HH:MM)")
        self.btn_activar_alarma.config(state="enabled")

    def activar_alarma(self):
        hora_actual = time.strftime("%H:%M")
        if hora_actual == self.hora_alarma:
            messagebox.showinfo("Alarma", "Alarma activada")
        else:
            self.ventana.after(6000,self.activar_alarma)

    
    
if __name__ == "__main__":
    ventana = tk.Tk()
    new_reloj_digital = relojDigital(ventana)
    new_reloj_digital.iniciar_reloj()
    ventana.mainloop() 
       
# Min 26.14 video 94
# Verificar seccion de configurar alarma









