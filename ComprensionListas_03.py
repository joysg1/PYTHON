palabras = ['buenas', 'tardes', 'queridos', 'amigos']
mayuscula = []

for palabra in palabras:
    mayuscula.append(palabra.upper())
print(f"Lista de palabras en formato original {palabras}\n")
print(f"Lista de palabras en mayuscula {mayuscula}\n")


print("*"*40)

print("Usando metodo de comprension de listas \n")

mayuscula = [palabra.upper() for palabra in palabras ]
print(f"Lista de palabras en mayuscula {mayuscula}\n")

    