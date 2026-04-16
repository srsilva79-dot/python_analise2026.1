# Crie uma função que receba o lado de um quadrado e retorne o valor de sua área
# (A = lado^2)
# A = l ** 2

def calcular_area_quadrado(lado):
    area = lado ** 2
    return area
lado_do_quadrado = 8
resultado = calcular_area_quadrado(lado_do_quadrado)
print(f"A área de um quadrado com lado {lado_do_quadrado} é: {resultado}")

def quadrado(lado):
    #usando o operador de exponenciação (**)
    return lado ** 2
    
# Interação com o usuário
medida_Lado = float(input("Digite a medida do lado do quadradao"))

# Chamada da funão e exibição dos resultados
area = quadrado(medida_lado)
print(f"A área do quadrado é: {area} ")

   
