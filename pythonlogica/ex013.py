#Crie um programa em Python que:
#Solicite um valor em reais (R$)
#Converta esse valor para dólares
#Use uma taxa de conversão fixa definida no código
#Exiba o valor em reais e o valor convertido em dólares

valorreal = float(input('Digite quantos reais você tem: '))
dolar = 5.49
valorconvertido = valorreal / dolar
print('Você tem {} reais e o valor convertido é: {:.2f} dolares.'.format(valorreal, valorconvertido))