maior_peso = 0
menor_peso = 0

for pessoas in range(1, 6): #para pessoas no intervalo de 1 a 5
    peso = float(input(f'Peso da {pessoas}ª pessoa: '))
    if pessoas == 1: #se pessoas é igual a 1
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'O maior peso é: {maior_peso}.')
print(f'O menor peso é {menor_peso}.')
