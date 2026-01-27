menor = cont = total_gasto = produto_caro = 0
while True:
    print('-' * 30)
    print('       Loja Mix Lacerda')
    print('-' * 30)
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))

    cont += 1
    total_gasto += preco # saber a soma total
    if preco > 1000:
        produto_caro += 1

    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco

    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Quer continuar? [S/N]: ').upper().strip()[0]



    if opcao == 'N':
        print('Finalizando a compra...')
        break
print(f'O total da compra foi de R$ {total_gasto:.2f}')
print(f'Temos {produto_caro} produtos custando 1000 reais.')
print(f'O produto com o menor preço custa {menor:.2f} reais.')
