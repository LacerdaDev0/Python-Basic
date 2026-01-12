
#Diga um valor e descubra o valor em dobro, triplo e a raiz quadrada desse valor.

valor = int(input('Digite qualquer valor: '))
valorfinal = valor*2
valorfinal2 = valor*3
valorfinal3 = valor**(1/2)
print('O dobro do valor {} é igual a: {}'.format(valor, valorfinal))
print('O triplo do valor {} é igual a: {}'.format(valor, valorfinal2))
print('A raiz quadrada do valor {} é igual a: {}'.format(valor, valorfinal3))