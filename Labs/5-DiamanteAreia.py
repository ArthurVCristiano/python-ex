def criaMina(self):
    pilha = self.split(" ")
    return pilha    

def minerioAtual(self):
    pilha = criaMina(self)
    if len(pilha) > 1:
        return pilha[-1]
    else:
        return pilha[0]

def minerioAntecessor(self):
    pilha = criaMina(self)
    if len(pilha) > 2:
        return pilha[-2]
    elif len(pilha) == 2:
        return pilha[0]
    else:
        return 0
        
def minera(self):
    
    pilha = self.split(" ")
    stack =[]
    contadorDiamantes = 0
        
    for item in pilha:
            if item == '<':
                stack.append(item)
            elif item == '>':
                if stack:
                    stack.pop()
                    contadorDiamantes += 1


    return contadorDiamantes

self = ". < . . . < < . . > > . . . . > . . . . > > > ."

criaMina(self)
print(minera(self))