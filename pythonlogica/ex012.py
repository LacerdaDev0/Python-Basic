#Crie um programa em Python que:
#Solicite o valor de um produto
#Solicite a quantidade comprada
#Calcule o valor total
#Se o valor total for maior que 100, aplique 10% de desconto
#Exiba o valor final a pagar

produto = float(input('Digite o valor do produto: '))
qnt = int(input('Digite a quantidade: '))
valortotal = produto * qnt
if valortotal > 100:
    print('Você ganhou desconto de 10% nos produtos.')
    valordesconto = (valortotal*10)/100
    valorfinal = valortotal - valordesconto
    print('Seu valor final com desconto é: {} reais'.format(valorfinal))
else:
    print('Você não ganhou desconto!')
    print('Seu valor final é {} reais'.format(valortotal))
