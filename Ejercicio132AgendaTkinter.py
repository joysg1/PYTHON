from tkinter import *
from tkinter import StringVar
ANCHO = 560
ALTO = 540
POSX = 400
POSY = 400
anchoAlto = str(ANCHO) + "x" + str(ALTO)
posicionX = "+" + str(POSX)
posicionY = "+" + str(POSY)
colorVentana = "blue"
colorFondo ="blue"
colorLetra ="white"
ventana=Tk()
ventana.config(bg=colorVentana)
ventana.geometry(anchoAlto+posicionX+posicionY)
ventana.title("Agenda")
frame = Frame()
frame.config(width=ANCHO,height=ALTO)
frame.config(bg=colorVentana)
frame.pack()

#variables
ID = IntVar()
nombre = StringVar()
apellidos = StringVar()
telefono = StringVar()
email = StringVar()

#widgets
etiquetaID = Label(frame,text="ID: ").place(x=50,y=50)
cajaID = Entry(frame, textvariable=ID).place(x=130, y=50)
etiquetaNombre=Label(frame,text="Nombre: ").place(x=50, y=90)
cajaNombre = Entry(frame,textvariable=nombre).place(x=130, y=90)
etiquetaApellidos = Label(frame, text="Apellidos: ").place(x=50, y=130)
cajaApellidos = Entry(frame, textvariable=apellidos).place(x=130, y=130)
etiquetaTelefono = Label(frame, text="Teléfono: ").place(x=50, y=170)
cajaTelefono = Entry(frame, textvariable=telefono).place(x=130, y=170)
etiquetaEmail = Label(frame, text="Email: ").place(x=50, y=210)
cajaEmail = Entry(frame, textvariable=email).place(x=130, y=210)
text = Text(frame)
text.place(x=50, y=240, width=500,height=200)
botonAnadir = Button(frame, text="Añadir").place(x=150, y=500)
botonBorrar = Button(frame, text="Borrar").place(x=200, y=500)
botonConsultar = Button(frame, text="Consultar").place(x=250, y=500)
botonModificar = Button(frame, text="Modificar").place(x=320, y=500)
ventana.mainloop()

