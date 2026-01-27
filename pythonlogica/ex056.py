contador = 0
total_gasto = 0
menor_preco = 0
nome_barato =  ''
cont_produtos = 0


while True: #Enquanto for verdadeiro, vai rodar
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))

    print('[ 1 ] Deseja continuar? ')
    print('[ 2 ] Deseja encerrar? ')
    opcao = int(input('Digite uma opcao valida: '))


    cont_produtos += 1
    if cont_produtos == 1: #Se for o primeiro produto da lista
        menor_preco = preco
        nome_barato = nome
    else: #Senão, se o produto atual for mais barato que preco anterior
        if preco < menor_preco:
            menor_preco = preco
            nome_barato = nome

    total_gasto += preco
    if preco > 1000: #Se o preco for maior que 1000 reais, faça uma soma dos produtos
            contador += 1
    if opcao == 1: #Se o usuário escolher opcao 1, vai continuar a compra
        print('Continuando a compra...')
    elif opcao == 2: #Senao, se escolher opcao 2, vai mostrar uma mensagem e dar break
        print('Encerrando o programa...')
        break

print(f'Total de produtos acima de 1000 reais {contador}')
print(f'Seu total gasto na compra foi de {total_gasto:.2f}')
print(f'Seu produto mais barato foi o {nome_barato} custando {menor_preco:.2f} reais.')