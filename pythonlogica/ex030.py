veloc = int(input('Qual a velocidade do carro em km? '))

if veloc > 80:
    print('Seu carro ultrapassou 80km/h e você foi multado!')
    multa = (veloc - 80) * 7
    print('Você ultrapassou o limite e o valor da multa é {} reais por cada km excedido'.format(multa))
else:
    print('Você não foi multado')