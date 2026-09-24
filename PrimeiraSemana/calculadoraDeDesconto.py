#Calculadora de desconto: Recebe o preço de um produto e o percentual de desconto, imprime o preço final.

valorProduto = float(input("Entre com o valor atual do Produto: "))
percentualDesconto = float(input("Entre com o percentual de desconto desejado: "))

valorDesconto = valorProduto * (percentualDesconto / 100)
valorFinal = valorProduto - valorDesconto

print(f"O Valor Final: {valorFinal}")