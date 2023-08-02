# Exercício Python 075: Desenvolva um programa que leia
# quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
count = soma_9 = 0
numero = (
    int(input('--> ')),
    int(input('--> ')),
    int(input('--> ')),
    int(input('--> ')),
)

print(f'Os numeros que você digitou: {numero}')
print(f'Vezes que você digitou 9: {numero.count(9)}')
if 3 in numero:
    print(f'Posição do numero 3: {numero.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram:', end='')
for i in numero:
    if i % 2 ==0:
        print(i, end=' - ')