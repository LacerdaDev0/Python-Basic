#Peça o nome completo do usuário e mostre:
#apenas o primeiro nome
#apenas o último nome

nome = str(input('Digite seu nome completo: '))
print('Seu nome completo é {}'.format(nome))
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu último nome é {}'.format(nome.split()[-1]))