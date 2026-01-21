def somar_apenas_pares():
    soma = 0

    for i in range(1, 7): #para i no intervalo de 1 ao 6
        n = int(input(f'Digite o {i}º número: '))


        if n % 2 == 0: #resto da divisão por 2 é zero
            soma += n
        else:
            #desconsiderar o número impar
            print("Número ímpar desconsiderado.")

    print(f'\nSeu valor total de pares somados é igual a {soma}.')


if __name__ == '__main__':
    somar_apenas_pares()