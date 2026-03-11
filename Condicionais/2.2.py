velocidade = float(input("Qual a velocidade voce estava?"))

if velocidade > 80:
    print("Voce foi multado por excesso de velocidade")
    diferenca = velocidade - 80
    multa = diferenca * 30
    print(f"Voce deve pagar uma multa de R${multa:.2f}")
else:
    print("Voce estava dentro do limite de velocidade")