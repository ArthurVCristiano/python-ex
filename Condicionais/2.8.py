kWhConsumida = float(input("Informe a quantidade de kWh copnsumida: "))
instalacao = input("Informe o tipo de instalação (R (Residencia), C(Comércios), I(Industriais)): ")

if instalacao == "R":
    if kWhConsumida <= 500:
        valorPagar = kWhConsumida * 0.40
        print(f"O valor a pagar é: R${valorPagar:.2f}")
    if kWhConsumida > 500:
        valorPagar = kWhConsumida * 0.65
        print(f"O valor a pagar é: R${valorPagar:.2f}")
        
if instalacao == "C":
    if kWhConsumida <= 1000:
        valorPagar = kWhConsumida * 0.55
        print(f"O valor a pagar é: R${valorPagar:.2f}")
    if kWhConsumida > 1000:
        valorPagar = kWhConsumida * 0.60
        print(f"O valor a pagar é: R${valorPagar:.2f}")
        
if instalacao == "I":
    if kWhConsumida <= 5000:
        valorPagar = kWhConsumida * 0.55
        print(f"O valor a pagar é: R${valorPagar:.2f}")
    if kWhConsumida > 5000:
        valorPagar = kWhConsumida * 0.60
        print(f"O valor a pagar é: R${valorPagar:.2f}")