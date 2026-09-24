#Média de notas: Recebe 3 notas via input(), calcula e imprime a média com 2 casas decimais.

nota1 = float(input("Entre com a Nota 1: "))
nota2 = float(input("Entre com a Nota 2: "))
nota3 = float(input("Entre com a Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A media foi de {media:.2f}")