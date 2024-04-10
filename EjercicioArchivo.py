def GuardaTexto(nomA, texto):
    try:
     fichero = open(nomA + '.txt', 'w')
     fichero.write(texto) 
     print('Texto guardado')
     return True
    except Exception:
        print("Ha ocurrido un error") 
    finally:
       fichero.close()     
    

def LeeTexto(nomA):
    try:
     fichero = open(nomA + '.txt','r')
     texto = fichero.read()
     fichero.close()
     return texto
    except Exception:
        print("Ha ocurrido un error")
    finally:
        fichero.close()    

texto = str(input ("Por favor ingrese el texto a guardar: "))
archivo = str(input("Indique el nombre del archivo: "))

GuardaTexto(archivo, texto)
texto = LeeTexto(archivo)
print("Este es el texto del archivo: ")
print(texto)