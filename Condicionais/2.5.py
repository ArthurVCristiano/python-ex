distanciaKM = float(input("Informe a distancia em km que você deseja percorrer: "))

if distanciaKM <= 200:
    valorCorrida = distanciaKM * 0.50
    print(f"O valor da corrida é: R${valorCorrida:.2f}")
    
if distanciaKM > 200:
    valorCorrida = distanciaKM * 0.45
    print(f"O valor da corrida é: R${valorCorrida:.2f}")