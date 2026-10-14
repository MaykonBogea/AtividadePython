# Sprint 5 — Sistema de Análise de Dados

Projeto em Python que lê um arquivo CSV, valida os campos com expressões regulares, trata exceções e gera um relatório em texto.

## 1. Requisitos

- Python 3.10 ou superior (não requer bibliotecas externas).
- Arquivos `analise_dados.py` e `dados.csv` na mesma pasta.

## 2. Como executar

No terminal, dentro da pasta do projeto:

```bash
python analise_dados.py
```

O programa lê `dados.csv`, exibe o relatório no terminal e grava uma cópia em `relatorio.txt`.

## 3. Formato do arquivo de entrada

O CSV deve usar cabeçalho e conter as colunas obrigatórias:

```csv
nome,email,cpf,telefone,data
Ana Silva,ana.silva@example.com,123.456.789-00,(11) 91234-5678,15/05/2024
Bruno Costa,bruno.costa@example.com,987.654.321-00,11987654321,31/02/2023
```

A data deve estar no formato `DD/MM/AAAA`. O arquivo de exemplo inclui registros válidos e inválidos para demonstrar o relatório.

## 4. Justificativa das validações

| Campo | Regra aplicada |
|---|---|
| Nome | Não pode estar vazio. |
| E-mail | Verifica uma estrutura básica de usuário, `@` e domínio com ponto. |
| CPF | Verifica o formato `000.000.000-00`. |
| Telefone | Aceita formatos comuns com DDD e, opcionalmente, o código `+55`. |
| Data | Verifica o formato `DD/MM/AAAA`, a existência da data no calendário e impede datas futuras. |

Os padrões são compilados com `re.compile()` e usam `fullmatch()` para exigir que o valor inteiro corresponda ao padrão. `\d` representa dígitos, `\w` caracteres de palavra e os pontos e hífens literais são usados para representar a pontuação esperada.

**Limitação importante:** a validação do CPF verifica apenas o formato, não calcula os dígitos verificadores. A validação de e-mail também é estrutural e não confirma que o endereço existe.

## 5. Exceções tratadas

- `FileNotFoundError`: o CSV não foi encontrado.
- `ValueError`: o arquivo está vazio ou uma data não representa um dia válido; a data inválida é convertida em `FormatoInvalidoError`.
- `KeyError`: uma ou mais colunas obrigatórias não estão presentes.
- `csv.Error`: falha na leitura ou interpretação do CSV.
- `FormatoInvalidoError`: exceção personalizada para campos vazios, formatos incorretos, datas inexistentes ou datas futuras.

A leitura e a escrita usam `with open(..., encoding="utf-8")`, que fecha os arquivos automaticamente. O bloco `finally` anuncia o fim da tentativa de leitura, mesmo quando ocorre uma das exceções tratadas.

## 6. Exemplo de saída

Com o `dados.csv` fornecido, o relatório terá a seguinte estrutura (a quantidade exata depende dos dados):

```text
RELATÓRIO DE ANÁLISE DE DADOS
================================
Total de registros: 4
Registros válidos: 2
Registros inválidos: 2

REGISTROS VÁLIDOS
--------------------------------
...

REGISTROS INVÁLIDOS
--------------------------------
...
```

O relatório completo é escrito em `relatorio.txt`. Cada registro inválido inclui a linha do CSV e os motivos da reprovação.

## 7. Estrutura do repositório

```text
sprint-05-analise-dados/
├── analise_dados.py
├── dados.csv
├── README.md
└── relatorio.txt  # gerado ao executar o programa
```

## 8. Publicação no GitHub

1. Crie um repositório chamado `sprint-05-analise-dados`.
2. Adicione `analise_dados.py`, `dados.csv` e `README.md`.
3. Faça o primeiro commit e envie os arquivos ao GitHub.
4. Deixe o repositório público, caso a atividade exija acesso sem autenticação.

Exemplo de comandos Git:

```bash
git init
git add analise_dados.py dados.csv README.md
git commit -m "Entrega Sprint 5: análise e validação de dados"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/sprint-05-analise-dados.git
git push -u origin main
```
