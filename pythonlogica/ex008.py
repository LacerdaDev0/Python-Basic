altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
tinta = area / 2
print('Sua área é equivalente a {}x{} que é igual: {}'.format(altura, largura, area))
print('Levando em consideração que precisa de 2l de tinta pra pintar a parede, você precisara de {}l de tinta'.format(tinta))