# Función para convertir una lista de strings a mayúsculas usando map()
def lista_a_mayusculas_map(lista):
    """
    Convierte todos los elementos string de una lista a mayúsculas usando map()
    
    Args:
        lista: Lista que puede contener strings y otros tipos de datos
    
    Returns:
        Lista con los strings convertidos a mayúsculas
    """
    def convertir_a_mayuscula(elemento):
        """Función auxiliar para convertir a mayúscula si es string"""
        return elemento.upper() if isinstance(elemento, str) else elemento
    
    return list(map(convertir_a_mayuscula, lista))

# Versión más compacta usando lambda
def lista_a_mayusculas_map_lambda(lista):
    """Versión con map() y lambda"""
    return list(map(lambda x: x.upper() if isinstance(x, str) else x, lista))

# Versión simple si solo hay strings en la lista
def lista_strings_mayusculas_map(lista):
    """Versión simple para listas que solo contienen strings"""
    return list(map(str.upper, lista))

# Función para convertir una lista de strings a mayúsculas (versión original con bucle)
def lista_a_mayusculas_bucle(lista):
    """Versión original con bucle for"""
    resultado = []
    for elemento in lista:
        if isinstance(elemento, str):
            resultado.append(elemento.upper())
        else:
            resultado.append(elemento)
    return resultado

# Alternativa usando list comprehension
def lista_a_mayusculas_comprehension(lista):
    """Versión con list comprehension"""
    return [elemento.upper() if isinstance(elemento, str) else elemento for elemento in lista]

# Ejemplos de uso
if __name__ == "__main__":
    # Ejemplo 1: Lista solo con strings usando map()
    lista1 = ["hola", "mundo", "python", "código"]
    resultado1 = lista_a_mayusculas_map(lista1)
    print("=== Usando map() con función auxiliar ===")
    print(f"Lista original: {lista1}")
    print(f"Lista en mayúsculas: {resultado1}")
    print()
    
    # Ejemplo 2: Lista mixta usando map() con lambda
    lista2 = ["hola", 123, "mundo", 45.6, "python"]
    resultado2 = lista_a_mayusculas_map_lambda(lista2)
    print("=== Usando map() con lambda ===")
    print(f"Lista mixta original: {lista2}")
    print(f"Lista mixta con strings en mayúsculas: {resultado2}")
    print()
    
    # Ejemplo 3: Lista solo strings usando map() simple
    lista3 = ["buenos", "días", "desde", "panamá"]
    resultado3 = lista_strings_mayusculas_map(lista3)
    print("=== Usando map() simple (solo strings) ===")
    print(f"Lista original: {lista3}")
    print(f"Lista en mayúsculas: {resultado3}")
    print()
    
    # Comparación de todas las versiones
    lista4 = ["test", 42, "map", "función"]
    print("=== Comparación de todas las versiones ===")
    print(f"Lista original: {lista4}")
    print(f"Con map() y función: {lista_a_mayusculas_map(lista4)}")
    print(f"Con map() y lambda: {lista_a_mayusculas_map_lambda(lista4)}")
    print(f"Con bucle for: {lista_a_mayusculas_bucle(lista4)}")
    print(f"Con comprehension: {lista_a_mayusculas_comprehension(lista4)}")
    print()
    
    # Ejemplo 4: Lista vacía
    lista5 = []
    resultado5 = lista_a_mayusculas_map(lista5)
    print(f"Lista vacía: {lista5} -> {resultado5}")