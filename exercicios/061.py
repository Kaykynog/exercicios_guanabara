# programa que le dois valores e realiza operações diversas até o usuario,
# quiser sair

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

while True:
    menu = int(input(
        'Qual será a operação?\n'
        '1 - Soma\n'
        '2 - Multiplicação\n'
        '3 - Maior valor digitado\n'
        '4 - Novos numeros\n'
        '5 - Sair\n'
        '-> '
    ))
    if menu == 1:
        print(f'A soma de {n1} + {n2} é {n1+n2}')
    if menu == 2:
        print(f'A multiplicação de {n1} + {n2} é {n1*n2}')
    if menu == 3:
        if n1 > n2:
            print(f'O maior numero digitado foi {n1}')
        elif n1 == n2:
            print('Os valores são iguais')
        else:
            print(f'O maior numero digitado foi {n2}')
    if menu == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    if menu == 5:
        print('Voce saiu. bye! ')
        break

