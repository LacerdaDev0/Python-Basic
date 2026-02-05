valores = {}
partidas = []

total = soma = 0

valores['nome'] = input('Nome do jogador: ')
part = int(input(f'Quantas partidas {valores["nome"]} jogou: '))

for v in range(part):
    partidas.append(int(input(f'Quantos gols na partida {v+1}: ')))
valores['gols'] = partidas[:]
valores['total'] = sum(partidas)
    

print('=' * 20)
print(valores)
print('=' * 20)
for k, v in valores.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 20)
print(f'O jogador {valores['nome']} jogou {len(partidas)} partidas.')
for i, v in enumerate(valores['gols']):
    print(f'  Na partida {i+1} fez {v} gols')
print(f'Totalizando um total de {valores['total']} gols')