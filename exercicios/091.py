# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado 
# e tenham resultados aleatórios. Guarde esses resultados em um dicionário 
# em Python. No final, coloque esse dicionário em ordem, sabendo que o 
# vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

dados = {
    'Jogador 1': randint(1,6),
    'Jogador 2': randint(1,6),
    'Jogador 3': randint(1,6),
    'Jogador 4': randint(1,6),
}
ranking = dict()

for d,j in dados.items():
    print(f'{d} tirou {j} nos dados')
    sleep(0.8)

ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print(f'RANKING: \n {ranking}')

    

