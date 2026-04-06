#Desenvolva um código Pyhon que leia um valor e dê um desconto
# de acordo com a tabela de valores abaixo:
# >500- 20%; 100 a 499- 15%; <100- 5%

valor=float(input("Digite um valor "))
if valor < 100:
    p= valor * 0.05
    d= valor - p
elif valor < 499:
    p= valor * 0.15
    d= valor - p
else: 
    p= valor * 0.2
    d= valor - p
print(f"O valor de {valor} com desconto de {p} ficará em {d}")