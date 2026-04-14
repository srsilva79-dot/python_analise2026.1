# Desenvolva um código Python que leia 3 valores e 
# ao final mostre qual é o maior entre os 3.

i=0
maior=0
while i < 3:
    v=int(input("Diigte um valor"))
    if v > maior:
        maior = v
    i=i+1
print(f"{maior}")
