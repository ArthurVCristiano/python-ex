numero1 = float(input("Informe o número 1: "))
numero2 = float(input("Informe o número 2: "))
numero3 = float(input("Informe o número 3: "))

auxliarMaior = 0
auxiliarMenor = 0

if numero1 > numero2 and numero1 > 3:
    auxliarMaior = numero1
if numero2 > numero1 and numero2 > numero3:
    auxliarMaior = numero2
if numero3 > numero1 and numero3 > numero2:
    auxliarMaior = numero3

if numero1 < numero2 and numero1 < numero3:
    auxiliarMenor = numero1
if numero2 < numero1 and numero2 < numero3:
    auxiliarMenor = numero2
if numero3 < numero1 and numero3 < numero2:
    auxiliarMenor = numero3

print(f"O maior número é: {auxliarMaior}")
print(f"O menor número é: {auxiliarMenor}")