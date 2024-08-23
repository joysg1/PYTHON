import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

def calcular_mcd(num1, num2):
    """Calcula el máximo común divisor utilizando el algoritmo de Euclides."""
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def calcular():
    try:
        numero1 = int(entry1.get())
        numero2 = int(entry2.get())
        mcd = calcular_mcd(numero1, numero2)
        resultado_label.config(text=f"El mínimo común divisor es: {mcd}", font=("Helvetica", 12, "bold"))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números enteros.", icon="warning")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de MCD")
ventana.geometry("350x200")
ventana.configure(bg="#f0f0f0")  # Color de fondo suave

# Crear los elementos de la interfaz
etiqueta1 = tk.Label(ventana, text="Ingrese el primer número:", font=("Helvetica", 12))
etiqueta1.pack(pady=10)

entry1 = tk.Entry(ventana, font=("Helvetica", 12))
entry1.pack()

etiqueta2 = tk.Label(ventana, text="Ingrese el segundo número:", font=("Helvetica", 12))
etiqueta2.pack(pady=10)

entry2 = tk.Entry(ventana, font=("Helvetica", 12))
entry2.pack()

boton_calcular = tk.Button(ventana, text="Calcular MCD", command=calcular, bg="#4CAF50", fg="white", font=("Helvetica", 12))
boton_calcular.pack(pady=15)

resultado_label = tk.Label(ventana, text="", font=("Helvetica", 14))
resultado_label.pack()

# Iniciar la aplicación
ventana.mainloop()