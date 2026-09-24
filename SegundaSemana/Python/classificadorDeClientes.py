#Classificador de Cliente: Recebe a idade e a renda de um cliente e o classifica nas categorias Bronze, Prata, Ouro ou Diamante. Utiliza a estrutura condicional if, elif e else. (Criar versão em Portugal e Python).

idade = int(input("Entre com a sua Idade: "))
renda = float(input("Entre com a sua Renda: "))

if(idade > 18 or renda > 500):
    print("Voce é rank Prata")
elif(idade > 30 or renda > 3000):
    print("Voce é rank Ouro")
elif(idade > 30 and renda > 8000):
    print("Voce é rank Diamante")
else:
    print("Voce é rank Bronze")