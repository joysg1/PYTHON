class Persona:
    contador = 0  #Variable de clase
    def __init__(self, nombre): #Constructor
        self.nombre = nombre 
        Persona.contador = Persona.contador +1  #Incremento al crear objeto o instancia de clase

# Instancias de las clase Persona

persona1 = Persona("Juan")
persona2 = Persona("Maria")
persona3 = Persona("Luisa")

# Acceder al contador de la clase Persona

print(f"Cantidad de personas: {Persona.contador}")
print("\n")
print("*"*80)

# La variable contador es una variable comun a todas las instancias