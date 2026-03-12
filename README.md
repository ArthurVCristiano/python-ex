# python-ex
EX 54 -> Busca 

vetor = [] 
continuar = "Y"

while continuar == "Y":
    num = int(input("Informe um número: "))
    vetor.append(num)
    
    continuar = input("Deseja adicionar mais um número ao vetor? ").upper()
    
    if continuar != "Y":
        break
    
numBusca = int(input("Informe número de busca:"))

print(vetor)

for i, valor in enumerate(vetor):
    
    if numBusca == valor: 
        print(f"Número de busca igual a posiçõ {i + 1} do vetor")
    else:
        print("Número não encontrado!")
#FEITO NO CARTÓRIO
