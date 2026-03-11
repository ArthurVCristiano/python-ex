numero1 = float(input("Informe o número 1: "))
numero2 = float(input("Informe o número 2: "))
numero3 = float(input("Informe o número 3: "))
auxiliar = 0

if numero1 > numero2 and numero1 > numero3:
    auxiliar = numero1
    if numero2 > numero3:
        print(f"A sequencia é: : {auxiliar} > {numero2} > {numero3}")
    else:
        print(f"A sequencia é: : {auxiliar} > {numero3} > {numero2}")
        
if numero2 > numero1 and numero2 > numero3:
    auxiliar = numero2
    if numero1 > numero3:
        print(f"A sequencia é: : {auxiliar} > {numero1} > {numero3}")
    else:
        print(f"A sequencia é: : {auxiliar} > {numero3} > {numero1}")

if numero3 > numero1 and numero3 > numero2:
    auxiliar = numero3
    if numero1 > numero2:
        print(f"A sequencia é: : {auxiliar} > {numero1} > {numero2}")
    else:
        print(f"A sequencia é: : {auxiliar} > {numero2} > {numero1}")