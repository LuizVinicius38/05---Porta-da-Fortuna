import random
pontos = 0
while True:
    entrada = str(input("Deseja comprar mais carte? S/N! ")).upper()
    if entrada == "S":
        cartas = random.randrange(1, 10)
        pontos = pontos + cartas
        print("Carta comprada: {}" .format(cartas))
        print("Total de pontos: {}" .format(pontos))
        if pontos == 21:
            print("Você ganhou! {}" .format(pontos))
            break
        elif pontos > 21:
            print("Você perdeu! {}" .format(pontos))
            break
    elif entrada == "N":
        print(pontos)
        break