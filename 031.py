import random
numero = random.randint(0,5)
usuario = int(input('Tente advinhar o nuemro que a maquina esta pensando: '))
if numero == usuario:
    print('Voce acertou')
else:
    print('Voce errou')
