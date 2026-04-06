#Desenvolva um código Python que leia 3 notas e calcule a média entre as 3 notas.
#Use input e float
#se a média for maior ou igual a 6
#mostre aprovado
#senão
#mostre recuperação

n1=  float(input("Digite a primeira nota "))
n2= float(input("Digite a segunda nota "))
n3= float(input("Digite a terceira nota "))
med= (n1 + n2 +n3) / 3
print(f"A média das 3 notas é {med} ")
if med >= 6:
    print("APROVADO")
else:
    print("RECURERAÇÃO")


        
    
