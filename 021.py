# lendo angulo e mostrando: Seno, cosseno, tangente 

from math import cos, tan, sin, radians

angulo = float(input('Digite o angulo: ')) 
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O seno é {seno:.2f} cosseno: {cosseno:.2f} tangente: {tangente:.2f}')