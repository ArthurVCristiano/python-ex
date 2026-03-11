numero = float(input("Informe um número: "))

for i in range(2,(int)(numero) + 1):
    if numero % i == 0 :
        if i == numero:
            print(f"O número {numero} é primo.")
        else:            
            print(f"O número {numero} não é primo. é divisivel por {i}.")
            break
        