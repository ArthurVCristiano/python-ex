numero = float(input('Informe um número ( Digite 0 para encerrar): '))
numerosDigitados = " "
somaNumeros = 0
media = 0
contador = 0

while numero != 0:
    contador += 1 
    numerosDigitados += " " + str(numero)
    somaNumeros += numero
    
    numero = float(input('Informe um número ( Digite 0 para encerrar): '))

media = somaNumeros / contador
print(numerosDigitados)
print(f"A média é: {media:.2f}")
print(f"A soma é: {somaNumeros}")