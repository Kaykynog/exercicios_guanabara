# Faça um programa que mostre na tela uma contagem
# Regressiva para o estouro de fogos, indo de 10 até 0
# Contendo 1 segundo de intervalo 

from time import sleep

for c in range(10,0, -1):
    sleep(1)
    print(f'Fogos em {c}...')
print('Psthciuuu iuuu')
