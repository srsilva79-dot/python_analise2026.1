#Desenvolva um código para o Exército Brasileiro onde irá verificar 
#se o candidato está apto a se alistar ou não.
#Para se alistar deve ser do sexo masculino e maior de idade.

an=float(input("Digite seu ano de nascimento "))
idade= 2026-an
genero=(input("Digite seu gênero, masculino ou feminino "))
if idade >= 18 and genero == "m":
    print("APTO")
else:
    print("NÃO APTO")