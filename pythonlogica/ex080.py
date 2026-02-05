dados_lista = []
dados_dic = {}

media = soma = 0

while True:
    dados_dic.clear()
    dados_dic['Nome'] = input('Nome: ').strip()

    while True:
        dados_dic['Sexo'] = input('Sexo: ').upper().strip()[0]
        if dados_dic['Sexo'] in 'MF':
            break
        print('Digite uma opção correta!')

    dados_dic['Idade'] = int(input('Idade: '))
    soma += dados_dic['Idade']

    dados_lista.append(dados_dic.copy())
    while True:
        opcao = input('Você deseja continuar? [S/N]: ').upper().strip()[0]
        if opcao in 'SN':
            break
        else:
            print('Digite uma opção valida!')
    if opcao == 'N':
        break

media = soma / len(dados_lista)
    

print(f'Total de {len(dados_lista)} pessoas cadastradas.')
print(f'A media de idade das pessoas é {media:5.2f}')
print('Nome de mulheres cadastradas é: ', end='')
for p in dados_lista:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print()