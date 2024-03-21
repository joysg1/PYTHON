def CalculoSal(horas, paga_hora, dias):
    result = horas * paga_hora * dias
    return result




horasUsuario = 0

while horasUsuario <=0:

 horasUsuario = int(input("Por favor ingrese las horas trabajadas por dia: "))


pagaHoraUsuario = 0

while pagaHoraUsuario <=0:

 pagaHoraUsuario = float(input("Por favor ingrese la paga por hora: "))


diasUsuario = 0

while diasUsuario <=0:
  diasUsuario = int(input("Por favor ingrese el numero de dias trabajados: "))


print("\n")
print("*"*80)

print("---- RESULTADOS ----\n")
print(f" - Horas trabajadas por dia = {horasUsuario} \n - Paga por hora = {pagaHoraUsuario} \n - Dias Trabajados: {diasUsuario} \n")  
salResult = CalculoSal(horasUsuario, pagaHoraUsuario, diasUsuario)
print(f"El salario es igual a = {salResult}")