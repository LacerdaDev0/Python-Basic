#Crie um programa em Python que:
#Solicite um número inteiro ao usuário
#Verifique se o número é par ou ímpar
#Exiba o resultado

valor = int(input('Digite um valor inteiro: '))
if valor % 2 == 0:
    print('Seu número é par')
else:
    print('Seu número é impar')