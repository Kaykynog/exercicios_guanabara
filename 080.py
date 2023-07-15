# Exercício Python 080: Crie um programa onde o usuário possa
# digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, 
# mostre a lista ordenada na tela.

lista = []
while True:
    item = input('Adicione um numero a sua lista: ')
    if item == item.index(1):
        item.insert(1)