def numvocales(frase):
    vocales = "aeiouAEIOU"
    contador = 0
    print(f"Texto introducido = {frase}")
    for caracter in frase:
        if caracter in vocales:
            contador += 1
            print(f"Vocal encontrada: {caracter}")
    
    print(f"Total de vocales encontradas: {contador}")


texo = input("Introduce un texto: ")
numvocales(texo)