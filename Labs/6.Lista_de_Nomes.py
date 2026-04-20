from queue import Queue

class nameList(object):
    
    def __init__(self):
        self.fila = Queue(maxsize=12)
    
    def insert_names(self):
        nome = ""
        auxiliar = ""      
        fila2 = ""
        tamanhoInterior = None


        while not self.fila.full():
            
            nome = input("nome > ")
            
            if tamanhoInterior is None:
                fila2 += nome
            elif len(nome) == tamanhoInterior:
                fila2 += "\n" + nome
            else:
                fila2 += ", " + nome
            
            tamanhoInterior = len(nome)
            
            self.fila.put(nome)

        print(fila2)

    
            
            

c = nameList()
c.insert_names()

