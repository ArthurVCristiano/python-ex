vetor = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

print(vetor)

for i in range(8):
    vetor[i], vetor[i+8] = vetor[i+8], vetor[i]

print(vetor)