import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

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

def encontrar_primos(inicio, fin):
    """Encuentra los números primos en un intervalo.

    Args:
        inicio: Límite inferior del intervalo.
        fin: Límite superior del intervalo.

    Returns:
        Una lista con los números primos encontrados.
    """

    primos = []
    for num in range(inicio, fin + 1):
        if es_primo(num):
            primos.append(num)
    return primos

def generar_grafica(primos, inicio, fin):
    """Genera una gráfica lineal marcando los números primos.

    Args:
        primos: Lista de números primos.
        inicio: Límite inferior del intervalo.
        fin: Límite superior del intervalo.
    """

    x = np.arange(inicio, fin + 1)
    y = np.zeros_like(x)
    for primo in primos:
        y[primo - inicio] = 1

    plt.figure(figsize=(12, 6))
    plt.scatter(x[y == 1], y[y == 1], color='red', label='Números primos', s=80)
    plt.scatter(x[y == 0], y[y == 0], color='gray', label='Números compuestos', s=20)
    plt.xlabel("Número")
    plt.ylabel("Tipo de número")
    plt.title(f"Distribución de números primos entre {inicio} y {fin}")

    # Agregar etiquetas sobre los puntos de los números primos
    for primo in primos:
        plt.annotate(str(primo), (primo, 1), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.legend()
    plt.grid(True)
    plt.show()

def comprobar_primos():
    try:
        inicio = int(entry_inicio.get())
        fin = int(entry_fin.get())
        if inicio >= fin:
            messagebox.showerror("Error", "El límite inferior debe ser menor que el superior.")
            return

        primos = encontrar_primos(inicio, fin)
        generar_grafica(primos, inicio, fin)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números enteros válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Detector de Números Primos")

# Crear un label y un campo de entrada para el límite inferior
label_inicio = tk.Label(ventana, text="Límite inferior:")
label_inicio.pack()
entry_inicio = tk.Entry(ventana)
entry_inicio.pack()

# Crear un label y un campo de entrada para el límite superior
label_fin = tk.Label(ventana, text="Límite superior:")
label_fin.pack()
entry_fin = tk.Entry(ventana)
entry_fin.pack()

# Crear un botón para ejecutar la comprobación
boton = tk.Button(ventana, text="Comprobar", command=comprobar_primos)
boton.pack()

ventana.mainloop()