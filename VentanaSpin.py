from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry("640x480")

def mostrar():
    messagebox.showinfo("Mensaje ","Valor seleccionado " + valor.get())
valor = StringVar()
etiqueta = Label(ventana,text="Spinbox").place(x=20,y=20)
combo=Spinbox(ventana,from_=1, to =10,textvariable=valor).place(x=20,y=20)
boton = Button(ventana,text="Valor = ",command=mostrar).place(x=20,y=100)
ventana.mainloop()