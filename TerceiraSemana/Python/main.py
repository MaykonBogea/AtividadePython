from calculadora import somar, subtrair, multiplicar, dividir
from utilidades import (
    converter_temperatura,
    validar_senha,
    caixa,
    ficha_aluno
)
from listaSegura import lista_segura


# Calculadora
print("=== CALCULADORA ===")

print("Soma:", somar(10, 5))
print("Subtração:", subtrair(10, 5))
print("Multiplicação:", multiplicar(10, 5))
print("Divisão:", dividir(10, 5))
print("Divisão por zero:", dividir(10, 0))


# Utilidades
print("\n=== UTILIDADES ===")

print("25°C em Fahrenheit:", converter_temperatura(25))

print("Senha válida:", validar_senha("12345678"))

print("Total da caixa:", caixa(10.50, 20.00, 5.75))

print("\n=== FICHA DO ALUNO ===")
ficha_aluno(
    nome="May",
    idade=18,
    curso="ADS",
    nota=10
)

# Lista Segura
lista = [20, 20, 20]
novaLista = lista_segura(lista, 30)