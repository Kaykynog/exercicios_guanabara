num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Segundo numero'))
num3 = int(input('Terceiro numero:'))

if num1 > num2 and num3:
    print(f'{num1} é o maior')
    if num2 > num3:
        print(f'{num3} é o menor')
    else:
        print(f'{num2} é o menor')

if num2 > num1 and num3:
    print(f'{num2} é o maior')
    if num1 > num3:
        print(f'{num3} é o menor')
    else:
        print(f'{num1} é o menor')


if num3 > num2 and num1:
    print(f'{num3} é o maior')
    if num2 > num1:
        print(f'{num1} é o menor')
    else:
        print(f'{num2} é o menor')