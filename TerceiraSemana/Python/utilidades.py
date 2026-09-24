def converter_temperatura(celsius):
    return (celsius * 9 / 5) + 32


def validar_senha(senha):
    return len(senha) >= 8


def caixa(*precos):
    return sum(precos)


def ficha_aluno(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")