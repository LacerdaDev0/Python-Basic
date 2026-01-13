#Crie um programa em Python que:
#Solicite dois números ao usuário
#Verifique qual número é o maior
#Mostre na tela:
#qual número é maior
#ou informe que os dois números são iguais

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if n1 > n2:
    print('O valor {} é maior'.format(n1))
elif n1 < n2:
    print('O valor {} é maior'.format(n2))
else:
    print('Os dois são iguais')
