# Programa que reciba un caracter y devuelva el valor ASCII del mismo
def get_ascii_char(char):
  """
  Returns the ASCII value of a given character.
  """
  return ord(char)


caracter = input("Introduce un caracter: ")
valor_ascii = get_ascii_char(caracter)
print(f"El valor ASCII de '{caracter}' es {valor_ascii}")