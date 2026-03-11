nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))
operacao = input("[A] Aritmética [P]Ponderada:").upper()

def mediaAritmetica(nota1,nota2, nota3):
    media =  ((nota1 + nota2 + nota3) / 3)

    return print(media)

def mediaPonderada(nota1,nota2,nota3):
    media = ((nota1 * 0.5) + (nota2 * 0.3) + (nota3 * 0.2))
    return print(media)

if operacao == "A":
    print(mediaAritmetica(nota1, nota2, nota3))
elif operacao == "P":
    print(mediaPonderada(nota1, nota2, nota3))