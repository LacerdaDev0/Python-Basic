def fazer_login():
    usuario_correto = 'Gabriel'
    senha_correta = 'abc'

    nome = input('Digite o seu nome: ').strip()
    senha = input('Digite a sua senha: ').strip()

    if nome == usuario_correto and senha == senha_correta:
        print(f'Olá, {nome}. Você entrou com sucesso!')
        return True
    else:
        print('Usuário ou senha incorretos!')
        return False


def fazer_pagamento():
    try:  # Protege os inputs numéricos
        valor = float(input('Digite o valor do seu produto: ').replace(',', '.'))
        desconto = float(input('Digite o valor do desconto em %: ').replace(',', '.'))

        valor_desconto = (valor * desconto) / 100
        valor_total = valor - valor_desconto

        print(f'\n--- RESUMO DO PAGAMENTO ---')
        print(f'Valor original: R$ {valor:.2f}')
        print(f'Desconto aplicado: R$ {valor_desconto:.2f}')
        print(f'Valor total a pagar: R$ {valor_total:.2f}')
    except ValueError:
        print('Erro: Digite apenas números válidos para valor e desconto.')


# O BLOCO PRINCIPAL (Organizador)
if __name__ == '__main__':
    # Aqui a ponte acontece:
    logado = fazer_login()

    if logado:  # Se o login retornar True, executa o que está abaixo
        fazer_pagamento()
    else:
        print("Acesso negado. O sistema será encerrado.")