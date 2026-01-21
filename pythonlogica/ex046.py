soma = 0 #variável soma vai guardar o valor zero

for i in range(1, 6): #para i no intervalo de 1 a 5
    numero_usuario = int(input('Digite um valor: ')) #usuário vai digitar o número
    soma = soma + numero_usuario #a soma mais o numero do usuário vai resultar no valor total
print(f'Seu valor total é {soma}')
