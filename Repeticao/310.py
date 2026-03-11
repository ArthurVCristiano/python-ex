continuar = input("Deseja começar Operacao? [S/N]: ").upper()
numeroVeiculosCidade1 = 0
numeroVeiculosCidade2 = 0
numeroVeiculosCidade3 = 0
numeroVeiculosCidade4 = 0
numeroVeiculosCidade5 = 0
numeroAcidentesCidade1 = 0
numeroAcidentesCidade2 = 0
numeroAcidentesCidade3 = 0
numeroAcidentesCidade4 = 0
numeroAcidentesCidade5 = 0

while continuar == "S":
    
    codigoCidade = int(input("Digite o código da cidade [1][2][3][4][5]: "))
    if codigoCidade == 1:
        print("Cidade 1 - Ibirama")
        numeroVeiculosCidade1 = int(input("Digite o número de veículos de passeio: "))
        numeroAcidentesCidade1 = int(input("Digite o número de acidentes de trânsito com vítimas: "))
    elif codigoCidade == 2:
        
        print("Cidade 2 - Palhoça")
        numeroVeiculosCidade2 = int(input("Digite o número de veículos de passeio: "))
        numeroAcidentesCidade2 = int(input("Digite o número de acidentes de trânsito com vítimas: "))
    elif codigoCidade == 3:
        
        print("Cidade 3 - Blumenau")
        numeroVeiculosCidade3   = int(input("Digite o número de veículos de passeio: "))
        numeroAcidentesCidade3 = int(input("Digite o número de acidentes de trânsito com vítimas: "))
    elif codigoCidade == 4:
        
        print("Cidade 4 - Joinville")
        numeroVeiculosCidade4 = int(input("Digite o número de veículos de passeio: "))
        numeroAcidentesCidade4 = int(input("Digite o número de acidentes de trânsito com vítimas: "))
    elif codigoCidade == 5:
        
        print("Cidade 5 - Florianópolis")
        numeroVeiculosCidade5 = int(input("Digite o número de veículos de passeio: "))
        numeroAcidentesCidade5 = int(input("Digite o número de acidentes de trânsito com vítimas: "))    

    print('Deseja continuar? [S/N]: ')
    continuar = input().upper()
        
    if continuar == "N":
        print("Programa encerrado.")
        break

mediaVeiculosGeral = (numeroVeiculosCidade1 + numeroVeiculosCidade2 + numeroVeiculosCidade3 + numeroVeiculosCidade4 + numeroVeiculosCidade5) / 5
mediaAcidentesGeral = (numeroAcidentesCidade1 + numeroAcidentesCidade2 + numeroAcidentesCidade3 + numeroAcidentesCidade4 + numeroAcidentesCidade5) / 5

if numeroVeiculosCidade1 > numeroVeiculosCidade2 and numeroVeiculosCidade1 > numeroVeiculosCidade3 and numeroVeiculosCidade1 > numeroVeiculosCidade4 and numeroVeiculosCidade1 > numeroVeiculosCidade5:
    print("A cidade com maior número de veículos é: Ibirama.")
elif numeroVeiculosCidade2 > numeroVeiculosCidade1 and numeroVeiculosCidade2 > numeroVeiculosCidade3 and numeroVeiculosCidade2 > numeroVeiculosCidade4 and numeroVeiculosCidade2 > numeroVeiculosCidade5:
    print("A cidade com maior número de veículos é: Palhoça.")
elif numeroVeiculosCidade3 > numeroVeiculosCidade1 and numeroVeiculosCidade3 > numeroVeiculosCidade2 and numeroVeiculosCidade3 > numeroVeiculosCidade4 and numeroVeiculosCidade3 > numeroVeiculosCidade5:
    print("A cidade com maior número de veículos é: Blumenau.")
elif numeroVeiculosCidade4 > numeroVeiculosCidade1 and numeroVeiculosCidade4 > numeroVeiculosCidade2 and numeroVeiculosCidade4 > numeroVeiculosCidade3 and numeroVeiculosCidade4 > numeroVeiculosCidade5:
    print("A cidade com maior número de veículos é: Joinville.")
elif numeroVeiculosCidade5 > numeroVeiculosCidade1 and numeroVeiculosCidade5 > numeroVeiculosCidade2 and numeroVeiculosCidade5 > numeroVeiculosCidade3 and numeroVeiculosCidade5 > numeroVeiculosCidade4:
    print("A cidade com maior número de veículos é: Florianópolis.")
    
if numeroAcidentesCidade1 > numeroAcidentesCidade2 and numeroAcidentesCidade1 > numeroAcidentesCidade3 and numeroAcidentesCidade1 > numeroAcidentesCidade4 and numeroAcidentesCidade1 > numeroAcidentesCidade5:
    print("A cidade com maior número de acidentes é: Ibirama.")
elif numeroAcidentesCidade2 > numeroAcidentesCidade1 and numeroAcidentesCidade2 > numeroAcidentesCidade3 and numeroAcidentesCidade2 > numeroAcidentesCidade4 and numeroAcidentesCidade2 > numeroAcidentesCidade5:
    print("A cidade com maior número de acidentes é: Palhoça.")
elif numeroAcidentesCidade3 > numeroAcidentesCidade1 and numeroAcidentesCidade3 > numeroAcidentesCidade2 and numeroAcidentesCidade3 > numeroAcidentesCidade4 and numeroAcidentesCidade3 > numeroAcidentesCidade5:
    print("A cidade com maior número de acidentes é: Blumenau.")
elif numeroAcidentesCidade4 > numeroAcidentesCidade1 and numeroAcidentesCidade4 > numeroAcidentesCidade2 and numeroAcidentesCidade4 > numeroAcidentesCidade3 and numeroAcidentesCidade4 > numeroAcidentesCidade5:
    print("A cidade com maior número de acidentes é: Joinville.")
elif numeroAcidentesCidade5 > numeroAcidentesCidade1 and numeroAcidentesCidade5 > numeroAcidentesCidade2 and numeroAcidentesCidade5 > numeroAcidentesCidade3 and numeroAcidentesCidade5 > numeroAcidentesCidade4:
    print("A cidade com maior número de acidentes é: Florianópolis.")
    
print(f"A média de veículos de passeio nas cinco cidades é: {mediaVeiculosGeral:.2f}")
print(f"A média de acidentes de trânsito com vítimas nas cinco cidades é: {mediaAcidentesGeral:.2f}")