lista_principal = [[], []]


for v in range(1,8):
    n = int(input(f'Digite o {v} valor: '))
    

    if n % 2 == 0:
        lista_principal[0].append(n)
        
    else:
        lista_principal[1].append(n)
        
    
lista_principal[0].sort()
lista_principal[1].sort()
print(f'Todos os valores são {lista_principal}')
print(f'Os valores pares são {lista_principal[0]}')
print(f'Os valores impares são {lista_principal[1]}')

