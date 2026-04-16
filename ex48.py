# Crie uma função que receba dois números e retorne o maior deles

def numeros(a, b):
    if a > b:
        return a
    else: 
        return b
resultado = numeros(11, 10)
print(f"O maior número é {resultado} ")