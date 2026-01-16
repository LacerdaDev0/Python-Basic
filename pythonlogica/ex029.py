salario = float(input('Digite seu salário: '))
tempo = int(input('Digite o tempo de empresa (em anos) '))

if tempo >= 5:
    print('Você ganhou 20% de aumento!')
    aumento20 = (salario*20)/100
    print('Seu salário antigo era {} reais e com o acrescimo de 20% ficou {:.2f} reais.'.format(salario, salario + aumento20))
elif tempo >= 2 and tempo <=4:
    print('Você ganhou 10% de aumento!')
    aumento10 = (salario*10)/100
    print('Seu salário antigo era {} reais e com o acrescimo de 10% ficou {:.2f} reais.'.format(salario, salario + aumento10))
else:
    aumento5 = (salario*5)/100
    print('Você não tem muito tempo de empresa e ganhou 5% de aumento! valor {:.2f} reais.'.format(salario + aumento5))

