numero = float(input("Informe um número: "))
numerosMultiplos = " "

for i in range(101):
    if i % numero == 0:
        numerosMultiplos += " " + str(i)
        
print(f"Os números múltiplos de {numero} entre 0 e 100 são: {numerosMultiplos}")