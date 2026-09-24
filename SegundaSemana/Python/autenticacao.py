#Sistema de Autenticação: Cria um sistema que solicita uma senha até que o usuário acerte. O sistema deve contar o número de tentativas e bloquear o acesso após 3 erros. Utiliza a estrutura de repetição while. (Criar versão em Portugal e Python).

senha_correta = "1234"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha = input("Introduza a sua senha: ")
    tentativas += 1

    if senha == senha_correta:
        print("Acesso autorizado!")
        break
    else:
        tentativas_restantes = max_tentativas - tentativas

        if tentativas_restantes > 0:
            print(f"Senha incorreta. Tentativas restantes: {tentativas_restantes}")
        else:
            print("Acesso bloqueado.")