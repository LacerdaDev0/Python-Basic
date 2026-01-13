#Crie um programa em Python que:
#Solicite um número ao usuário
#Verifique se o número é positivo, negativo ou zero
#Exiba o resultado

valor = float(input('Digite um número: '))
if valor > 0:
    print('Seu valor é positivo')
elif valor < 0:
    print('Seu valor é negativo')
else:
    print('Seu valor é igual a 0')