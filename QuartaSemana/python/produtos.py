def cadastrar_produtos():
    produtos = []

    quantidade = int(input("Quantos produtos deseja cadastrar? "))

    for indice in range(quantidade):
        print(f"\nCadastro do produto {indice + 1}")

        nome = input("Nome: ").strip()
        preco = float(input("Preço: R$ "))
        categoria = input("Categoria: ").strip()

        produto = {
            "nome": nome,
            "preco": preco,
            "categoria": categoria
        }

        produtos.append(produto)

    return produtos


def filtrar_por_preco(produtos, valor, criterio):
    if criterio == "acima":
        return [
            produto for produto in produtos
            if produto["preco"] > valor
        ]

    return [
        produto for produto in produtos
        if produto["preco"] < valor
    ]


def ordenar_por_preco(produtos):
    crescente = produtos.copy()
    crescente.sort(key=lambda produto: produto["preco"])

    decrescente = sorted(
        produtos,
        key=lambda produto: produto["preco"],
        reverse=True
    )

    return crescente, decrescente


def obter_categorias_unicas(produtos):
    return set(
        produto["categoria"] for produto in produtos
    )


def calcular_estatisticas(produtos):
    precos = [produto["preco"] for produto in produtos]

    if not precos:
        return None

    menor_preco = min(precos)
    maior_preco = max(precos)
    media_precos = sum(precos) / len(precos)

    return menor_preco, maior_preco, media_precos


def exibir_produtos(titulo, produtos):
    print(f"\n--- {titulo} ---")

    if not produtos:
        print("Nenhum produto encontrado.")
        return

    for produto in produtos:
        print(
            f"Nome: {produto['nome']} | "
            f"Preço: R$ {produto['preco']:.2f} | "
            f"Categoria: {produto['categoria']}"
        )


def gerar_relatorio(produtos):
    exibir_produtos("Todos os produtos", produtos)

    valor = float(
        input("\nInforme o preço para filtragem: R$ ")
    )

    criterio = input(
        "Filtrar produtos acima ou abaixo do valor? "
    ).strip().lower()

    while criterio not in ("acima", "abaixo"):
        criterio = input(
            "Digite 'acima' ou 'abaixo': "
        ).strip().lower()

    filtrados = filtrar_por_preco(
        produtos, valor, criterio
    )

    exibir_produtos(
        f"Produtos com preço {criterio} de R$ {valor:.2f}",
        filtrados
    )

    crescente, decrescente = ordenar_por_preco(produtos)

    exibir_produtos("Ordenação crescente", crescente)
    exibir_produtos("Ordenação decrescente", decrescente)

    categorias = obter_categorias_unicas(produtos)

    print("\n--- Categorias únicas ---")
    print(", ".join(sorted(categorias)) or "Nenhuma categoria.")

    estatisticas = calcular_estatisticas(produtos)

    print("\n--- Estatísticas ---")

    if estatisticas is None:
        print("Não há produtos cadastrados.")
    else:
        menor, maior, media = estatisticas

        print(f"Menor preço: R$ {menor:.2f}")
        print(f"Maior preço: R$ {maior:.2f}")
        print(f"Média dos preços: R$ {media:.2f}")

        print(f"Tupla de estatísticas: {estatisticas}")


def main():
    produtos = cadastrar_produtos()
    gerar_relatorio(produtos)


if __name__ == "__main__":
    main()