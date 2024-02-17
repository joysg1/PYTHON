def calcular(num1, num2, operacion = 'sumar'):


 def sumar(num1, num2):
    return num1 + num2

 def restar(num1, num2):
     return num1 - num2
 
 def muliplicar(num1, num2):
     return num1 * num2
 
 def dividir(num1, num2):
     return num1 / num2
 
 if operacion == 'sumar':
     print(f"{num1} + {num2} = {sumar(num1,num2)}")
     
 elif operacion == 'restar':
     print(f"{num1} - {num2} = {restar(num1,num2)}") 
     
 elif operacion == 'multiplicar':
     print(f"{num1} * {num2} = {muliplicar(num1,num2)}")   
     
 elif operacion == 'dividir':
     print(f"{num1} / {num2} = {dividir(num1,num2)}") 
 return '*'*40           
 

     

print(calcular(5,8))

print(calcular(5,8,"sumar"))

print(calcular(4,7,"restar"))

print(calcular(4,2,"multiplicar"))

print(calcular(10,2,"dividir"))


