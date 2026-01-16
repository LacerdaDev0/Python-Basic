ds = float(input('Digite a distância percorrida: '))

print('Você tá preste a começar uma viagem de {}km.'.format(ds))
if ds <= 200:
    valor1 = ds*0.50
    print('Como você vai percorrer menos de 200km, sua viagem vai custar 0,50 por km.')
    print('Seu valor total é {:.2f} reais.'.format(valor1))
elif ds > 200:
    valor2 = ds*0.45
    print('Como você vai percorrer mais de 200km, sua viagem vai custar 0,45 por km.')
    print('Seu valor total é {:.2f} reais.'.format(valor2))