continuar = "sim"
precoHoraAula = 146
horaAula = 0
mediaSalarioBrutoA = 0
salarioBrutoA = 0
mediaSalarioBrutoB = 0
salarioBrutoB = 0
mediaSalarioLiquidoA = 0
salarioLiquidoA = 0
mediaSalarioLiquidoB = 0
salarioLiquidoB = 0
contadorA = 0
contadorB = 0

while continuar == "sim":
    classe = input("Informe a classe: [A/B] ").upper()
    if classe == "A":
        contadorA += 1
        horaAula = (float(input("Informe a quantidade de horas aula: ")))
        salarioBrutoA += horaAula * precoHoraAula
        salarioLiquidoA += salarioBrutoA - (salarioBrutoA * 0.10)       
    elif classe == "B":
        contadorB += 1
        horaAula = (float(input("Informe a quantidade de horas aula: ")))
        salarioBrutoB += horaAula * precoHoraAula
        salarioLiquidoB += salarioBrutoB - (salarioBrutoB * 0.05)
    
    continuar = input("Deseja continuar? Digite sim para sim: ").lower()
    if continuar != "sim":
        print("Fim de cadastro.")


mediaSalarioBrutoA = salarioBrutoA / contadorA
mediaSalarioBrutoB = salarioBrutoB / contadorB
mediaSalarioLiquidoA = salarioLiquidoA / contadorA
mediaSalarioLiquidoB = salarioLiquidoB / contadorB

print(f"A média do salário bruto dos professores da classe A é: R${mediaSalarioBrutoA:.2f}")
print(f"A média do salário bruto dos professores da classe B é: R${mediaSalarioBrutoB:.2f}")
print(f"A média do salário líquido dos professores da classe A é: R${mediaSalarioLiquidoA:.2f}")
print(f"A média do salário líquido dos professores da classe B é: R${mediaSalarioLiquidoB:.2f}")
