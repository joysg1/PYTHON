#guardar datos en archivo

#abrimos el archivo

escritura = open("Archivo.txt","w")

escritura.write("Escribiendo en el archivo \n")
escritura.write("*"*80)
escritura.close()

#lectura de una linea del fichero

lectura = open("Archivo.txt","r")

#leemos una linea

leeLinea = lectura.readline()
print(f"Lectura de una linea: {leeLinea}")
lectura.close()



#lectura de todo el fichero

lectura = open("Archivo.txt","r")

leefichero = lectura.read()
print(f"Lectura de todo el fichero: {leefichero}")

#indicar el tipo de objeto de leefichero

tipoLeefichero = type(leefichero)

print(f"Tipo de objeto leefichero: {tipoLeefichero}")

lectura.close()



    