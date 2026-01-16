altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite o seu peso: '))

imc = peso / (altura**2)
print('Você tem um IMC igual a {:.2f}'.format(imc))

if imc < 18.5:
    print('Você tá abaixo do peso!')
elif 18.5 <= imc <25:
    print('Você tá no peso ideal!')
elif 25 <= imc < 30:
    print('Você tá com sobrepeso!')
elif 30 <= imc < 40:
    print('Você tá com obesidade!')
else:
    print('Você tá com obesidade mórbida!')