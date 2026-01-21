from datetime import date

maior_idade = 0
menor_idade = 0
ano_atual = date.today().year

for i in range(1, 8):
    ano = int(input(f'Digite data de nascimento {i}ª'))
    idade = ano_atual - ano
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print('=-' * 15)
print(f'{maior_idade} são maiores de idade.')
print(f'{menor_idade} são menores de idade.')
print('=-' * 15)