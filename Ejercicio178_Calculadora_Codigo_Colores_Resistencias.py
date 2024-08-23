import customtkinter
from tkinter import messagebox
import tkinter as tk

# Configuración de CustomTkinter
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Diccionario de colores y valores de bandas de resistencia
COLOR_VALUES = {
    "Negro": 0,
    "Marrón": 1,
    "Rojo": 2,
    "Naranja": 3,
    "Amarillo": 4,
    "Verde": 5,
    "Azul": 6,
    "Violeta": 7,
    "Gris": 8,
    "Blanco": 9
}

# Crear la ventana principal
app = customtkinter.CTk()
app.geometry("400x600")
app.title("Calculadora de Valor de Resistencia")

# Crear los elementos de la interfaz
label_banda1 = customtkinter.CTkLabel(master=app, text="Seleccione el color de la Banda 1:", font=("Arial", 18))
label_banda1.pack(pady=10)

color_options = list(COLOR_VALUES.keys())

# Crear una ventana para el combobox de la Banda 1
banda1_frame = customtkinter.CTkFrame(master=app, corner_radius=10)
banda1_frame.pack(pady=5)

banda1_listbox = customtkinter.CTkComboBox(master=banda1_frame, values=color_options, font=("Arial", 12))
banda1_listbox.pack(pady=5)

# Crear una ventana para el combobox de la Banda 2
label_banda2 = customtkinter.CTkLabel(master=app, text="Seleccione el color de la Banda 2:", font=("Arial", 18))
label_banda2.pack(pady=10)

banda2_frame = customtkinter.CTkFrame(master=app, corner_radius=10)
banda2_frame.pack(pady=5)

banda2_listbox = customtkinter.CTkComboBox(master=banda2_frame, values=color_options, font=("Arial", 12))
banda2_listbox.pack(pady=5)

# Crear una ventana para el combobox de la Banda 3
label_banda3 = customtkinter.CTkLabel(master=app, text="Seleccione el color de la Banda 3:", font=("Arial", 18))
label_banda3.pack(pady=10)

banda3_frame = customtkinter.CTkFrame(master=app, corner_radius=10)
banda3_frame.pack(pady=5)

banda3_listbox = customtkinter.CTkComboBox(master=banda3_frame, values=color_options, font=("Arial", 12))
banda3_listbox.pack(pady=5)

# Crear una ventana para el combobox de la Banda 4
label_banda4 = customtkinter.CTkLabel(master=app, text="Seleccione el color de la Banda 4 (Multiplicador):", font=("Arial", 18))
label_banda4.pack(pady=10)

banda4_frame = customtkinter.CTkFrame(master=app, corner_radius=10)
banda4_frame.pack(pady=5)

banda4_listbox = customtkinter.CTkComboBox(master=banda4_frame, values=color_options, font=("Arial", 12))
banda4_listbox.pack(pady=5)

# Función para cambiar el color de la ventana en función de la selección
def cambiar_color(frame, combo):
    color = combo.get()
    if color == "Negro":
        frame.configure(fg_color="#000000")
    elif color == "Marrón":
        frame.configure(fg_color="#964B00")
    elif color == "Rojo":
        frame.configure(fg_color="#FF0000")
    elif color == "Naranja":
        frame.configure(fg_color="#FFA500")
    elif color == "Amarillo":
        frame.configure(fg_color="#FFFF00")
    elif color == "Verde":
        frame.configure(fg_color="#008000")
    elif color == "Azul":
        frame.configure(fg_color="#0000FF")
    elif color == "Violeta":
        frame.configure(fg_color="#800080")
    elif color == "Gris":
        frame.configure(fg_color="#808080")
    elif color == "Blanco":
        frame.configure(fg_color="#FFFFFF")

# Agregar la función a los combobox
banda1_listbox.configure(command=lambda x: cambiar_color(banda1_frame, banda1_listbox))
banda2_listbox.configure(command=lambda x: cambiar_color(banda2_frame, banda2_listbox))
banda3_listbox.configure(command=lambda x: cambiar_color(banda3_frame, banda3_listbox))
banda4_listbox.configure(command=lambda x: cambiar_color(banda4_frame, banda4_listbox))

result_frame = customtkinter.CTkFrame(master=app, corner_radius=10)
result_frame.pack(pady=10)

result_label = customtkinter.CTkLabel(master=result_frame, text="", justify=tk.CENTER, font=("Courier New", 12))
result_label.pack(padx=20, pady=20)

def calcular_valor_resistencia():
    """Calcula y muestra el valor de la resistencia basado en los colores seleccionados."""
    try:
        banda1 = banda1_listbox.get()
        banda2 = banda2_listbox.get()
        banda3 = banda3_listbox.get()
        banda4 = banda4_listbox.get()
        
        if not all([banda1, banda2, banda3, banda4]):
            messagebox.showerror("Error", "Por favor, seleccione todos los colores de las bandas.")
            return
        
        valor_banda1 = COLOR_VALUES[banda1]
        valor_banda2 = COLOR_VALUES[banda2]
        multiplicador = 10 ** COLOR_VALUES[banda4]
        
        # El valor de la resistencia es (banda1*10 + banda2) * multiplicador
        valor_resistencia = (valor_banda1 * 10 + valor_banda2) * multiplicador
        
        result_label.configure(text=f"Valor de la Resistencia: {valor_resistencia:.2e} ohmios")
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {str(e)}")

button_calcular = customtkinter.CTkButton(master=app, text="Calcular Valor de Resistencia", command=calcular_valor_resistencia,
                                         font=("Arial", 18))
button_calcular.pack(pady=15)

# Ejecutar la aplicación
app.mainloop()








