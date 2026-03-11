i = int(input('Informe um valor entre (1,2,3): '))
a = float(input('Informe o valor de A: '))
b = float(input('Informe o valor de B: '))
c = float(input('Informe o valor de C: '))
aux = 0

if i == 1:
    if a >b and a > c:
        aux = a
        if b>c:
            print(f"A ordem é: {aux} > {b} > {c}")
        else:            
            print(f"A ordem é: {aux} > {c} > {b}")
    if b > a and b > c:
        aux = b
        if a>c:
            print(f"A ordem é: {aux} > {a} > {c}")
        else:            
            print(f"A ordem é: {aux} > {c} > {a}")
    if c > a and c > b:
        aux = c
        if a>b:
            print(f"A ordem é: {aux} > {a} > {b}")
        else:            
            print(f"A ordem é: {aux} > {b} > {a}")

if i == 2:
    if a < b and a < c:
        aux = a
        if b < c: 
            print(f'A ordem decrescente é: {aux} < {b} < {c}')
        if c < b: 
            print(f'A ordem decrescente é: {aux} < {c} < {b}')
    if b < a and b < c:
        aux = b
        if a < c: 
            print(f'A ordem decrescente é: {aux} < {a} < {c}')
        if c < a: 
            print(f'A ordem decrescente é: {aux} < {c} < {a}')
    if c < a and c < b:
        aux = c
        if a < b: 
            print(f'A ordem decrescente é: {aux} < {a} < {b}')
        if b < a: 
            print(f'A ordem decrescente é: {aux} < {b} < {a}')
            
if i == 3:
    if a > b and a > c:
        print(f'{b} < {a} < {c}')
    if b> a and b > c:
        print(f'{a} < {b} < {c}')
    if c > a and c > b:
        print(f'{a} < {c} < {b}')