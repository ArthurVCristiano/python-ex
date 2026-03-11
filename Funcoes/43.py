import math

equacao = (input("Informe a equacao como formula separado por , : "))
x = equacao.split(",")
a = float(x[0])
b = float(x[1])
c = float(x[2])

def formulaBhaskara(a,b,c):
    delta = b**2 - 4*a*c
    bhaskaraX1 = (-b + math.sqrt(delta))/(2 * a)
    bhaskaraX2 = (-b - math.sqrt(delta))/(2 * a)

    print(f"x1: {bhaskaraX1} e x2 {bhaskaraX2}")

formulaBhaskara(a,b,c)