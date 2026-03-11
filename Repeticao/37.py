codigo = int(input('Digite uma opção [1][2][3][5][9]: '))
quantidadeComprada = int(input('Digite a quantidade comprada: '))
totalCompra = 0
continuar = "S"

while continuar == "S":
    
    if codigo == 1:
        totalCompra += quantidadeComprada * 0.50
        
    if codigo == 2:
        totalCompra += quantidadeComprada * 1.00
        
    if codigo == 3:
        totalCompra += quantidadeComprada * 4.00
        
    if codigo == 5:
        totalCompra += quantidadeComprada * 7.00
        
    if codigo == 9:
        totalCompra += quantidadeComprada * 8.00
        
    if codigo != 1 and codigo != 2 and codigo != 3 and codigo != 5 and codigo != 9:
        print('Código inválido.')
    if codigo == 0:
        
        print("Compra realizada com sucesso.")
        break
    print('Deseja continuar? [S/N]: ')
    continuar = input().upper()
    
    if continuar == "S":
        print('Digite o código do produto: ')
        codigo = int(input())
        
        print('Digite a quantidade comprada: ')
        quantidadeComprada = int(input())
        
    if continuar == "N":
        print("Compra realizada com sucesso.")
        break
    
print(f'O total da compra é: R${totalCompra:.2f}')