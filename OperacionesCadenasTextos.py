#Convertir a miniscula

cadena = "EjEMPLo de cadenA de TexTo"

print(cadena.lower())

#Convertir a mayuscula

print("-"*80)

cadena2 = "ejemplo de cadena de TexTO"

print(cadena.upper())

print("-"*80)

#Primera letra en mayuscula

print(cadena2.capitalize())

print("-"*80)

#Poner en mayuscula las primeras letras de todas las palabras

print(cadena2.title())

print("-"*80)

#Invertir las mayusculas a minisculas y en sentido contrario

print(cadena.swapcase())
print(cadena2.swapcase())

print("-"*80)

#Determinar si la cadena esta en mayuscula

cadena3 = "HOLA"
print(cadena.isupper())
print(cadena2.isupper())
print(cadena3.isupper())

print("-"*80)

#Determinar si la cadena esta en miniscula

cadena4 = "hola"
print(cadena4.islower())
print(cadena3.islower())
print(cadena2.islower())
print(cadena.islower())

print("-"*80)

#Determinar si la cadena es numerica

cadena5 = '4561'
print(cadena5.isnumeric())
print(cadena.isnumeric())

print("-"*80)

#Determinar si la cadena esta compuesta por letras y numeros

cadena6 = "art67"
print(cadena6.isalnum())

print("-"*80)

#Determinar si es un titulo

cadena7 = "Titulo 1"
print(cadena7.istitle())
print(cadena4.istitle())

print("-"*80)
