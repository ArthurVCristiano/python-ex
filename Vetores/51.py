vetor = [1,2,3,4,5,6,7,8,9,10] 
posicao = input("Informe o valor da posição do vetor (X e Y), divida por ,:")
xvetor = posicao.split(",")

indicex = int(xvetor[0])
indicey = int(xvetor[1])

x = vetor[indicex]
y = vetor[indicey]

print(f"Soma de X: {x} e Y: {y} é de: {x + y}")