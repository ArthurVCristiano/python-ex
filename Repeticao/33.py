numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
auxiliar = 0
contador = 0
resto = 0

while numero1 > 0:
    contador += 1
    numero1 -= numero2
    
    if numero1 == 0:
        resto = 0
        break

print(f"O resultado da divisão é: {contador} e o resto é: {resto}")