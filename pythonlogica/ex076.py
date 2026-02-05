valores = {}

valores['Nome'] = input('Nome: ')
valores['Media'] = float(input('Média do aluno: '))


for k, v in valores.items():
    print(f'{k} é igual a {v}')

if valores['Media'] >=7:
    print('Situação é igual Aprovado!')
else:
    print('Situação é igual Reprovado!')