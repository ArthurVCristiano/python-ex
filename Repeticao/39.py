numero = float(input('Digite um número: '))
contadorFatorial = 1
somatorioFormula = '1/'
somaTot =  0 

for i in range(1,(int)(numero + 1)):
    contadorFatorial *= i
    somatorioFormula += f' + 1/{contadorFatorial}'
    somaTot += contadorFatorial

print(somatorioFormula)
print(f'Soma total: 1/{somaTot}')