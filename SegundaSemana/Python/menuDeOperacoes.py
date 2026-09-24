#Menu de Operações Matemáticas: Cria um menu com 4 operações matemáticas (ex.: soma, subtração, multiplicação, divisão) e executa a operação escolhida pelo usuário. Utiliza a estrutura match/case no Python. (Criar versão em Portugal e Python).

entrada1 = float("Entre com o primeiro valor: ")
entrada2 = float("Entre com o segundo valor: ")

opcao = int(input("Entre com a operacao escolhida:\n 1- Soma\n 2- Subtração\n 3- Multiplicação\n 4- Divisão\n>> "))

match opcao
    case 1:
        resultado = entrada1 + entrada2
    case 2:
        resultado = entrada1 - entrada2
    case 3:
        resultado = entrada1 * entrada2
    case 4:
        resultado = entrada1 / entrada2
    case _:
        print("Operacao Invalida!")

print(f"Resultado: {resultado}")