def cadenaReves(cadena):
    alreves = ""
    contador = len(cadena) 
    indice = -1
    while contador >=1:
        alreves += cadena[indice]
        indice = indice +(-1)
        contador = contador -1
    return alreves

print(cadenaReves("hola"))
        