# Exercício Python 096: Faça um programa que tenha uma função chamada
# area(), que receba as dimensões de um terreno retangular (largura e 
# comprimento) e mostre a área do terreno.

def area(larg, comp):
    a = larg * comp 
    print(f'A area de um terreno {larg}X{comp} é de {a}m☻')

l = float(input('latgura: '))
c = float(input('comprimento: '))
area(l, c)