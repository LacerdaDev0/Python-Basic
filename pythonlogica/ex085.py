from random import randint

numeros = []


def sorteia(lista):
    for v in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
    print(f'Os valores sorteados são {numeros}')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma =+ valor
    print(f'A soma dos valores pares da {lista} é {soma}')



sorteia(numeros)
somaPar(numeros)



