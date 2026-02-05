from time import sleep
maior = cont = 0
def valores(* num):
    print('=' * 35)
    print('Analisando os valores passados...')
    sleep(1)
    for valor in num:
        print(f'{valor}', end=' ')
    print(f'ao todo foram {len(num)} números.')
    print(f'O maior valor é {max(num)}')
    sleep(2)


valores(1, 4, 6, 7, 8, 9)
valores(4)
valores(4, 5, 4, 2)
valores(7, 8, 9)