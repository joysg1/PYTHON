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
precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad: "))
importe_total = precio * cantidad
print("El importe total es: ", importe_total)

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

