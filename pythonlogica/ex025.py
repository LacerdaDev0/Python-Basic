#Peça uma frase ao usuário e mostre:
#quantas vezes aparece a letra “a”
#a posição da primeira letra “a”
#a posição da última letra “a”

fr = str(input('Digite uma frase: ')).upper().strip()
print('Letra A aparece {} vezes'.format(fr.count('A')))
print('Letra A na primeira posição {}'.format(fr.find('A')+1))
print('Letra A na última posição {}'.format((fr.rfind('A')+1)))
