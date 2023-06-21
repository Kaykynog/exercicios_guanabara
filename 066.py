n = 0
contador = 0
soma = 0

while n != 999:
    n = int(input('Digite um numero: '))
    soma = soma + n
    contador += 1

print(f'voce digitou {contador} numeros e soma entre eles é {soma - 999}')
