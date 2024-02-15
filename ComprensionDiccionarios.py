numeros = [1,2,3,4,5]

diccionario_cuadrados = {num: num **2 for num in numeros}
print(f"Lista original de los numeros = {numeros}\n")
print(f"Diccionario de los numeros con sus cuadrados = {diccionario_cuadrados}\n")
print("*"*85)

numeros2 = [1,2,3,4,5,6,7,8,9,10]
diccionario_num2_pares = {num2: num2%2 ==0 for num2 in numeros2}
print(f"Segunda lista de numeros {numeros2}\n")
print(f"Diccionario de numeros pares en la segunda lista {diccionario_num2_pares}\n")
print("*"*85)

palabras = {"python", "diccionarios", "ejemplos"}
diccionario_longitudes = {pal: len(pal) for pal in palabras}
print(f'Lista de palabras originales = {palabras}\n')
print(f"Diccionario de las palabras y sus longitudes = {diccionario_longitudes}\n")
print("*"*85)