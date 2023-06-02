n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
notas_finais = n1+n2+n3
media = notas_finais / 3

if media < 5:
    print('repetente')
elif media >= 5 and media < 7:
    print('Ta de recuperação irmao')
else:
    print('passou de ano cachorro')