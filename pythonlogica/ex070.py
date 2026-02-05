valores = []

while True:
    n = int(input('Digite valores inteiros: '))

    if n not in valores:
        valores.append(n)
        print('O valor foi adicionado com sucesso!')
    else:
        print('O valor digitado já tá cadastrado! Tente novamente...')
        
    opcao = input('Você deseja continuar? [S/N] ').upper().strip()[0]

    if opcao == 'N':
        print('Encerrando o programa...')
        break

valores.sort()
print(f'Todos os valores digitados foram {valores}.')