texto = "Esto es un texto para el ejemplo que vamos a realizar"

# Comprobaciones de inicio y terminacion

print(f"Cadena: {texto}\n")
print("-"*80)
print("Comprobar con que empieza la cadena\n")


print("La cadena empieza con Esto",texto.startswith("Esto"))

print("La cadena empieza con Hola",texto.startswith("Hola"))

print("-"*80)
print("Comprobar con que termina la cadena \n")

print("La cadena termina con realizar:",texto.endswith("realizar"))
print("La cadena termina con len :",texto.endswith("len"))
print("-"*80)

# Se agrega .lower para que compruebe a pesar de haber colocado la palabra con inicio en mayuscula

print("La cadena termina con Realizar: ",texto.lower().endswith("Realizar".lower()))

print("-"*80)

# Alinear texto centrado

print(texto.center(80,'*'))
print(texto.center(80,'/'))

print("-"*80)

longitudCadena = len(texto)

print(longitudCadena)

#Centrar a la longitud de la cadena mas un numero
print(texto.center(longitudCadena+7,'-'))

print("-"*80)

#Alinear a la izquierda y agregar los caracteres (hasta llegar a 80)
print(texto.ljust(80,'-'))

print("-"*80)

#Alinear a la derecha y agregar los caracteres (hasta llegar a 80)
print(texto.rjust(80,'+'))

print("-"*80)

#Eliminar espacios en blanco por delante y detras de la cadena

texto2 = "  hola esta cadena tiene espacio por delante y detras   "

print(f"Cadena con espacio: {texto2}")
print(f"Cadena sin espacios: {texto2.strip()}")

print("-"*80)

#Reemplazar un caracter de una cadena por otro, primero se coloca
#el caracter existente y luego el caracter nuevo

texto3 = "1112 --- Buenas tardes"

print(texto3.replace("-","7"))

print(texto3.replace("1","*"))

print("-"*80)

#Guardar el resultado del reemplazo de un caracter en una cadena

textoModificado = texto3.replace("-","L")
print(textoModificado)

print("-"*80)