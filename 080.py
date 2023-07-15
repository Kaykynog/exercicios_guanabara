# Exercício Python 080: Crie um programa onde o usuário possa
# digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, 
# mostre a lista ordenada na tela.

lista = []

for l in range(0,5):
    item = int(input('Digite um numero: '))
    if l == 0 or item > lista[len(lista)-1]:
        lista.append(item)
        print('Adicionando ao final da lista...')
    else:
        posicao = 0
        while posicao < len(lista):
            if item <= lista[posicao]:
                lista.insert(posicao, item)
                print(f'Adicionando na posição:{posicao}...')
                break
            posicao += 1
print(lista)