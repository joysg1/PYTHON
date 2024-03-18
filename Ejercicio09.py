

def areat(base, altura):
    return (base * altura)/2



base = 0
altura = 0

while base <=0 or altura <=0:
 base = float(input("Ingrese la base del triangulo: "))
 altura = float(input("Ingrese la altura del triangulo: "))
 
 
area = areat(base,altura) 

print(f"--- DATOS INGRESADOS ---")
print(f"BASE = {base} - ALTURA = {altura}")
print("*"*80)
print("\n")
print(f"AREA DEL TRIANGULO = {area}")