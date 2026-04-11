# Desenvolva um código Python que imprima na tela os números
# de 15 a 30 e diga cada um deles se é par ou ímpar

for i in range(15,31):
    r= i % 2
    if r == 0:
        print(f" {i} é par")
    else:
        print(f" {i} é ímpar")