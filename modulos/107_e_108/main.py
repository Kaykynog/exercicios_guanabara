# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as 
# funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas 
# funções.

# Exercício Python 108: Adapte o código do desafio #107, criando uma 
# função adicional chamada moeda() que consiga mostrar os números 
# como um valor monetário formatado.

import moeda
calc = 0
n = float(input('digite o preço: R$ '))
print(f'Aumentando 10 % -- {moeda.aumentar(n, 10)}')
print(f'Diminuindo 10 % -- {moeda.diminuir(n, 10)}')
print(f'Metade -- {moeda.metade(n)}')
print(f'Dobro % -- {moeda.dobro(n)}')

 