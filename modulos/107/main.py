# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as 
# funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas 
# funções.
import moeda
calc = 0
n = int(input('digite um numero: '))
print(f'Aumentando 10 % -- {moeda.aumentar(n, 10)}')
print(f'Diminuindo 10 % -- {moeda.diminuir(n, 10)}')
print(f'Metade -- {moeda.metade(n)}')
print(f'Dobro % -- {moeda.dobro(n)}')
