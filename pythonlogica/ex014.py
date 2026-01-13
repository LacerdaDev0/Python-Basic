#Crie um programa em Python que:
#Solicite dois números ao usuário
#Solicite a operação desejada (+, -, * ou /)
#Execute a operação escolhida
#Exiba o resultado da operação

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
operacao = str(input('Digite uma operação matemática'))
if operacao == '+':
    soma = valor1 + valor2
    print('A soma vale de {} e {} é igual a {}'.format(valor1, valor2, soma))
elif operacao == '-':
    menos = valor1 - valor2
    print('A subtração de {} e {} é igual a {}'.format(valor1, valor2, menos))
elif operacao == '*':
    multiplicar = valor1 * valor2
    print('A multiplicação de {} e {} é igual a {}'.format(valor1, valor2, multiplicar))
elif operacao == '/':
    divisao = valor1 / valor2
    print('A divisão de {} e {} é igual a {}'.format(valor1, valor2, divisao))
else:
    print('Operação invalida')
