# Exercício Python 078: Faça um programa que leia
# 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições 
# na lista.

lista = [
    input('Digite um valor para a posição 0: '),
    input('Digite um valor para a posição 1: '),
    input('Digite um valor para a posição 2: '),
    input('Digite um valor para a posição 3: '),
    input('Digite um valor para a posição 4: '),
]
maximo = max(lista)
print((f'o maior valor foi...{max(lista)} na posição...{lista.index(max(lista))}'))
print((f'o menor valor foi...{min(lista)} na posição...{lista.index(min(lista))}'))