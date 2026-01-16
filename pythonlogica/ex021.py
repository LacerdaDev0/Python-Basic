#Peça o valor de um produto e a porcentagem de desconto.
#Mostre:
#o valor do desconto
#o valor final do produto

produto = float(input('Digite o valor do produto: '))
desconto = int(input('Digite a porcentagem de desconto: '))
valorcomdesconto = (produto*desconto)/100
print('Você ganhou {} de desconto e seu valor final é {:.2f} reais.'.format(valorcomdesconto, produto-valorcomdesconto))