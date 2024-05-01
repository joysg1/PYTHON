from tkinter import *
from tkinter import messagebox

def info():
    messagebox.showinfo("Mensaje","Mensaje de informacion")
    
def advertencia():
    messagebox.showwarning("Mensaje","Mensaje de advertencia")

def pregunta():
    messagebox.askyesno("Mensaje","Quieres continuar")  

ventana = Tk()

ventana.geometry("640x480")
boton1 = Button(ventana, text = "MessageBox", command=info).place(x=100,y=100)
boton2 = Button(ventana, text = "Advertencia",command=advertencia).place(x=100, y=200)
boton3 = Button(ventana, text = "Pregunta",command=pregunta).place(x=100, y=300)
ventana.mainloop()