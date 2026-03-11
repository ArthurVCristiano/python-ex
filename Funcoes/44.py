def isTriangule(x,y,z):
    if x < y+z or y < x+z or z < x+y:
        print('Verificado')
        return True
    else: 
        return False
    
def categoriaTriangulo(x,y,z):

    if x < y+z and y < x+z and z < x+y:
        if x == y and y == z:
            return print("Triângulo Equilátero")
        if x == y or y == z or z == x:
            return print('Triângulo Isósceles')
        if x != y and y != z:
            return print('Triângulo Escaleno')
    else:
        return print('Não é um triângulo')

def analisaTriangulo():
    perimetroTotal = 0
    perimetroMedio = 0
    for i in range(5):
        x = float(input('Informe o valor de X: '))
        y = float(input('Informe o valor de Y: '))
        z = float(input('Informe o valor de Z: '))

        perimetroTotal += x + z + y
        
        if isTriangule(x,y,z) == True : 
            categoriaTriangulo(x,y,z)
    perimetroMedio= perimetroTotal / 15
    print(f'Perimetro total dos triangulos: {perimetroTotal}')
    print(f'Perimetro médio dos triangulos: {perimetroMedio}')

analisaTriangulo()