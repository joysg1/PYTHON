def crear_archivos(num_archivos):
    for i in range(1, num_archivos + 1):
       if i <10:
           contador = "0" +str(i)
       else:
           contador = str(i)
       nombre_archivo = f"Fichero_texto {contador}.txt"
       with open(nombre_archivo, "w") as archivo:
           archivo.write(str(i))

if __name__ == "__main__":
    num_archivos = int(input("Ingrese el número de archivos a crear: "))
    crear_archivos(num_archivos)