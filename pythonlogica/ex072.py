listatotal = []
pareslista = []
imparlista = []

while True:
    n = int(input('Digite valores inteiros: '))
    listatotal.append(n)

    if n % 2 == 0: # Se o número digitado restar 0, vai adicionar n na lista de pares
        pareslista.append(n)
    else: # Senão o número digitado restar 1, vai adicionar n na lista de impares
        imparlista.append(n)

    opcao = input('Você deseja continuar? [S/N]').upper().strip()[0]
    if opcao == 'N':
        break

print('=-' * 25)
print(f'Todos os números digitados foram: {listatotal}')
print(f'Todos os valores pares digitados são {pareslista}')
print(f'Todos os valores impares digitados são {imparlista}')
print('=-' * 25)