idadeJogador = int(input("Digite a idade do jogador: "))
alturaJogador = float(input("Digite a altura do jogador: "))
pesoJogadores = float(input("Digite o peso do jogador: "))
continuar = input("Digite S para continuar?: ").upper()
contador = 0
mediaAltura = 0
mediaIdade = 0
qtdIdadeMaior18 = 0

while continuar == "S":
    contador +=1
    if contador <= 11:
        print("=== TIME DE IBIRAMA ===")
    idadeJogador = int(input(f"Informe a idade do Jogador {contador}: "))
    mediaIdade += idadeJogador
    if idadeJogador < 18:
        qtdIdadeMaior18 += 1
    alturaJogador = float(input(f"Informe a altura do Jogador {contador}: "))
    mediaAltura += alturaJogador
    pesoJogadores = float(input(f"Informe o peso do Jogador {contador}: "))
    if pesoJogadores > 80:
        pesoJogadores += 1
        
    if contador > 11 and contador <= 22:
        print("=== TIME GUARANI DA PALHOÇA ===")
    idadeJogador = int(input(f"Informe a idade do Jogador {contador}: "))
    mediaIdade += idadeJogador
    if idadeJogador < 18:
        qtdIdadeMaior18 += 1
    alturaJogador = float(input(f"Informe a altura do Jogador {contador}: "))
    mediaAltura += alturaJogador
    pesoJogadores = float(input(f"Informe o peso do Jogador {contador}: "))
    if pesoJogadores > 80:
        pesoJogadores += 1
        
    continuar = input("Deseja continuar? Digite S para sim: ").upper()
    
mediaAltura = mediaAltura / contador
mediaIdade = mediaIdade / contador

print(f"A média de altura dos jogadores é: {mediaAltura:.2f}")
print(f"A média de idade dos jogadores é: {mediaIdade:.2f}")
print(f"A quantidade de jogadores com idade menor que 18 anos é: {qtdIdadeMaior18}")
print(f"O percentual de jogadores com peso maior que 80 kg é: {pesoJogadores/contador*100:.2f}%")