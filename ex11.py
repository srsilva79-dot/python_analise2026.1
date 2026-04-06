#Crie código Python que leia o nome de uam pessoa e o ano de nascimento
#Ao final mostre a seguinte mensgaem "olá fulano você tem X anos"

nome= input("Digite um nome ")
an=int(input("Digite o ano de nascimento => "))
idade=2026-an
print(f"Olá {nome} você tem {idade} anos")