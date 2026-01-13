nome = str(input('Digite o seu nome completo: ')).strip()

print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem {} caracteres.'.format(len(nome) - nome.count(' ')))
nomesep = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(nomesep[0], len(nomesep[0])))