# Exercicio de Progressao Aritimetica
n = int(input('Qual é o primeiro termo da PA? : '))
r = int(input('Qual é a razão? : '))
for c in range(0,10):
    n = n + r
    print(f'Termos subsequentes: {n}')

