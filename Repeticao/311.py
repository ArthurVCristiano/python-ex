ciclos = float(input("Informe um número: "))
numero = 1
auxiliar = 1
segundoAuxiliar = 0
sequencia = "0, 1, 1, "
#(0,1,1,2,3,5,8,13,21,...)

for i in range(int(ciclos - 3)):
    if numero == 0:
        print(0)
    else:
        segundoAuxiliar = auxiliar
        auxiliar = numero
        numero = segundoAuxiliar + auxiliar
        sequencia += str(numero) + ", "
        
print(sequencia)