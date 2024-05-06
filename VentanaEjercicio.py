from tkinter import *

# constantes 

ANCHO = 600
ALTO = 400
POSX = 300
POSY = 100

def click():
    texto = "Hola, "+ nombre.get() 
    etiquetaResultado.configure(text = texto)

anchoAlto = str(ANCHO) + "x" + str(ALTO)
posicionX = "+" +str(POSX)
posicionY = "+" +str(POSY)

ventana = Tk()
ventana.title ("Ejercicio Saludo")
ventana.resizable(True,True)
ventana.config()
ventana.geometry(anchoAlto+posicionX+posicionY)
frame = Frame()
frame.pack()
frame.config()

#variables

nombre = StringVar()
edad = IntVar()

etiquetaNombre = Label(frame,text = "Nombre",font=("Arial",12))
etiquetaNombre.grid(column = 1, row = 2)
entradaNombre = Entry(frame,textvariable=nombre,width=50)
entradaNombre.grid(column=2,row=2)



nombre.set("Ingrese su nombre")


etiquetaResultado = Label(frame,text = "----",font=("Arial",12))
etiquetaResultado.grid(column = 2, row = 7)
boton = Button(frame,text = "pulsame",bg="red",fg="yellow",command=click)
boton.grid(column=2,row=5)
ventana.mainloop()