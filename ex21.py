#Desenvolva um código Python que leia o salário de um funcionário.
# Se p salário for maior que 5000, calcule o IRRF que será 7.5% sobre o salário.
# Se for menor que 5000 não paga imposto e se for maior que 8000
# o imposto será 27%. Ao final mostre: o salário bruto
# e o valor do imposto pago e salário final.

s= float(input("Digite seu salário"))
if s <= 5000:
    imposto= 0
elif s <= 8000:
    imposto= s * 0.075
else:
    imposto= s * 0.27
salfinal= s - imposto
print(f"O salário {s}, imposto, - {imposto}, salário bruto {salfinal} ")

