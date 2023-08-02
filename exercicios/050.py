# Somando numeros impares multiplos de 3 entre 0 e  500
soma = 0
for c in range(0,500):
    if c % 2 != 0:
        print(f'Numero impar {c}')
        if c % 3 == 0:
            soma = soma + c
print(soma)

