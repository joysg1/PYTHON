palabra = input("Ingrese una palabra: ")
palabra2 = palabra[::-1]


if palabra ==palabra2:
    print("La palabra es un palindromo")
    print(f"{palabra} = {palabra2}")
else:
    print("La palabra no es un palindromo")
    print(f"{palabra} != {palabra2}")
    

    