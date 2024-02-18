# con map convertir cadenas a mayusculas

cadenas = ["Hola", "Amigos", "Programadores"]
mayusculas = list(map(lambda x: x.upper(),cadenas))

print(f"Lista original {cadenas}")
print(f"Lista en mayuscula con map {mayusculas}")

print("-"*80)

# sin map convertir cadenas a mayusculas

mayusculas = []
for cadena in cadenas:
    mayusculas.append(cadena.upper())
print(f"Lista en mayuscula sin map {mayusculas}")    
    