#Conversor de tempo: Recebe um valor em segundos e imprime o equivalente em horas, minutos e segundos.

segundos = int(input("Entre com o valor em segundos: "))


minutos = segundos // 60
segundos = segundos % 60

horas = minutos // 60
minutos = minutos % 60

print(f"Valor em Horas: {horas}")
print(f"Valor em Minutos: {minutos}")
print(f"Valor em Segundos: {segundos}")