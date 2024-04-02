def IMC(estatura,peso):

    r = peso / (estatura * estatura)
    return r



pesoU = 0

while pesoU <=0:
   pesoU = float(input("Por favor ingrese su peso en kilogramos: "))

print("\n")
print("*"*80)

estaturaU = 0

while estaturaU <=0:
 estaturaU = float(input("Por favor ingrese su estatura en metros: "))


 resultU = IMC(estaturaU,pesoU)

 print("\t\t---- RESULTADOS ----\n")
 print(f"Estatura = {estaturaU:.2f} --- Peso = {pesoU:.2f} --- IMC = {resultU:.2f}")

