from queue import Queue

class Fila:
    def __init__(self):
        self.fila = Queue(maxsize=100)
    
    def adc(self, valor):
        self.fila.put(valor)
    
    def remove(self):
        print("x : ")
        print(self.fila.get())
    
    def mostrar(self):
        return list(self.fila.queue)
    
    def get_min(self):
        pilha = []

        copia = list(self.fila.queue)

        for temp in copia:

            while pilha and pilha[-1] > temp:
                pilha_aux = pilha.pop()
                copia.append(pilha_aux)  
            

            pilha.append(temp)
        
        print(pilha[0])
        return pilha[0]

class Pilha:
    def __init__(self):
        self.pilha= []
        
    def push(self,valor):
        return self.pilha.append(valor)
    
    def topo(self):
        return self.pilha[-1]
    
    
o = Fila()
o.adc(5)
o.adc(3)
o.adc(8)
print(o.mostrar())
o.get_min()
o.remove()
o.get_min()
o.remove()
o.get_min()
print(o.mostrar())