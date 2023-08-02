# Programa que le um numero e retorna seu fatorial

# # Versão com while
# num = int(input('Digite um numero: '))
# resul = 1
# contador = 1
# while contador <=  num:
#     resul *= contador
#     contador += 1

# print(resul)
    
# Versão com for 

# fat = int(input('Digite um numero: '))
# for fat in  range(fat, fat-1):

# Com a biblioteca math 
from math import factorial
n = int(input('Digite um numero e obtenha seu fatorial: '))
f = factorial(n)
print(f)