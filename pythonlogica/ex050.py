def calcular_pagamento():
    try:
        entrada = input('Digite o valor do pagamento: ').replace(',','.')
        valor = float(entrada)

        print('----FORMAS DE PAGAMENTO----')
        print('''[ 1 ] á vista [10% OFF]
        [ 2 ] débito cartão [5% OFF]
        [ 3 ] 2x no cartão [SEM JUROS]
        [ 4 ] 3x no cartão [JUROS 20%]''')

        opcao = int(input('Escolha a sua opção.'))

        valor_final = valor
        mensagem = ''

        if opcao == 1:
            valor_final = valor * 0.90
            mensagem = 'Você ganhou 10% de desconto!'
        elif opcao == 2:
            valor_final = valor * 0.95
            mensagem = 'Você ganhou 5% de desconto!'
        elif opcao == 3:
            mensagem = 'Preço normal, sem juros.'
        elif opcao == 4:
            valor_final = valor * 1.20
            mensagem = 'Teve um acrescimo de 20%.'
        else:
            print('Opção invalida!')
            return #encerre a função se for opção errada

        print(f'\n--- RESUMO DA COMPRA ---')
        print(f'Status: {mensagem}')
        print(f'Valor original: R$ {valor} reais.')
        print(f'Valor final a pagar R$ {valor_final:.2f} reais.')

    except ValueError:
        print('Digite apenas opção valida!')

if __name__ == '__main__':
    calcular_pagamento()