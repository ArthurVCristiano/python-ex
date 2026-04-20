from queue import Queue

class calculadora(object):
    def __init__(self):
        self.fila = []
        
    def soma(self,valor_a, valor_b):
        
        soma = valor_a + valor_b
        self.fila.append(soma)
        
        return soma
    
    def subtracao(self,valor_a, valor_b):
        
        subtracao = valor_a - valor_b
        self.fila.append(subtracao)
        
        return subtracao
    
    def multiplicacao(self,valor_a, valor_b):
        
        multiplicacao = valor_a * valor_b
        self.fila.append(multiplicacao)
        
        return multiplicacao
    
    def divisao(self,valor_a, valor_b):
        
        if valor_b != 0:
            divisao = valor_a / valor_b
            self.fila.append(divisao)
            return divisao
        else:
            return "By zero"
        
    def mostraUltimaOpereacao(self):
        if len(self.fila) != 0:
            return self.fila[-1]
        else:
            return "Nenhuma operação feita"
    
    def excluirUltimaOperacao(self):
        print(self.fila.pop())
        
n  = None
c = calculadora()
print("Seja bem-vindo a calculadora do Arthur")
while n != 7:
    n = int(input(" \n Qual operação deseja fazer hoje: \n [1] Soma \n [2] Subtração \n [3] Multiplicação \n [4] Divisão \n [5] Mostrar Ultima Operacao \n [6] Excluir ultima operaçaõ \n [7] Sair \n >>"))
    

    
    match n: 
        case 1:
            print("Para começar, digite dois valores: ")
            a = float(input(">"))
            b = float(input(">"))
            soma = c.soma(a,b)
            print(f"Soma > {soma}")
            
        case 2:
            print("Para começar, digite dois valores: ")
            a = float(input(">"))
            b = float(input(">"))
            sub = c.subtracao(a,b)
            print(f"Subtração > {sub}")
            
        case 3: 
            print("Para começar, digite dois valores: ")
            a = float(input(">"))
            b = float(input(">"))
            mult = c. multiplicacao(a,b)
            print(f"Multiplicação > {mult}")
            
        case 4:
            print("Para começar, digite dois valores: ")
            a = float(input(">"))
            b = float(input(">"))
            div = c.divisao(a,b)
            print(f"Divisão > {div}" )
            
        case 5:
            last = c.mostraUltimaOpereacao()
            print(f"Ultima operação > {last}" )
            
        case 6:
            exc = c.excluirUltimaOperacao()
            print(f"Operação excluída")

        case 7:
            print("Encerrando...")
            break