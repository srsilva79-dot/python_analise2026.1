#Desenvolva um código Python que leia 10 médias de alunos e ao momento que está lendo
# mostre se este aluno está aprovado se for maior que 5 ou em recuperação.

for i in range(0,10):
    média= float(input("Digite uma média"))
    if média > 5:
        print("Está aprovado")
    else:
        print("Está em recuperação")
        
    