nome = str(input('Digite o seu nome completo: ')).strip()
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))

media = (n1+n2+n3)/3
if media >= 7: #saber se a media é maior ou igual a 7
    print('Você foi aprovado!')
    print('{} você teve uma média final de {:.2f} e você foi aprovado!'.format(nome, media))

elif media >= 5 and media < 7: #saber se a média é maior ou igual a 5 e menor que 7
    print('Você tá em recuperação!')
    print('{} você teve uma média final de {:.2f} e você tá em recuperação!'.format(nome, media))

else: #senao nenhuma média for alcançada = reprovado
    print('Você foi reprovado!')
    print('{} você teve uma média {:.2f} e tá reprovado!'.format(nome, media))
