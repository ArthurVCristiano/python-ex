numero1 = float(input("Informe o número 1: "))
numero2 = float(input("Informe o número 2: "))

escolha = input("Escolha a operação: +, -, *, /: ")

if escolha == '+':
    print(f"Resultado: {numero1 + numero2}")
if escolha == '-':
    if numero1>numero2:
        print(f"Resultado: {numero1 - numero2}")
    else:
        print(f'Resultado: {numero2 - numero1}')
if escolha == '*':
    print(f"Resultado: {numero1 * numero2}")
if escolha == '/': 
    if numero2 != 0:
        print(f"Resultado: {numero1 / numero2}")
    else:
        print("Não é possível dividir por zero")