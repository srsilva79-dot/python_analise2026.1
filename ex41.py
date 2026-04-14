#Desenvolva um código Python usando while que digite um nome e imprima.
# Só pare o programa se digitar sair______________________ != diferente

nome=""
while nome != "sair":
    nome = input("Digite um nome ")
    if nome == "sair":
        break
    print(f"Olá {nome}")


