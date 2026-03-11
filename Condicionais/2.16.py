print('Menu de Opções:')
print('1 - Imposto')
print('2 - Novo salário')
print('3 - Classificação')

opcao = int(input('Informe a opção desejada: '))
salario = float(input('Informe o salário: '))

if opcao == 1:
    if salario < 500:
        imposto = 500 * 0.05
        print(f'Valor do imposto: R${imposto}')
    if salario >= 500 and salario <= 850:
        imposto = 500 * 0.10
        print(f'Valor do imposto: R${imposto}')
    if salario > 850:
        imposto = 500 * 0.15
        print(f'Valor do imposto: R${imposto}')
        
if opcao == 2:
    if salario > 1500:
        salario = salario + 25
        print(f'Novo salário: R${salario}')
    if salario >= 750 and salario <= 1500:
        salario = salario + 50
        print(f'Novo salário: R${salario}')
    if salario >= 450 and salario < 750:
        salario = salario + 75
        print(f'Novo salário: R${salario}')
    if salario < 450:
        salario = salario + 100
        print(f'Novo salário: R${salario}')
        
if opcao == 3:
    if salario >= 700:
        print('Bem remunerado')
    if salario < 700:
        print('Mal remunerado')