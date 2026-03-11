#   Aluguel do carro

qtdKmPercorrido = float(input('Digite a quantidade de km percorrido:'))
qtdDias = int(input('Digite a quantidade de dias:'))

priceTot = (qtdKmPercorrido * 0.15) + (qtdDias * 60)

print('O valor total da comrpa é de R$: ', priceTot)