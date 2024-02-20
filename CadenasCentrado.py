texto = "Esto es un texto para el ejemplo que vamos a realizar"
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