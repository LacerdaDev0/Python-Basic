valores = {}
partidas = []
time = []

total = soma = 0
while True:
    valores.clear()
    valores['nome'] = input('Nome do jogador: ')
    part = int(input(f'Quantas partidas {valores["nome"]} jogou: '))
    partidas.clear()

    for v in range(part):
        partidas.append(int(input(f'Quantos gols na partida {v+1}: ')))
    valores['gols'] = partidas[:]
    valores['total'] = sum(partidas)
    time.append(valores.copy())

    while True:
        opcao = input('Deseja continuar? [S/N]: ').upper().strip()[0]

        if opcao in 'SN':
            break
        else:
            print('Digite uma opção valida!')

    if opcao == 'N':
        break

print('=-' * 20)
print('cod  ', end='')
for i in valores.keys():
    print(f'{i:<16}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
