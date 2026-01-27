soma = contador = maior = menor = 0

while True:
    num = int(input('Digite um número inteiro: '))

    # Cálculos básicos
    soma += num
    contador += 1


    if contador == 1:
        maior = menor = num
    else:
        # Se não for o primeiro,  compara com o que já tem guardado
        if num > maior:
            maior = num
        if num < menor:
            menor = num


    con = input('Quer continuar? [S/N]: ').upper().strip()

    if con == 'N':
        print('Encerrando o programa...')
        break

# Cálculo da média
media = soma / contador

print(f'\nVocê digitou {contador} números e a média foi {media:.2f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')