def tipoFormaGeometrica():
    formaGeometrica = input('Informe a forma de escolha: [CUBO]Cubo [PARA]Paralelepípedo [CILI]Cilindro [ESFE]Esfera [CONE]Cone: ').upper()
    
    if formaGeometrica == "CUBO":
        lado = float(input('Informe o lado do cubo: '))
        return print(calculaCubo(lado))
    
    elif formaGeometrica == "PARA":
        largura = float(input('Informe a largura do paralelepipedo: '))
        comprimento = float(input('Informe o lado do paralelepipedo: '))
        altura = float(input('Informe a altura do paralelepipedo: '))
        return print(calculaParalelepipedo(largura,comprimento,altura))
    
    elif formaGeometrica == "CILI":
        raio = float(input('Informe o raio do cilindro: '))
        altura = float(input('Informe o lado do cilindro: '))
        return print(calculaCilindro(raio,altura))
    
    elif formaGeometrica == "ESFE":
        raio = float(input('Informe o raio da esfera: '))
        return print(calculaEsfera(raio))
    
    elif formaGeometrica == "CONE":
        return print(calculaCone(raio,altura))

def calculaCubo(lado):
    return lado ** 3

def calculaParalelepipedo(largura, comprimento, altura):
    return largura * comprimento * altura

def calculaCilindro(raio,altura):
    return 3.14 * raio**2 * altura

def calculaEsfera(raio):
    return (4*3.14*raio**3)/3

def calculaCone(raio,altura):
    return (3.14*raio**2*altura)/3

tipoFormaGeometrica()