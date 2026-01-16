#Peça um nome completo e mostre:
#o nome em maiúsculo
#o nome em minúsculo
#quantos caracteres ele tem (sem contar os espaços)

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome completo em maiúsculo é {}'.format(nome.upper()))
print('Seu nome completo em minúsculo é {}'.format(nome.lower()))
print('Você tem um total de {} caracteres.'.format(len(nome) - nome.count(' ')))