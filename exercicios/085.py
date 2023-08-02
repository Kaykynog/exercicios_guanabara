# Exercício Python 085: Crie um programa onde o usuário possa 
# digitar sete valores numéricos e cadastre-os em uma lista única 
# que mantenha separados os valores pares e ímpares. No final, 
# mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]
cont = 1
numero = 0

for i in range(0,7):
    numero = int(input(f'Digite o {cont}º numero:' ))
    cont += 1
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

print(f'Numeros pares: {sorted(lista[0])}')
print(f'Numeros impares: {sorted(lista[1])}')
