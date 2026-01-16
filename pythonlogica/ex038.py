n1 = float(input('Digite sua primeira nota:')) #Pergunte a primeira nota do usuário
n2 = float(input('Digite sua segunda nota: ')) #Pergunte a segunda nota do usuário

media = (n1 + n2) /2 #valor da média é as duas notas divido por dois
print('A media da primeira e segunda nota é {}'.format(media))
if media >= 7: #se media for maior ou igual a 7, aluno sera aprovado
     print('Você foi aprovado!')
elif media >= 5 and media <= 6.9: #senao, se o valor da média for maior ou igual a 5 e menor ou igual a 6.9, tá em recuperação
    print('Você tá em recuperação!')
else: #senao, o aluno foi reprovado
    print('Você foi reprovado com a media {}'.format(media))