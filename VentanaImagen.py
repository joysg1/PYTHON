from tkinter import *

from PIL import ImageTk, Image

ventana = Tk()
ventana.geometry("200x200")
imagen = ImageTk.PhotoImage(Image.open("logoP.png"))

imgLabel = Label(ventana,image= imagen).place(x=50, y=50)
ventana.mainloop()
