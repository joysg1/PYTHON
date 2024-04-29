from tkinter import *

def click():
    cadena = "Pulsaste "
    if (option.get()==1):
        cadena += " Rojo "
        ventana.config(bg="Red")
 
    if(option.get()==2):
        cadena += " Azul" 
        ventana.config(bg="Blue")
    if(option.get()==3):
        cadena +=" Verde" 
        ventana.config(bg="Green")      
    etiqueta.config(text=cadena)



ventana = Tk()

ventana.title("OptionButton")
ventana.geometry("640x360")
frame = Frame()
frame.pack()
option = IntVar()
rdRojo = Radiobutton(frame,text="Rojo",variable=option,value=1,command=click)
rdRojo.grid(column=1, row=3)


rdAzul = Radiobutton(frame,text="Azul",variable=option,value=2,command=click)
rdAzul.grid(column=1, row=4)

rdVerde = Radiobutton(frame,text="Verde",variable=option,value=3,command=click)
rdVerde.grid(column=1, row=5)

etiqueta = Label(frame,text = "Selecciona opcion" )
etiqueta.grid(column=1, row =7)

ventana.mainloop()