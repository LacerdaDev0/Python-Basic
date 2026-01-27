listagem = ('Papel', 1.79,
           'Caderno', 21.89,
           'Lápis', 2,
           'Borracha', 2,
           'Caneta', 2.19,
            'Bolsa', 84,99)

print('=-' * 20)
print(f'{"SuperMercado Lacerda":^40}')
print('=-' * 20)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')

    else:
        print(f'R$ {listagem[pos]:>7.2f}')