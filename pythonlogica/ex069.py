valores = []

while True:
    n = int(input('Digite um valor inteiro: '))

    if n not in valores:
        valores.append(n)
        print('O valor foi adicionado com sucesso!')
    else:
        print('Você já digitou esse número! Tente novamente...')

    opcao = input('Você deseja continuar? [S/N] ').upper().strip().title()

    if opcao == 'N':
        print('Encerrando o programa...')
        break

valores.sort()
print(f'Todos os valores da lista já em ordem crescente são {valores}.')
