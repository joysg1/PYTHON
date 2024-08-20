import tkinter as tk
from tkinter import messagebox

# Tamaños originales de la ventana
ancho_original = 300
alto_original = 100

def es_primo(num):
    """Determina si un número es primo.

    Args:
        num: El número a evaluar.

    Returns:
        True si el número es primo, False en caso contrario.
    """

    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def comprobar_primo():
    """Obtiene el número ingresado por el usuario y verifica si es primo.
    Ajusta el tamaño de la ventana según el resultado.
    """

    try:
        num = int(entry.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número entero.")
        return

    if es_primo(num):
        messagebox.showinfo("Resultado", f"El número {num} es primo.")
        # Aumenta el tamaño de la ventana si es primo
        ventana.geometry(f"{ancho_original+100}x{alto_original+50}")
    else:
        messagebox.showinfo("Resultado", f"El número {num} no es primo.")
        # Restaura el tamaño original de la ventana
        ventana.geometry(f"{ancho_original}x{alto_original}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Detector de Números Primos")
ventana.geometry(f"{ancho_original}x{alto_original}")

# Crear un label y un campo de entrada
label = tk.Label(ventana, text="Ingrese un número:")
label.pack()

entry = tk.Entry(ventana)
entry.pack()

# Crear un botón para ejecutar la comprobación
boton = tk.Button(ventana, text="Comprobar", command=comprobar_primo)
boton.pack()

ventana.mainloop()