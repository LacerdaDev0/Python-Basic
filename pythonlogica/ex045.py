numero = int(input('Digite um número inteiro: '))

for i in range(1, 11): #nosso contador "i" vai no intervalo de 1 a 10
    multiplicador = numero * i #o número que o usuário escolheu vezes o contador vai ser nosso multiplicador
    print(f'{numero} x {i} = {multiplicador}') #mostrar o resultado
