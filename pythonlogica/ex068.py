valores = []

for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {v} ')))

print(f'O valores digitados foram {valores}.')

maior = max(valores)
menor = min(valores)

print(f'O seu maior valor é {maior}.', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'Sua posição na lista é a {i}.', end='')

print(f'O seu menor valor é {menor}.')
for i, v in enumerate(valores):
    if v == menor:
        print(f'Sua posição na lista é a {i}.', end='')