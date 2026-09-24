#Calculadora de troco: Recebe o valor da compra e o valor pago, calcula e imprime o troco.


valorCompra = float(input("Entre com o valor da Compra: "))
valorPago =  float(input("Entre com o valor Pago: "))

valorTroco = valorPago - valorCompra
print(f"Troco: {valorTroco}")