from tkinter import *


def click():
    cadena = "Pulsaste "
    if (color01.get):
        cadena = ""
        cadena += " Rojo "
        ventana.config(bg="Red")
 
    if(color02.get()):
        cadena = ""
        cadena += " Azul " 
        ventana.config(bg="Blue")
    if(color03.get()):
        cadena = ""
        cadena +=" Verde " 
        ventana.config(bg="Green")
             
    
    if(not color01.get() and not color02.get() and not color03.get()):
        cadena = ""
        cadena = "No hay nada pulsado"
        ventana.config(bg="white")

    etiqueta.config(text=cadena)


ventana = Tk()

ventana.title("OptionButton")
ventana.geometry("640x360")
frame = Frame()
frame.pack()

color01 = IntVar()
color02 = IntVar()
color03 = IntVar()

chkRojo = Checkbutton(frame,text="Rojo",variable=color01,onvalue=1, offvalue=0, command=click)
chkRojo.grid(column=1, row=2)

chkAzul = Checkbutton(frame,text="Azul",variable=color02,onvalue=1, offvalue=0, command=click)
chkAzul.grid(column=1, row=3)

chkVerde = Checkbutton(frame,text="Verde",variable=color03,onvalue=1, offvalue=0, command=click)
chkVerde.grid(column=1, row=4)



etiqueta = Label(frame,text = "Selecciona opcion" )
etiqueta.grid(column=1, row =7)

ventana.mainloop()