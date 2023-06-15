# Advinhando o numero que a maquina está pensando e no final mostrando
# quantas tentativas foram feitas. 

import random
numero = 1
usuario = 0
chances = 0
while numero != usuario:
    numero = random.randint(1,11)
    usuario = int(input('Advinhe o numero que a maquina esta pensando entre 0 a 10: '))
    if usuario == numero:
        print('voce acertou!!')
        break
    else:
        chances += 1

print(f'Voce acertou depois de {chances} tentativas')