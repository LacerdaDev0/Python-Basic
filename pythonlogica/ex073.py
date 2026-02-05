pessoas = []
dados = []

maior = menor = 0
while True:
    dados.append(input('Digite o seu nome: '))
    dados.append(int(input('Digite o seu peso: ')))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()


    opcao = input('Você deseja continuar? [S/N]').upper().strip()[0]

    if opcao == 'N':
        print('Encerrando o programa...')
        break
print('=-' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O peso mais pesado é {maior}')
print(f'O peso menos pesado é {menor}')