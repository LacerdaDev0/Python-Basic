#Pergunte um valor, de um desconto e saiba o valor final com desconto.
 = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor do desconto: '))
print('O valor do produto é {} e {:.0f}% de desconto.'.format(produto, desconto))
valorcomdesconto = (produto * desconto) / 100
valorfinal = produto - valorcomdesconto
print('Seu valor final com desconto é igual a: {:.2f} reais'.format(valorfinal))