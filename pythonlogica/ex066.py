num = (int(input('Digite um numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite mais um numero: ')))

print(f'Seus valores digitados são {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 foi digitado na posição {num.index(3)+1}')
else:
    print('Não foram digitados nenhum valor 3')
print(f'Os valores pares são', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')