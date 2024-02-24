import os
#crear carpeta o directorio

# os.makedirs("MiCarpeta")

#listar el contenido del directorio

# print(os.listdir("./"))

#mostrar directorio actual

# print(os.getcwd())

#mostrar tamano de la carpeta indicada

# print(os.path.getsize("MiCarpeta"))

#comprobar si se trata de un archivo

# print(os.path.isfile("MiCarpeta"))

#comprobar si se trata de una carpeta

# print(os.path.isdir("MiCarpeta"))

#cambiar de directorio

# os.chdir("MiCarpeta")
# print(os.getcwd())
# print(os.listdir("./"))

#crear carpeta dentro

# print("*"*80)

#os.makedirs("MiCarpeta2")
#os.chdir("MiCarpeta2")
#print(os.getcwd())
#print(os.listdir("./"))

# Regresamos un nivel de directorio
#os.chdir("../")
#print(os.getcwd())
#print(os.listdir("./"))

# Renombrar la carpeta

#os.rename("MiCarpeta","Mi_Carpeta")

#print(os.listdir("./"))


# Nos movemos a la carpeta de adentro

#os.chdir("Mi_Carpeta")
#os.chdir("MiCarpeta2")


#print(os.getcwd())
#print(os.listdir("./"))

#Volvemos a la carpeta superior 
#os.chdir("../")
#print(os.getcwd())
#print(os.listdir("./"))

# Borrar una carpeta de adentro

#os.rmdir("MiCarpeta2")

#Borrar archivo

# os.remove(os.getcwd()+"/Archivo.txt")

