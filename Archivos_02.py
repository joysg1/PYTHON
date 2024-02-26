import os

"""

carpeta = "/home/userj2/Documentos/CURSO_PYTHON/MiCarpeta/"
#print(carpeta)

listado = os.listdir(carpeta)

print(listado)
print(type(listado))

#filtrado para archivos mp3

for archivo in listado:
    if archivo.endswith(".mp3"):
        print("*"*80)
        print("Existe un archivo mp3 \n")
        print(f"Nombre del archivo {archivo}")
        

print("*"*80)


#filtrado para archivos .txt

for archivo in listado:
    if archivo.endswith(".txt"):
        print("*"*80)
        print("Existe un archivo txt \n")
        print(f"Nombre del archivo: {archivo}")
        
  

print("*"*80)        
        
#otra forma de filtrar

filtrado = [archivo for archivo in listado if archivo.endswith(".mp3")]
print(filtrado)

print(type(filtrado))

print("*"*80)

filtrado2 = [archivo for archivo in listado if archivo.endswith(".txt")]
print(filtrado2)
print(type(filtrado2))

"""

#cambio de directorio

os.chdir("/home/userj2/Documentos/CURSO_PYTHON/MiCarpeta/")

#renombrar un archivo

# os.rename("newfile.txt","newfileChangedName.txt")

# borrar un archivo
# os.remove("newfile")

# renombrar varios archivos a la vez

"""

contador = 1
listado = os.listdir(carpeta)
print(listado) 
print("fin listado inicial")
for archivo in os.listdir():
    nombre, extension = os.path.splitext(archivo)
    print(nombre)
    print(extension)
    nuevoNombre = f'renombrado: {str(contador)}_{nombre}{extension}'
    contador+=1
    os.rename(archivo,nuevoNombre)
    
listado = os.listdir(carpeta)
print("Print listado renombrado")
print("\n\n")
print(listado)    

"""


# copiar contenido de un fichero a otro

# try:
    
#  fichero = open("Contenido.txt","r")
#  nuevofichero = open("Contenido2.txt","w")

#  for linea in fichero:
#     nuevofichero.write(linea)
#  fichero.close()
#  nuevofichero.close() 

# except FileNotFoundError:
#     print("Disculpe el archivo no ha sido encontrado")

# otra forma de copiar contenido de un archivo a otro 

try:
 with open("Contenido.txt","r") as fichero:
    with open("Contenido2.txt","w") as nuevofichero:
        for linea in fichero:
            nuevofichero.write(linea)
except FileNotFoundError:
    print("Disculpe archivo no encontrado")          
    
    
       

        
    

