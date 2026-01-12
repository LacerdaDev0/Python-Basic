aluguel = int(input('Por quantos dias você alugou? '))
andou = float(input('Quantos km rodados? '))
print ('Você alugou por {} dias e rodou {}km'.format(aluguel, andou))

valoraluguel = aluguel * 60
valorandou = andou * 0.15
valorfinal = valoraluguel + valorandou

print('Seu valor final a pagar é igual a: {:.2f} reais'.format(valorfinal))