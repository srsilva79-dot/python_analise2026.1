# Desenvolva um código Python que envia um valor para uma função
# e que essa verifique se o número é ímpar ou par

def par(a):
    if a % 2 == 0:
        return "PAR"
    else:
        return "ÍMPAR."

v=int(input("Digite um valor"))
y = par(v)
print(y)
