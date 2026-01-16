from datetime import date #vai importar a biblioteca datetime
ano = int(input('Digite o ano de nascimento: '))

ano_atual = date.today().year #saber o ano atual
idade_atual = date.today().year - ano #o ano atual menos a idade de nascimento pra saber a idade

print('Você é nascido em {} e tem {} anos.'.format(ano, idade_atual))

if idade_atual <= 9: #se idade atual for menor ou igual 9, mostre mirim
    print('Você é categoria Mirim!')
elif idade_atual <= 14: #senao, se idade atual for menor ou igual 14, mostre infantil
    print('Você é categoria infantil!')
elif idade_atual <= 19: #senao, se idade atual for menor ou igual 19, mostre junior
    print('Você é categoria junior!')
elif idade_atual <= 25: #senao, se idade atual for menor ou igual 25, mostre senior
    print('Você é categoria senior!')
else: #senao for igual nenhuma das alternativas, mostre master. isto é, é maior que 25
    print('Você é categoria MASTER!')