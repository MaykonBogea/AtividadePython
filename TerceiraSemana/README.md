# 📌 Entregável de Desenvolvimento em Python – Semana 03 (Desafio Sprint 3)

O que deve ser entregue?

Finalização da atividade de modularização e organização de código, aplicando os conceitos de funções, parâmetros, retorno, escopo e criação de módulos. O projeto deve ser entregue em arquivos .py e deve apresentar:

Módulo calculadora.py: Deve conter funções matemáticas básicas (somar, subtrair, multiplicar) e uma função dividir(a, b) que trate explicitamente a divisão por zero (retornando None ou uma mensagem de erro, sem quebrar o programa).

Módulo utilidades.py: Deve conter as funções dos desafios da Prática Independente (Conversor de temperatura, Validador de senha, Caixa com *precos e Ficha do Aluno com **dados).

Script Principal: Um arquivo .py que importe os módulos criados e execute as chamadas das funções, demonstrando o reaproveitamento de código.

Lista Segura: Uma função que adicione um item a uma lista sem alterar a lista original (utilizando cópia defensiva).

Versões em Portugal: Para cada exercício prático, deve ser entregue a versão equivalente em Portugal (comentada), demonstrando a compreensão da lógica independente da sintaxe.

Desafios Bônus (Opcional): Módulo estatistica.py (com media, mediana, moda e alias est), função recursiva fatorialNão e função relatorio(titulo, *linhas, **config).

Certifique-se de que todos os códigos rodam sem erro, utilizam docstrings para documentar as funções e aplicam nomes de variáveis descritivos seguindo a PEP 8 (snake_case).

Objetivo da atividade

A construção desses scripts ajudará a equipe a dominar a modularização de código, compreendendo na prática como dividir um problema complexo em funções menores e reutilizáveis. Além disso, a comparação entre a sintaxe de Portugal e Python reforça a compreensão sobre passagem de parâmetros (por valor vs. por atribuição), mutabilidade de objetos e escopo de variáveis, servindo como base fundamental para a organização de projetos maiores.

💡 Dica: Fiquem atentos aos erros comuns: nunca usem listas ou dicionários como valores padrão em parâmetros (usem None e criem a lista dentro da função); lembrem-se de que funções sem return devolvem None automaticamente; e utilizem o bloco if __name__ == "__main__": para testar os módulos sem que eles sejam executados automaticamente ao serem importados. Revisem os exemplos de *args (tuplas) e **kwargs (dicionários) para os desafios mais complexos.