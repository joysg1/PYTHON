from tkinter import Tk
from modulo_visual import Aplicacion
from modulo_db import Database


def main():
    root = Tk()
    app = Aplicacion(root)
    root.mainloop()

if __name__ == '__main__':
    main()