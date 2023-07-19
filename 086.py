# Exercício Python 086: Crie um programa que declare uma
# matriz de dimensão 3×3 e preencha com valores lidos pelo 
# teclado. No final, mostre a matriz na tela, com a formatação 
# correta.

matriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
 ]


 
for m in range(0,3):
    for l in range(0,3):    
        matriz[m][l] = int(input(f'Digite um numero para alocar na matriz --> [{m}, {l}] '))

print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')

