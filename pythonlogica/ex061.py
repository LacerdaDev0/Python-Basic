maior_idade = 0
contadorh = 0
menor_idadem = 0
while True:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
          '     CADASTRE UMA PESSOA\n'
          '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').upper().strip()[0]


    if idade >= 18:
        maior_idade += 1

    if sexo == 'M':
        contadorh += 1

    if sexo == 'F' and idade < 20:
        menor_idadem += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Quer continuar [S/N]: ').upper().strip()[0]

    if opcao == 'N':
        print('Encerrando o Programa...')
        break

print(f'Tem um total de {maior_idade} pessoas com mais de  18 anos.')
print(f'Tem um total de {contadorh} homens cadastrados.')
print(f'Tem um total de {menor_idadem} mulheres com menos de 20 anos.')
