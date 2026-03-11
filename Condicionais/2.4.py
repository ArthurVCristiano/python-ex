#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários
#superiores a $ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, calcule um aumento de 15%.

salario = float(input("Informe seu salario: "))

if salario > 1250:
    aumento = salario * 0.10
    novoSalario = salario + aumento
    print(f"Seu novo salário é: R${novoSalario:.2f}")
if salario <= 1250:
    aumento = salario * 0.15
    novoSalario = salario + aumento
    print(f"Seu novo salário é: R${novoSalario:.2f}")

