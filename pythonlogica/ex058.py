valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

while True: # Início do loop principal do sistema
    print('---------- M E N U ----------- \n'
          '[ 1 ] Somar \n'
          '[ 2 ] Multiplicar \n'
          '[ 3 ] Divisão \n'
          '[ 4 ] Mudar valores \n'
          '[ 5 ] Sair do programa \n')

    opcao = int(input('Digite a sua opcao: '))

    # Estrutura condicional para processar a escolha do usuário
    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} é igual a {soma}.')

    elif opcao == 2:
        multiplicar = valor1 * valor2
        print(f'A multiplicação de {valor1} e {valor2} é igual a {multiplicar}.')

    elif opcao == 3:
        if valor2 != 0: #impede a quebra do sistema por divisão por zero
            divisao = valor1 / valor2
            print(f'A divisão entre {valor1} e {valor2} é igual a {divisao}.')
        else:
            print('Não existe valor dividido por zero')

    elif opcao == 4: # Permite atualizar as variáveis de cálculo sem reiniciar o script
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))

    elif opcao == 5:
        print('Saindo do programa...')
        break

    else:
        print('Opção invalida!! Tente novamente!')
print('Fim do programa!')