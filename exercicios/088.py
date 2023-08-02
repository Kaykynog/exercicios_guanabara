# Exercício Python 088: Faça um programa que ajude um jogador da 
# MEGA SENA a criar palpites.O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint

print('*'*30)
print('PALPITES PARA MEGA SENA')
print('*'*30)
jogo = list()  
lista = list()
contador = 0
sorteio = int(input('Quantos palpites voce quer para jogar na mega? '))
total = 1
while total <= sorteio:
    while True:
        aleatorio = randint(1,60)
        if aleatorio not in jogo:
            jogo.append(aleatorio)
            contador += 1
        if contador >= 6:
            break


    jogo.sort()
    lista.append(jogo[:])
    jogo.clear() 
    print(lista)
    lista.clear()
    total += 1

    