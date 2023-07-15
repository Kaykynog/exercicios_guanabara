# Exercício Python 084: Faça um programa que leia nome 
# e peso de várias pessoas,                                     
# guardando tudo em uma lista. No final, mostre:                                                                                                    
# A) Quantas pessoas foram cadastradas.                                                                                                               
# B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C) Uma listagem com as pessoas mais leves.

galera = list()
dado = list()
totpessoa = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    galera.append(dado[:])
    dado.clear()
    verifica = str(input('Quer continuar? S/N')).upper().strip()[0]
    totpessoa += 1
    if 'N' in verifica:
        break

print(f'Pessoas cadastradas {totpessoa}')
print(f'o mais pesado foi: {max(galera)}')
print(f'o mais leve foi: {min(galera)}')

