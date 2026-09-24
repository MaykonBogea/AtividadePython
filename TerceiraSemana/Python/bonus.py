def media(valores):
    if not valores:
        return None

    return sum(valores) / len(valores)


def mediana(valores):
    if not valores:
        return None

    valores = sorted(valores)
    tamanho = len(valores)
    meio = tamanho // 2

    if tamanho % 2 == 0:
        return (valores[meio - 1] + valores[meio]) / 2

    return valores[meio]


def moda(valores):
    if not valores:
        return None

    frequencias = {}

    for valor in valores:
        frequencias[valor] = frequencias.get(valor, 0) + 1

    maior_frequencia = max(frequencias.values())

    for valor, frequencia in frequencias.items():
        if frequencia == maior_frequencia:
            return valor

def fatorial(n):
    if n < 0:
        raise ValueError("O fatorial não existe para números negativos.")

    if n == 0 or n == 1:
        return 1

    return n * fatorial(n - 1)

def relatorio(titulo, *linhas, **config):
    separador = config.get("separador", "=")
    largura = config.get("largura", 40)

    print(separador * largura)
    print(titulo.center(largura))
    print(separador * largura)

    for linha in linhas:
        print(linha)

    print(separador * largura)