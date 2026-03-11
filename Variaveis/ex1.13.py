#OPERA_REAL

valor = float(input('Digite qualquer valor: '))

print(f'Valor original: {valor}')
print(f'Valor inteiro do número: {int(valor)}')
print(f'Valor arredondado  para número inteiro: {round(valor)}')
print(f'Valor arredondado para 1 casas decimal: {round(valor, 1)}')
print(f'Parte fracionaria do número: {valor - int(valor)}')