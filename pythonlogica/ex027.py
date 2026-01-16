valor = float(input('Digite o valor do produto: '))
form = str(input('Digite a forma de pagamento CARTÃO/A VISTA: '))

if form == 'a vista':
    print('Você ganhou desconto de 10%')
    valor10 = (valor*10)/100 #calculo do valor com o desconto
    print('Seu valor final com desconto de 10% é {} reais.'.format(valor - valor10)) #valor final do produto com o desconto

elif form == 'cartão':
    print('Nessa forma de pagamento vai ter acrescimo de 5%')
    valor5 = (valor*5)/100 #calculo do valor com o acrescimo
    print('Seu valor final com acrescimo de 5% é {} reais.'.format(valor + valor5)) #valor final do produto com o acrescimo
else:
    print('Sua forma de pagamento é invalida! A VISTA OU CARTÃO')

