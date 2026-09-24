#Par ou ímpar: Recebe um número inteiro e informa se ele é par ou ímpar (utilizando o operador de módulo %).

numero = int(input("Entre com um numero: "))
if(numero % 2 == 0):
    print("O numero é par")
else:
    print("O numero é impar")