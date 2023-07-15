# # Exercício Python 081: Crie um programa que vai ler vários números
# # e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.                                                                                                           
# B) A lista de valores, ordenada de forma decrescente.                                                                                      
# C) Se o valor 5 foi digitado e está ou não na lista.
resposta = ''
verifica = 5
lista = []
while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    resposta = str(input('Deseja continuar? S/N ')).upper().strip()[0]
    if resposta in 'Ss':
        ...
    else:
        if verifica in lista:
            print('O numero 5 está na lista!')
            print('Adeus...')
            break

print(f'Numero de elementos: {len(lista)}')
print(f'Lista ordenada em decrescente: {sorted(lista, reverse=True)}')