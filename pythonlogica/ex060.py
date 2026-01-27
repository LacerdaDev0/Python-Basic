while True: #Enquanto for verdadeiro vai rodar até dar um break
    num = int(input('Você quer ver a tabuada de qual número? '))

    if num < 0:
        break
    print('=-=-=-=-=- T A B U A D A -=-=-=-=-=')
    for c in range(1, 11): # Para contar de 1 a 10
        print(f'{num} x {c} = {num * c}')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print('Fim do Programa!')