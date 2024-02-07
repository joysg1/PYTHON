print("Bienvenido a mi primer programa")
print("Tipo entero")
print(type(38))
print("Tipo flotante")
print((type(23.43)))
print("Tipo cadena")
print(type("Hola"))
print("Tipo booleano")
print(type(True))

#ejemplos con las cadenas
print("Hola, "+" Amigos")
print("Saludos"*4)
variable = "cadena en variable"
print(variable)
variable = "sumo esto a " + variable
print(variable)

#imprimir la posicion 3 de la cadena
print(variable[3])

#imprimir la posicion 5 de la cadena
print(variable[5])

#imprimir la ultima posicion de la cadena
print(variable[-1])

#imprimir subcadena desde la posicion 2 hasta la 5 (la posicion 5 no se incluye)
print(variable[2:5])

#imprimir longitud de la variable (se cuentan espacios en blanco)
print(len(variable))

#imprimir la cadena en mayuscula
print(variable.upper())

#imprimir la cadena en minuscula
print(variable.lower())

#imprimir la cadena con el primer caracter en mayuscula
print(variable.capitalize())

cadena = "    Esto es una cadena con muchos espacios    "

print(cadena)

#imprimir la cadena sin los espacios por delante y por detras
print(cadena.strip())

#reemplazar valor en cadena
cadena = "Esto es un texto sin reemplazar"
print(cadena)
print(cadena.replace("sin reemplazar", "con reemplazo"))