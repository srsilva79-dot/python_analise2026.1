# Desenvolva um código que o usuário digite
# 5 valores e após digitar, informe se o valor é par ou ímpar

for i in range(0,5):
    x=int(input("Digite um valor => "))
    r= x % 2
    if r % 2 == 0:
        input(f"o valor {x} é par")
    else: 
        input(f"o valor {x} é ímpar")
