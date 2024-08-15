# Tipos de datos
# bool int float str

# bool
verdadero = True

entero = 5
decimal = 3.45
cadena = "Hola mundo"

print(type(verdadero))
print(type(entero))
print(type(decimal))
print(type(cadena))

print(verdadero)
print(entero)
print(decimal)
print(cadena)

# Operadores aritmeticos
# + - * / % **
suma = 5 + 3
resta = 5 - 3
multiplicacion = 5 * 3
division = 5 / 3
modulo = 5 % 3
exponente = 5 ** 3
division_entera = 5 // 3

print(suma)
print(resta)
print(multiplicacion)
print(division)
print(modulo)
print(exponente)
print(division_entera)

# Operadores de comparacion
# == != < > <= >=
igual = 5 == 3
no_igual = 5 != 3
menor = 5 < 3
mayor = 5 > 3
menor_igual = 5 <= 3
mayor_igual = 5 >= 3
print(igual)
print(no_igual)
print(menor)
print(mayor)
print(menor_igual)
print(mayor_igual)

# Operadores booleanos
# and or not

print(1==0 and 1!=2)
print(1<2 or 1>9)
print(not 1==4 or 1<5)

# Variables 
nombre = "Juan"
edad = 25
peso = 70.5
casado = False
print(nombre)
print(edad)
print(peso)
print(casado)
print(type(nombre))
print(type(edad))
print(type(peso))
print(type(casado))

# Escribe un programa que solicite precio y cantidad y calcule el importe total
""" precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad: "))
importe_total = precio * cantidad
print("El importe total es: ", importe_total) """

# Concatenar cadenas
nombre = "Juan"
edad = 25
print("Mi nombre es " + nombre + " y tengo " + str(edad) + " años.")

# Longitud de una cadena
cadena = "Hola mundo"
print(len(cadena))

# Rebanar cadenas
cadena = "Hola mundo"
print(cadena)
print(cadena[1:4])

# Genera un codigo que solicite el nombre y la edad
""" nombre = input("Ingrese su nombre: ").strip()
edad = int(input("Ingrese su edad: "))
print("Su nombre es " + nombre + " y su edad es " + str(edad) + " años.") """


# Genera un codigo que solicite un numero y si es 15 indique que ha acertado


""" numero = int(input("Ingrese un numero: "))
if numero == 15:
    print("Ha acertado")
elif numero > 15:
    print("El numero es mayor")
elif numero < 15:
    print("El numero es menor")
else:
    print("No ha acertado") 
    print("Intenta nuevamente")
 """

# Bucles

# Genera un codigo que imprima los numeros del 10 al 50 con saltos de 5 en 5
""" for i in range(10, 51,5):
  print(f"Numero: ", i) """

# Genea un codigo que recorra los elementos de una cadena
""" cadena = "Hola mundo"
for caracter in cadena:
  print(caracter)
 """

# Genera un codigo que pida al usuario su nombre hasta que se deje en blanco
""" nombre = input("Ingrese su nombre: ")
while nombre != "":
  print("Hola: " + nombre)
  nombre = input("Ingrese su nombre: ")
  if nombre == "":
    print("Gracias por utilizar el programa")
    break
   """

# Funciones

""" def sum(num1, num2):
  resultado = num1 + num2
  return resultado


result = sum(2,2)
print(result) """

# Listas y diccionarios
""" lista = []
print(lista)
lista = [1,2,3,4]
print(lista)
lista.append(5)
print(lista)
lista.pop()
print(lista)
lista.remove(2)
print(lista) """


# Genera un codigo para crear un diccionario 
diccionario = {}
diccionario["nombre"] = "Juan"
diccionario["edad"] = 25
diccionario["peso"] = 70.5
diccionario["casado"] = False
print(diccionario)

# Genera un codigo para generar un diccionario de los meses
meses = {}
meses["Enero"] = 1
meses["Febrero"] = 2
meses["Marzo"] = 3
meses["Abril"] = 4
meses["Mayo"] = 5
meses["Junio"] = 6
meses["Julio"] = 7
meses["Agosto"] = 8
meses["Septiembre"] = 9
meses["Octubre"] = 10
meses["Noviembre"] = 11
meses["Diciembre"] = 12

del meses["Diciembre"]
print(meses)
meses["Diciembre"] = 12
print(meses)

for clave, valor in meses.items():
  print(f"{clave} - {valor}")










    










