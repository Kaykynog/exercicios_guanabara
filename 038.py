

num1 = int(input('Digite o primeira reta: '))
num2 = int(input('Segunda reta: '))
num3 = int(input('Terceira reta: '))

if num1 < num2+num3:
    print('Sim, é um triangulo')

    
elif num2 < num1+num3:
    print('Sim, é um triangulo')


elif num3 < num1+num2:
    print('Sim, é um triangulo')


else:
    print('Não é um triangulo ')
    