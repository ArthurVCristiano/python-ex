numeromn = input("Informe o valor de m e n: ")
numeros = numeromn.split()
m = int(numeros[0])
n = int(numeros[1])
auxiliar = m
sequencia = "  "
somador = 0

while m < n:
    m += 1
    auxiliar = m
    if auxiliar >= m and auxiliar < n:
        sequencia += str(auxiliar) + ", "
        somador += auxiliar

print(sequencia)
print(somador)