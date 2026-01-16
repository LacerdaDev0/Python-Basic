from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))

idadeatual = date.today().year - ano #ano atual menos o ano da idade do usuário é igual a idade atual

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idadeatual, date.today().year))
if idadeatual > 18: #se a idade atual for maior que 18, mostre que ele já passou da idade
    print('Você deveria ter se alistado há {} anos.'.format(idadeatual - 18))
elif idadeatual == 18: #senao, se a idade atual for igual a 18, mostra que ele já tá na idade
    print('Você tem exatamente {} e já pode se alistar!'.format(idadeatual))
else: #senao mostra que não tem idade suficiente
    print('Você ainda não tem idade!')
