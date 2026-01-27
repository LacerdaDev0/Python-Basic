extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    valor = int(input('Digite um valor inteiro entre 0 e 10: '))

    if 0 <= valor <= 10:
        break

    else:
        print('Tente novamente, digite um valor entre 0 e 10')


print(f'Você digitou {extenso[valor]}')