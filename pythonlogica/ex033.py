ano = int(input('Digite um ano: '))

if ano % 400 == 0:
    print('Seu ano é bissexto!')
elif ano % 4 == 0 and ano % 100 != 0:
    print('Seu ano é bissexto!')
else:
    print('seu ano não é bissexto')
