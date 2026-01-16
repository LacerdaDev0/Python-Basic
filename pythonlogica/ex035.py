valor = int(input('Digite um valor inteiro qualquer: '))
print('[ 1 ] converter para binário.')
print('[ 2 ] converter para octal.')
print('[ 3 ] converter para hexadecimal.')
n = int(input('Escolha o número: '))

if n == 1: #se o valor 'n' for igual a 1, vai converter em binário.
    print('Seu valor convertido em binário é {}.'.format(bin(valor)))
elif n == 2: #se o valor 'n' for igual a 2, vai converter em octal.
    print('Seu valor convertido em octal é {}.'.format(oct(valor)))
elif n == 3: #se o valor 'n' for igual a 3, vai converter em hexadecimal
    print('Seu valor convertido em hexadecimal é {}.'.format(hex(valor)))
else: #se não for encontrado nenhum valor, opção errada.
    print('Opção não encontrada!')