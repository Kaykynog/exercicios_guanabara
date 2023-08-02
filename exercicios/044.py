idade = int(input('Qual sua idade: '))

if idade <= 9:
    print('MIRIM')
    
elif idade <= 14 and idade > 9:
    print('INFANTIL')
    
elif idade <= 19 and idade > 14:
    print('JUNIOR')

elif idade <= 20 and idade > 19:
    print('SENIOR')
else: 
    print('MASTER')