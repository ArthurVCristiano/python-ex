def pilha(self):
    pilhaNum = self
    return pilhaNum

def encontraTopo(self):
    pilhaNum = pilha(self)
    if len(pilhaNum) >= 2:
        return pilhaNum[-1]
    else:
        return pilhaNum[0]
    
def encontraAnt(self):
    pilhaNum = pilha(self)
    if len(pilhaNum) >= 3:
        antecessor = pilhaNum[-2]
    else:
        antecessor = pilhaNum[0]
    
    return antecessor

def addLista(self, x):
    pilhaNum = pilha(self)
    pilhaNum.append(x)

# +
def addSoma(self):
    ant = encontraAnt(self)
    topo = encontraTopo(self)
    pilhaNum = pilha(self)
    
    soma = ant + topo
        
    pilhaNum.append(soma)
    tot = sum(pilhaNum)
    return tot

def d(self):
    topo = encontraTopo(self)
    pilhaNum = pilha(self)
    pilhaNum.append(topo * 2)
    return pilhaNum

def c(self):
    pilhaNum = pilha(self)
    topo = encontraTopo(self)
    pilhaNum.remove(topo)
    
    if len(pilhaNum) <= 1:
        pilhaNum.append(0) 

    return pilhaNum

def ex1():
    self = [5,2]
    c(self)
    d(self)
    print(addSoma(self))    

def ex2():
    self = [5,-2,4]
    c(self)
    d(self)
    addLista(self, 9)
    addSoma(self)
    print(addSoma(self))
    
def ex3():
    self = [1]
    c(self)
    print(self)
    
ex1() 
ex2()
ex3()