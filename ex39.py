#Desenvolva um código Python em que o usuário digite um número
#e irá mostrar a tabuada deste número usando while.

v=int(input("Digite um valor => "))
i = 0
while i <= 10:
    m= i * v
    print(f"{v} x {i} = {m}")
    i= i+1