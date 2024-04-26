from tkinter import *

ventana = Tk()

ventana.title("Mi primera ventana con python")

ventana.resizable(True,True)
ventana.geometry("640x480")
ventana.config(bg="red")
frame = Frame()
frame.pack(side="left", anchor = "s")
frame.config(bg="yellow")
frame.config(width=640,height=350)
ventana.mainloop()