import time

def contagem_regressiva(segundos):

    for c in range(segundos, -1, -1):
        print(c)
        time.sleep(1)
    print('Feliz Ano novo!!')
contagem_regressiva(10)