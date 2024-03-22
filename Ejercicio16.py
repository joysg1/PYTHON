
repetir = ""

while repetir !="n":
 # Nota el parametro a permite escribir en el archivo desde el final
 escritura = open("ArchivoTexto16.txt","a")
 textoIncluir = str(input("Por favor ingrese la linea de texto que desea agregar al archivo: "))
 escritura.write(textoIncluir + "\n")
 repetir = str(input("Desea incluir una nueva linea de texto s/n: "))
 if repetir =="N" or repetir =="n":
  escritura.close()
   
print("\n")
print("*"*80)

# Lectura del archivo
lectura = open("ArchivoTexto16.txt","r")
leefichero = lectura.read()

print("--- CONTENIDO DEL ARCHIVO ----")
print(f"Contenido del fichero = {leefichero}")
lectura.close()





