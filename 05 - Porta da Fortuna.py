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
for attempt in range(3):
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
print(f"Sua pontuação é {cont}")
    
    
