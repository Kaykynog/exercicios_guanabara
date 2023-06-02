ano = int(input('Qual ano vc quer saber se é bissexto: '))
if ano%4 == 0 or ano%400 == 0:
    print('é bissexto')
else: 
    print('ano normal')