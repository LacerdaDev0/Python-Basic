valor = float(input('Digite um valor: '))
desconto = int(input('Digite uma porcentagem: % '))
valordesconto = (valor*desconto)/100
valorfinal = valor + valordesconto
print('Seu valor é {:.0f} reais e tem um desconto de {}%, seu valor final com acresimo é {} reais.'.format(valor, desconto, valorfinal))