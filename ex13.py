#Desevolva um código Python onde o usuário digite seu gênero,
#M para masculino e F para feminino. Se o gênero for M irá imprimir Masculino,
#senão irá imprimir Feminino

g=input("Digite m para masculino ou f para feminino ")
if g == "m":
    print("masculino")
else:
    print("feminino")


#Usando mais de uma condição (elif)
g=input("Digite m para masculino ou f para feminino ")
if g == "m" or g == "M":
    print("Masculino")
elif g =="f" or g == "F":
    print("Feminino")
else:
    print("genero inválido")
    

    
    
