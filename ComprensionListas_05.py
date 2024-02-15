frase = "Python es un lenguaje de programacion"
frase_02 = "Ahora me encuentro aprendiendolo"

vocales = []
vocales2 = []

vocales = [letra for letra in frase if letra in 'aeiouAEIOU']

print(f"Primera frase: {frase}")
print(f"Vocales en la primera frase {vocales}")


vocales2 = [letra for letra in frase_02 if letra in 'aeiouAEIOU']

print("*"*88)

print(f"Segunda frase: {frase_02}")
print(f"Vocales en la segunda frase {vocales2}")