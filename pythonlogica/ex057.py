from random import randint #Importar a biblioteca random

print('Oi, eu sou o seu computador. \n'
      'Vamos fazer uma brincadeira: Adivinhe um número de 1 a 10.')

contador = 0
palpite = randint(1, 10)

while True: #Enquanto for verdadeiro, rode
    chute = int(input('Faça um chute de 1 a 10: '))
    contador += 1
    if chute == palpite:
        print(f'Você acertou com um total de {contador} chutes')
        break
    elif chute > palpite:
        print('Menos, você tá quase lá!')
    elif chute < palpite:
        print('Mais, você tá quase lá')