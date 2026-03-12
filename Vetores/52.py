vetorImpares = []
vetorPrimos = []
contador = 0
n =20

while len(vetorImpares) < 20:

    contador +=1

    if contador % 2 != 0:
        vetorImpares.append(contador)

for i in range(1,n):

    if n % i != 0:
        vetorPrimos.append(i)
   
print("Números ímpares: \n")
for numero in vetorImpares:
    print(f"{numero} ; ", end="")
   
print("Números primos: \n")
for numero in vetorPrimos:
    print(f"{numero} ; " ,end = "")