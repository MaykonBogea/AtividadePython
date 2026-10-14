import csv
import re
from datetime import datetime, date
from pathlib import Path


ARQUIVO_ENTRADA = Path("dados.csv")
ARQUIVO_RELATORIO = Path("relatorio.txt")

CAMPOS_OBRIGATORIOS = {"nome", "email", "cpf", "telefone", "data"}

PADROES = {
    "email": re.compile(r"^[\w.+-]+@[\w-]+(?:\.[\w-]+)+$", re.IGNORECASE),
    "cpf": re.compile(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"),
    "telefone": re.compile(
        r"^(?:\+55\s?)?(?:\(?\d{2}\)?\s?)?9?\d{4}-?\d{4}$"
    ),
    "data": re.compile(r"^\d{2}/\d{2}/\d{4}$"),
}


class FormatoInvalidoError(Exception):
    """Indica que um campo não atende às regras de formato do projeto."""


def validar_campo(campo, valor):
    """Valida o formato do campo e, no caso da data, sua validade no calendário."""
    valor = (valor or "").strip()

    if not valor:
        raise FormatoInvalidoError("campo vazio")

    if campo not in PADROES:
        return True

    if not PADROES[campo].fullmatch(valor):
        raise FormatoInvalidoError("formato inválido")

    if campo == "data":
        try:
            data_convertida = datetime.strptime(valor, "%d/%m/%Y").date()
        except ValueError as erro:
            raise FormatoInvalidoError("data inexistente no calendário") from erro

        if data_convertida > date.today():
            raise FormatoInvalidoError("a data não pode estar no futuro")

    return True


def validar_registro(registro, numero_linha):
    erros = []

    for campo in ("nome", "email", "cpf", "telefone", "data"):
        valor = registro.get(campo, "")

        if campo == "nome":
            if not valor.strip():
                erros.append(f"{campo}: campo vazio")
            continue

        try:
            validar_campo(campo, valor)
        except FormatoInvalidoError as erro:
            erros.append(f"{campo}: {erro}")

    return {
        "linha": numero_linha,
        "registro": registro,
        "valido": not erros,
        "erros": erros,
    }


def ler_e_validar_csv(caminho):
    resultados = []

    try:
        with open(caminho, mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            if leitor.fieldnames is None:
                raise ValueError("O arquivo CSV está vazio ou não possui cabeçalho.")

            campos_presentes = set(leitor.fieldnames)
            campos_ausentes = CAMPOS_OBRIGATORIOS - campos_presentes

            if campos_ausentes:
                # KeyError representa a ausência de uma coluna obrigatória.
                raise KeyError(", ".join(sorted(campos_ausentes)))

            for numero_linha, registro in enumerate(leitor, start=2):
                resultados.append(validar_registro(registro, numero_linha))

    except FileNotFoundError:
        print(f"Erro: arquivo não encontrado: {caminho}")
        return None
    except ValueError as erro:
        print(f"Erro nos dados do arquivo: {erro}")
        return None
    except KeyError as erro:
        print(f"Erro: coluna obrigatória ausente no CSV: {erro}")
        return None
    except csv.Error as erro:
        print(f"Erro ao interpretar o CSV: {erro}")
        return None
    else:
        return resultados
    finally:
        print("Leitura do arquivo finalizada.")


def gerar_relatorio(resultados, caminho_saida):
    total = len(resultados)
    validos = [item for item in resultados if item["valido"]]
    invalidos = [item for item in resultados if not item["valido"]]

    linhas = [
        "RELATÓRIO DE ANÁLISE DE DADOS",
        "=" * 32,
        f"Total de registros: {total}",
        f"Registros válidos: {len(validos)}",
        f"Registros inválidos: {len(invalidos)}",
        "",
        "REGISTROS VÁLIDOS",
        "-" * 32,
    ]

    if validos:
        for item in validos:
            registro = item["registro"]
            linhas.append(
                f"Linha {item['linha']}: {registro['nome']} | "
                f"{registro['email']} | CPF: {registro['cpf']} | "
                f"Telefone: {registro['telefone']} | Data: {registro['data']}"
            )
    else:
        linhas.append("Nenhum registro válido.")

    linhas.extend(["", "REGISTROS INVÁLIDOS", "-" * 32])

    if invalidos:
        for item in invalidos:
            registro = item["registro"]
            identificacao = registro.get("nome", "").strip() or "(sem nome)"
            linhas.append(f"Linha {item['linha']}: {identificacao}")
            for erro in item["erros"]:
                linhas.append(f"  - {erro}")
    else:
        linhas.append("Nenhum registro inválido.")

    conteudo = "\n".join(linhas) + "\n"

    with open(caminho_saida, mode="w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

    print("\n" + conteudo)
    print(f"Relatório salvo em: {caminho_saida}")


def main():
    resultados = ler_e_validar_csv(ARQUIVO_ENTRADA)

    if resultados is None:
        return

    gerar_relatorio(resultados, ARQUIVO_RELATORIO)


if __name__ == "__main__":
    main()
