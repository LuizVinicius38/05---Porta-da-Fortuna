jogando = True
cont = 0
from random import *
print('''
Porta da Fortuna!
=========

Existe um super prêmio atrás de uma destas 3 portas!
Advinhe qual é a porta certa para ganhar o prêmio!
   _____   _____   _____
  |     | |     | |     |
  | [1] | | [2] | | [3] |
  |     | |     | |     |
  |_____| |_____| |_____|
  ''')
while jogando == True:
    print("\nEscolha uma porta(1, 2 ou 3):")
    portaEscolhida = input("")
    portaEscolhida = int(portaEscolhida)
    portaCerta = randint(1,3)
    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)
    if portaEscolhida == portaCerta:
        print("Parabéns")
        cont = cont + 1
    else:
        print("Que pena")
        cont = 0
    print(f"Sua pontuação é {cont}")
    print("\nVocê que jogar de novo? (s/n)")
    resposta = input("").lower()[0]
    if resposta == 'n':
        jogando = False
print("Obrigado por jogar.")
print("Sua pontuação final é", cont)



