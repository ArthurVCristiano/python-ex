n1 = float(input("Informe o número 1: "))
n2 = float(input("Informe o número 2: "))
n3 = float(input("Informe o número 3: "))
n4 = float(input("Informe o número 4 fora da ordem: "))

if n4 > n3:
    print(f"A ordem crescente é: {n1} < {n2} < {n3} < {n4}")
if n4 < n3:
    print(f"A ordem crescente é: {n1} < {n2} < {n4} < {n3}")
if n4 < n2:
    print(f"A ordem crescente é: {n1} < {n4} < {n2} < {n3}")
if n4 < n1:
    print(f"A ordem crescente é: {n4} < {n1} < {n2} < {n3}")