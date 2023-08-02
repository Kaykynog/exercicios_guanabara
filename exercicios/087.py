# Exercício Python 087: Aprimore o desafio anterior, mostrando 
# no final:                                                    
# A) A soma de todos os valores pares digitados.                                                                                                  
# B) A soma dos valores da terceira coluna.                                                                                                                
# C) O maior valor da segunda linha.

matriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
 ]
soma_terceira = soma_par = 0

for m in range(0,3):
    for l in range(0,3):    
        matriz[m][l] = int(input(f'Digite um numero para alocar na matriz --> [{m}, {l}] '))
        if matriz[m][l] % 2 == 0:
            soma_par += matriz [m][l]
# Somando a terceira linha da matriz
for m in range(0,3):
    soma_terceira += matriz [m][2]

print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
print(f'Soma dos pares --> {soma_par}')
print(f'Soma da terceira coluna --> {soma_terceira}')
print(f'Maior valor da segunda coluna {max(matriz[1])}') # Retornando maior valor da segunda linha da matriz