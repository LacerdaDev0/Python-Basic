valor = float(input('Digite o valor da compra: '))

if valor >= 500: #se o valor for maior ou igual a 500, aplique desconto de 15%
    print('Você ganhou um desconto de 15%.')
    valor15 = (valor*15)/100 #divisão do valor com a porcentagem indicada
    valorcomdesconto15 = valor - valor15 #valor do produto com o desconto
    print('O seu produto custa {}, foi aplicado desconto de 15% e o valor final é {:.2f} reais.'.format(valor,valorcomdesconto15))

elif valor >= 300 and valor < 500: #senao se o valor for maior ou igual 300 e menor que 500. aplique desconto de 10%
    print('Você ganhou um desconto de 10%.')
    valor10 = (valor*10)/100 #divisão do valor com a porcentagem indicada
    valorcomdesconto10 = valor - valor10 #valor do produto com o desconto
    print('O seu produto custa {}, foi aplicado desconto de 10% e o valor final é {:.2f} reais.'.format(valor, valorcomdesconto10))

else: #caso nenhum valor indicado tenha aparecido, não vai dar desconto
    print('Você não tem desconto!')
    print('Seu valor final é {} reais.'.format(valor))
