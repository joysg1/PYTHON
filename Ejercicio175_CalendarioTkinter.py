import customtkinter
from tkinter import messagebox
import calendar
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk  # Importar tkinter para usar tk.CENTER

# Configuración de CustomTkinter
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Crear la ventana principal
app = customtkinter.CTk()
app.geometry("400x350")
app.title("Calendario Personalizado")

# Crear los elementos de la interfaz
label_mes = customtkinter.CTkLabel(master=app, text="Ingrese el mes (1-12):", font=("Arial", 12))
label_mes.pack(pady=10)

entry_mes = customtkinter.CTkEntry(master=app, font=("Arial", 12))
entry_mes.pack()

label_año = customtkinter.CTkLabel(master=app, text="Ingrese el año:", font=("Arial", 12))
label_año.pack(pady=10)

entry_año = customtkinter.CTkEntry(master=app, font=("Arial", 12))
entry_año.pack()

calendario_frame = customtkinter.CTkFrame(master=app, corner_radius=10)
calendario_frame.pack(pady=10)

calendario_label = customtkinter.CTkLabel(master=calendario_frame, text="", justify=tk.CENTER, font=("Courier New", 12))
calendario_label.pack(padx=20, pady=20)

def generar_calendario():
    """Genera y muestra el calendario según el mes y año ingresados."""
    try:
        mes = int(entry_mes.get())
        año = int(entry_año.get())
        
        if 1 <= mes <= 12:
            cal = calendar.month(año, mes)
            calendario_label.configure(text=cal)  # Usa configure en lugar de config
        else:
            messagebox.showerror("Error", "El mes debe estar entre 1 y 12.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un mes y un año válidos.")

def guardar_imagen():
    """Guarda el calendario mostrado como una imagen PNG."""
    # Crear una imagen en blanco
    imagen = Image.new('RGB', (300, 250), color=(0, 0, 0))  # Ajusta el tamaño según sea necesario
    draw = ImageDraw.Draw(imagen)
    font = ImageFont.load_default()  # Usa la fuente por defecto; puedes especificar una fuente diferente si lo deseas

    # Extraer el texto del calendario
    cal_text = calendario_label.cget("text")
    
    # Dibujar el texto en la imagen
    draw.text((10, 10), cal_text, font=font, fill=(255, 255, 255))

    # Guardar la imagen
    imagen.save("calendario.png")
    messagebox.showinfo("Éxito", "Calendario guardado como imagen PNG")

button_generar = customtkinter.CTkButton(master=app, text="Generar Calendario", command=generar_calendario,
                                       font=("Arial", 12))
button_generar.pack(pady=15)

button_guardar = customtkinter.CTkButton(master=app, text="Guardar como Imagen", command=guardar_imagen,
                                        font=("Arial", 12))
button_guardar.pack(pady=10)

app.mainloop()
