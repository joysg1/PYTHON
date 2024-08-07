import string 
import random

caracteres = list(string.ascii_letters + string.digits + string.punctuation)
#print(caracteres)


def dameClave():
    longitud = int (input (("Ingrese la longitud deseada de la clave: ")))
    random.shuffle(caracteres)
    clave = []
    for i in range(longitud):
        clave.append(random.choice(caracteres))
    random.shuffle(clave)
    return "".join(clave)


if __name__ == "__main__":
    clave = dameClave()
    print(f"La clave generada es: {clave}")