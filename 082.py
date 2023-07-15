# Exercício Python 082: Crie um programa que vai ler vários 
# números e colocar em uma lista. Depois disso, crie duas listas 
# extras que vão conter apenas os valores pares e os valores 
# ímpares digitados, respectivamente. Ao final, mostre o 
# conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    if num %2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
        
    resposta = str(input('Deseja continuar? S/N ')).upper().strip()[0]
    if resposta in 'Ss':
        ...
    else:
        break
    
print(f'Lista inteira:{lista}')
print(f'Lista de numeros pares:{lista_par}')
print(f'Lista de numeros impares:{lista_impar}')
    
