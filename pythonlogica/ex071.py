valores = []

while True:
    n = int(input('Digite um valor inteiro: '))
    valores.append(n)
    opcao = input('Você deseja continuar? [S/N] ').upper().strip()[0]

    if opcao == 'N':
        print('Encerrando o programa...')
        break
print('=-' * 30)
print(f'Esses são todos os valores digitados: {valores}.')
print(f'Foram digitados {len(valores)} valores.')
valores.sort(reverse=True)
print(f'Os valores em decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 foi digitado {valores.count(5)}.')
else:
    print('Você não tem o valor 5 armazenado na lista!')