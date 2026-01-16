#Peça o valor de um salário e a porcentagem de aumento.
#Mostre:
#o valor do aumento
#o novo salário

salario = float(input('Digite o valor do seu salário: '))
aumento = float(input('Digite a porcentagem de aumento '))

valordoaumento = (salario*aumento)/100
print('Seu novo salário com aumento é {}'.format(salario+valordoaumento))