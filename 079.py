# Exercício Python 079: Crie um programa onde o usuário possa 
# digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

lista = []
while True:
    item = input('Digite um numero: ')
    if item in lista:
        print('Não pode adicionar')
    else:
        lista.append(item)
        print(lista)
        print(f'Em ordem crescente...{sorted(lista)}')