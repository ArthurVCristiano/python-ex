angulo1 = float(input("Informe o angulo 1 do triangulo : "))
angulo2 = float(input("Informe o angulo 2 do triangulo : "))
angulo3 = float(input("Informe o angulo 3 do triangulo : "))

somaAngulos = angulo1 + angulo2 + angulo3

if somaAngulos == 180:
    
    if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("O triangulo é retangulo")
        
    elif angulo1 == angulo2 and angulo1 == angulo3:
        print("O triangulo é equilatero")
    
else:
    print("Os angulos não formam um triangulo")