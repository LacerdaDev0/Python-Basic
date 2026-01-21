import time

def cronometro_estudo(minutos):
    for c in range(1, minutos + 1):
        time.sleep(1)  # Simulando 1 minuto (em ADS usamos 60 para tempo real)

        #Calcular quantos minutos faltam
        faltam = minutos - c

        print(f"Minuto {c} concluído... Faltam {faltam} minutos.")

    print(f"BIIIIIP! Hora de descansar! Você estudou {minutos} minutos.")



if __name__ == "__main__":
    #decide quantos minutos quer estudar
    cronometro_estudo(5)