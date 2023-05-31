# math.SQRT(x) - Retorna a raiz quadrada de x.
# math.CEIL(x) - Retorna o valor arredondado para cime
# math.FLOOR(x) - Retorna o valor arredondado para baixo


from math import floor, ceil, sqrt, fabs, trunc

num = float(input('numero: '))
raiz = sqrt(num)
arredondando_cima = ceil(num)
arredondando_baixo = floor(num)
absoluto = fabs(num)
truncate = trunc(num)
print(raiz, arredondando_baixo, arredondando_cima, absoluto, truncate)

#Quebrando um numero 
# num = float(input('numero: '))
# num = int()
# print(num)