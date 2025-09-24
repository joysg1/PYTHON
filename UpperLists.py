# Función para convertir una lista de strings a mayúsculas
def lista_a_mayusculas(lista):
    """
    Convierte todos los elementos string de una lista a mayúsculas
    
    Args:
        lista: Lista que puede contener strings y otros tipos de datos
    
    Returns:
        Lista con los strings convertidos a mayúsculas
    """
    resultado = []
    for elemento in lista:
        if isinstance(elemento, str):
            resultado.append(elemento.upper())
        else:
            resultado.append(elemento)  # Mantiene elementos que no son strings
    return resultado

# Alternativa usando list comprehension (más pythónica)
def lista_a_mayusculas_v2(lista):
    """Versión con list comprehension"""
    return [elemento.upper() if isinstance(elemento, str) else elemento for elemento in lista]

# Ejemplos de uso
if __name__ == "__main__":
    # Ejemplo 1: Lista solo con strings
    lista1 = ["hola", "mundo", "python", "código"]
    resultado1 = lista_a_mayusculas(lista1)
    print(f"Lista original: {lista1}")
    print(f"Lista en mayúsculas: {resultado1}")
    print()
    
    # Ejemplo 2: Lista mixta (strings y otros tipos)
    lista2 = ["hola", 123, "mundo", 45.6, "python"]
    resultado2 = lista_a_mayusculas(lista2)
    print(f"Lista mixta original: {lista2}")
    print(f"Lista mixta con strings en mayúsculas: {resultado2}")
    print()
    
    # Ejemplo 3: Usando la versión con list comprehension
    lista3 = ["buenos", "días", "desde", "panamá"]
    resultado3 = lista_a_mayusculas_v2(lista3)
    print(f"Con list comprehension: {lista3} -> {resultado3}")
    print()
    
    # Ejemplo 4: Lista vacía
    lista4 = []
    resultado4 = lista_a_mayusculas(lista4)
    print(f"Lista vacía: {lista4} -> {resultado4}")