from datetime import datetime
dados = {}

dados['Nome'] = input('Nome: ')
ano = int(input('Ano de nascimento: '))
dados['Ctps'] = int(input('Carteira de Trabalho [0 não tem]: '))
ano_atual = datetime.today().year - ano
dados['Idade'] = ano_atual

if dados['Ctps'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salario'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = ano_atual + ((dados['Contratação'] + 35) - datetime.today().year)

print('=-' * 20)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
