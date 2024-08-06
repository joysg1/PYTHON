from tkinter import *
ventana = Tk()
ventana.title("Codifica")
ventana.config(bg="gray")
ventana.geometry("380x380")
frame = Frame()
frame.config(width=340, height=340)
frame.config(bg="cyan")
frame.pack()
textoSinCodificar = StringVar()
textoCodificado = StringVar()
etiquetaSinCodificar = Label(frame, text="Texto sin codificar: ").grid(row=3, column=1)
cajaSin = Entry(frame, textvariable=textoSinCodificar).grid(row=3, column=2)
etiquetaCodificada = Label(frame, text="Texto codificado: ").grid(row=4, column=1)
cajaCon = Entry(frame, textvariable=textoCodificado).grid(row=4, column=2)
botonCodificar = Button(frame, text="Codificar").grid(row=5, column=1)
botonDescodificar = Button(frame, text="Descodificar").grid(row=5, column=2)
botonGrabar = Button(frame, text="Grabar").grid(row=6, column=1)
botonCargar = Button(frame, text="Cargar").grid(row=6, column=2)
botonBorrar = Button(frame, text="Borrar").grid(row=7, column=1)


ventana.mainloop()

# Video 122 minuto 20

