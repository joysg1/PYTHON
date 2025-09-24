from PIL import Image
import matplotlib.pyplot as plt

# Cargar la imagen
im = Image.open(r"/home/userlm/Documentos/IMAGE_LOAD/L.jpg")

# Crear una figura y un eje
fig, ax = plt.subplots()

# Mostrar la imagen
ax.imshow(im)

# Agregar texto con la información de la imagen
ax.text(0.05, 0.9, f"Formato: {im.format}", transform=ax.transAxes, fontsize=10, color='yellow')
ax.text(0.05, 0.85, f"Tamaño: {im.size}", transform=ax.transAxes, fontsize=10, color='yellow')
ax.text(0.05, 0.8, f"Modo: {im.mode}", transform=ax.transAxes, fontsize=10, color='yellow')
ax.text(0.05, 0.75, f"Ancho: {im.width}", transform=ax.transAxes, fontsize=10, color='yellow')
ax.text(0.05, 0.7, f"Alto: {im.height}", transform=ax.transAxes, fontsize=10, color='yellow')

# Desactivar ejes
ax.axis('off')

# Mostrar la figura
plt.show()

