from time import sleep

# Criando uma função para fazer a contagem
def contador(i, f, p): 
    print('=' * 30)
    print(f'A contagem vai começar em {i} vai até {f} pulando de {p} e {p}')
    sleep(2)

    
    if p < 0:
        p *= -1
    if p == 0: #Aqui vai converter o zero em 1 pra não dar problema
        print('Não é possivel pular por ZERO! convertendo em 1')
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
            
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
            
        print('FIM')



contador(1, 10, 1)
contador(10, 0, 2)


print('Agora é sua vez de escolher: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
pulo = int(input('Pulando: '))

contador(inicio, fim, pulo)
