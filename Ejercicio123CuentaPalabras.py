def cuentaPalabras(texto):
    palabras =texto.split(" ")
    palabrasContadas ={}
    contador = 0
    longitud = len(palabras)
    for i in range(0,longitud):
        primera = palabras[i]
        for j in range(0,longitud):
            segunda = palabras[j]
            if primera ==segunda:
                contador +=1
        palabrasContadas[primera] = contador
        contador =0
    return palabrasContadas

try:
    fichero = open("FicheroCuentaPalabra.txt","r",encoding="utf-8")
    texto= fichero.read()
    print("Fichero correcto")
    
except:
    print("Error al abrir el fichero")
finally:
    print("Fichero cerrado")
    fichero.close()
    

cuentaPalabras = cuentaPalabras(texto)
print(cuentaPalabras)


