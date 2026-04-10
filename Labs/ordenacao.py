import time 
start_time = time.time()
   
a = [7 , 3, 2, 8 ,-1 , 4 , 5 , 0]     

def calcula_novo(a, v):
    a.sort()
    i = 0    
    j = len(a) - 1
    while i < j:
        
        if a[i] + a[j] == v:
            print(f'({a[i] , a[j]})')
            j -=1
        elif j > v:
            j -=1
        else:
            i+=1
calcula_novo(a, 7)

tempo_final = time.time() - start_time
print("Process finished %s seconds" % (tempo_final))