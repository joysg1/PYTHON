from tkinter import *

def click():
    texto = "Hola , "+entrada.get()
    etiqueta.configure(text=texto)

ventana = Tk()

ventana.title("Mi primera ventana con python")

ventana.resizable(True,True)
ventana.geometry("640x480")
ventana.config(bg="green")
frame = Frame()
frame.pack()
frame.config(bg="yellow")
frame.config(width=640,height=350)
etiqueta = Label(frame, text="Etiqueta")

etiqueta.grid(column=1,row=2)
entrada = Entry(frame, width = 50)
entrada.grid(column=2, row=2)
boton = Button(frame, text = "Pulsame",background="red", foreground="yellow",command = click)
boton.grid(column = 1, row = 4)
ventana.mainloop()