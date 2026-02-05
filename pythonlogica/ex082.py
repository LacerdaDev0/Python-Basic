def area(largura, comprimento):
    a = largura * comprimento
    print(f'Minhas medidas {largura}x{comprimento} é igual área {a}.')

print('CONTROLE DE TERRENO')
print('-' * 20)
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)