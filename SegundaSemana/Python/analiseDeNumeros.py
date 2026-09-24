#Análise de Números: Lê 5 números via input() e calcula a soma, a média, o maior e o menor valor. Utiliza a estrutura de repetição for. (Criar versão em Portugal e Python).

soma = 0

for i in range(5):
    numero = float(input(f"Introduza o {i + 1}º número: "))
    
    soma += numero

    if i == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

media = soma / 5

print(f"\nSoma: {soma}")
print(f"Média: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")