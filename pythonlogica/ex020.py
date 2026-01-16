#Peça dois números ao usuário e mostre:
#a soma
#a subtração
#a multiplicação
#a divisão

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

print('A soma de {} e {} é igual a {:.2f}.'.format(n1, n2, n1+n2))
print('A subtração de {} e {} é igual a {:.2f}.'.format(n1, n2, n1-n2))
print('A multiplicação de {} e {} é igual a {:.2f}.'.format(n1, n2, n1*n2))
print('A divisão de {} e {} é igual a {:.2f}.'.format(n1, n2, n1/n2))
print('Aqui tá todos os resultados obtidos!')