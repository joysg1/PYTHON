import qrcode 

nombreArchivo = input("Ingrese el nombre del archivo sin la extension: ")
textoQR = input("Ingrese el texto para el codigo QR: ")

imagen = qrcode.make(textoQR)
fichero = open(nombreArchivo + ".png", "wb")
imagen.save(fichero)
fichero.close()
print("Codigo QR generado con exito")
print("El archivo esta guardado en la carpeta del script")
