# Jogando jokenpo com a maquina

import random 

print('1 - Pedra\n2 - Papel\n3 - Tesoura\n:: ')

usuario = int(input(''))
maquina = random.randint(1,3)
print(maquina)

if maquina == 1 and usuario == 2:
    print('USUARIO WIN!!')

elif maquina == 1 and usuario == 3:
    print('MAQUINA WIN!!')
elif maquina == 2 and usuario == 3:

    print('USUARIO WIN!!')

elif maquina == 2 and usuario == 1:
    print('MAQUINA WIN!!')
elif maquina == 3 and usuario == 2:

    print('MAQUINA WIN!!')

elif maquina == 3 and usuario == 1:

    print('USUARIO WIN!!')
elif maquina == usuario:
    print('EMPATE!')

    