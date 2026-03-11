nota1 = float(input("Informe a nota 1: ")) * 2
nota2 = float(input("Informe a nota 2: ")) * 3
nota3 = float(input("Informe a nota 3: ")) * 5

mediaPonderada = (nota1 + nota2 + nota3) / 10

if mediaPonderada >= 8.0 and mediaPonderada <= 10.0:
    print(f"Parabéns, você foi aprovado com média {mediaPonderada:.2f}, conceito A")

if mediaPonderada >= 7.0 and mediaPonderada >8.0:
    print(f"Parabéns, você foi aprovado com média {mediaPonderada:.2f}, conceito B")

if mediaPonderada >= 6.0 and mediaPonderada < 7.0:
    print(f"Você foi aprovado com média {mediaPonderada:.2f}, conceito C")

if mediaPonderada >=5 and mediaPonderada < 6.0:
    print(f"Você foi aprovado com média {mediaPonderada:.2f}, conceito D")
    
if mediaPonderada < 5.0:
    print(f"Infelizmente, você foi reprovado com média {mediaPonderada:.2f}, conceito E")