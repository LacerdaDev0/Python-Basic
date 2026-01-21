for i in range(1, 31): #para i no intervalo de 1 a 30
    if i % 3 == 0 and i % 5 == 0: #se "i" divido por 3 restar 0 e divido por 5 restar 0 = são multiplos
        print('FizzBuzz')
        print(f'{i} é multiplo de 3 e 5.')
    elif i % 3 == 0: #senao, se "i" divido por 3 restar 0, é multiplo de 3
        print('Fizz')
        print(f'{i} é multiplo de 3.')
    elif i % 5 == 0: #senao, se "i" divido por 5 restar 0, é multiplo de 3
        print('Buzz')
        print(f'{i} é multiplo de 5.')
    else: #senao, mostre apenas o valor
        print(f'{i}')
