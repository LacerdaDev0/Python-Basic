lista = []

while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))

    media = (nota1 + nota2) / 2

    lista.append([nome, [nota1, nota2], media])

    opcao = input('Você deseja continuar? [S/N]').upper().strip()[0]
    if opcao == 'N':
        print('Encerrando o programa...')
        break

print('=-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 20)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('=-' * 30)
    opc = int(input('Digite qual aluno você quer ver a nota: [999 interromper] '))

    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(lista) - 1:
        print(f'{lista[opc][0]} tem as notas iguais a {lista[opc][1]}')
    

