s = [ "(", "[" , "{" , "}", "]", ")"  ]

def __init__(self):
    signs = self
    return signs

def size(self):
    signs = self
    return len(signs)

def search_equals(self):
    signs = self
    signP = 0
    signCo = 0
    signCha = 0
    
    
    for i in range(len(signs)):
        
            if signs[i] == "(":
                signP += 1
            elif signs[i] == ")":
                signP += 1
                
            elif signs[i] == "{":
                signCo += 1
            elif signs[i] == "}":
                signCo += 1
                
            elif signs[i] == "[":
                signCha += 1
            elif signs[i] == "]":
                signCha += 1
                
    if signP % 2 == 0 and signCo % 2 == 0 and signCha % 2 == 0:
        print("Todos os valores tem par")
        return True

    return False

def sorted_open_close(self):
    pilha = self
    sorted_s = self.sort()
    pares = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for char in s:
        if char in "([{":
            pilha.append(char)
        else:
            if not pilha or pilha[-1] != pares[char]:
                return False
            pilha.pop()
    
    return len(pilha) == 0
        


def is_valid(self):
    signs = self
    pontuacao = 0
    
    if len(signs) > 1:
        pontuacao += 1
    else: 
        print("Lista não possui dupla")
        
    if search_equals(self):
        pontuacao += 1
    else:
        print("Nenhuma dos caractes possuem dupla")
    
    if sorted_open_close(self) != False:
        pontuacao += 1
    else:
        print("Não é fechado pelo mesmo simbolo")
        
    if pontuacao == 3:
        print("Válido, três requisitos atendidos")
    else:
        print("Portanto, não é válido")
    
        

def conta_sinais(self):
    signs = self

   

print(is_valid(s))
