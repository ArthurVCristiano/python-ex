depositoInicial = float(input("Informe o valor do depósito inicial:"))
taxaJuros = float(input("Informe a taxa de juros mensal: "))

for i in range(24):
    depositoInicial += depositoInicial * (taxaJuros / 100)
    print(f"O valor do depósito após {i+1} meses é: {depositoInicial:.2f}")

print(f"O valor do depósito após 24 meses é: {depositoInicial:.2f}")