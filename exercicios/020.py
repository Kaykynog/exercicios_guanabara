#Resolvendo tringulos retangulos

# Sem a biblioteca math

# cat_op = float(input('Comprimento do cateto oposto: '))
# cat_ad = float(input('Comprimento do cateto adjacente: '))

# hipo = (cat_op **2  + cat_ad**2) ** (1/2)

# print(f'{hipo:.2f}')

# Com a biblioteca math
import math


cat_op = float(input('Comprimento do cateto oposto: '))
cat_ad = float(input('Comprimento do cateto adjacente: '))
hipo = math.hypot(cat_op, cat_ad)
print(hipo)
