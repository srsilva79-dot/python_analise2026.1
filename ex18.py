#Desenvolva um código Python que leia a temperatura atual e o programa retorna:
# frio: entre 1 e 18 graus; normal: entre 19 e 24 graus; calor: acima de 24 graus

temp_atual=int(input("Digite a temperatura atual"))
if temp_atual >=1 and temp_atual <= 18:
    print("Frio")
elif temp_atual >18 and temp_atual <= 24:
    print("Normal")
else:
    print("Está calor")




