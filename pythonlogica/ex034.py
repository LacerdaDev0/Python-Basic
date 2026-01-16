casa = float(input('Digite o valor da casa: ')) #usuário vai digitar o valor da casa
salario = float(input('Quanto você recebe por mês? ')) #usuário vai digitar quanto ele recebe.
ano = int(input('Em quantos anos você quer parcelar? ')) #usuário vai digitar quantidade de anos

prestacao = casa / (ano*12) #valor da prestação é o valor da casa dividido por a quantidade de meses das parcelas.
limite = (salario*30)/100 #limite de 30% do salário do usuário

if prestacao <= limite: #se a prestação for menor ou igual limite o programa vai dar como aprovado
    print('Seu emprestimo foi aprovado!')
else: #senao foi negado
    print('Seu emprestimo foi negado!')
