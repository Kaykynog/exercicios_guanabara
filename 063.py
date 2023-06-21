# Refazendo o desafio de progressão aritmetica com while

n = int(input('Digite um numero para obter sua PA: '))
r = int(input('Qual é a razão ? '))
count = 0
while True:
    n = n + r 
    count += 1
    print(n)
    if count == 10:
        break