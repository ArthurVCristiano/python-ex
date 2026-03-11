precoCasa = float(input("Informe o valor da casa: "))
salarioComprador = float(input("Informe o salário do comprador: "))
quantidadeAnosParaPagar = int(input("Informe a quantidade de anos para pagar: "))
valorMensal = precoCasa/(quantidadeAnosParaPagar * 12)

if valorMensal > salarioComprador * 0.30:
    print("Empréstimo negado.")
else:
    valorPrestacao = precoCasa/(quantidadeAnosParaPagar * 12)
    print(("Empréstimo aprovado. O valor da prestação mensal é: R${valorPrestacao:.2f}"))
    