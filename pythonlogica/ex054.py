from random import randint
palpite = 1 #palpite começa com 1
segredo = randint(1, 10) #biblioteca random que vai sortear um número de 1 a 10

chute = int(input('Digite seu primeiro palpite [1 a 10]: '))

while chute != segredo: #Enquanto chute for diferente de segredo, vai rodar até ser igual
    if chute < segredo: #Se chute for menor que segredo, mostre uma dica
        print('Uma dica: é um número maior que esse.')
    else:
        print('Uma dica: é um número menor que esse.')
    print('Você errou!! Tente novamente!')
    chute = int(input('Digite seu palpite: '))
    palpite += 1 #Contador de palpite

print(f'Você acertou! Precisou de {palpite} palpites.')

