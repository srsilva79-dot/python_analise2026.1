# Desenvolva um código Python que leia 5 idades e diga se cada um
# é maior de idade, menor de idade ou idoso.

for i in range(0,5):
    idade= int(input("Digite a idade"))
    if idade < 18:
        print("Menor de idade")
    elif idade >= 18 and idade < 65:
        print("Maior de idade")
    else:
        print("Idoso") 