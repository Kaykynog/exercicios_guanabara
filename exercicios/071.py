# Exercício Python 071: Crie um programa que simule
#  o funcionamento de um caixa eletrônico. No início,
#  pergunte ao usuário qual será o valor a ser sacado
#  (número inteiro) e o programa vai informar
#  quantas cédulas de cada valor serão entregues.
#  
# OBS:
# considere que o caixa possui cédulas de 
# R$50, R$20, R$10 e R$1.

verificador = cont_50 = cont_20 = cont_10 = cont_1 = 0
print('=' *45)
print('BEM VINDO AO CAIXA ELETRONICO DO KAYKY')
print('=' *45)
saque = int(input('Qual valor você irá sacar: '))


while True:
    verificador += 50
    cont_50 += 1
    if saque < verificador:
        print(f'Você precisou {cont_50 - 1} notas de 50')
        break

verificador -= 50
while True:
        verificador += 20
        cont_20 += 1
        if saque < verificador:
            print(f'Você precisou de {cont_20 - 1} notas de 20')
            break
verificador -= 20
while True:
        verificador += 10
        cont_10+= 1
        if saque < verificador:
            print(f'Você precisou de {cont_10 - 1} notas de 10')
            break
verificador -= 10
while True:
        verificador += 1
        cont_1 += 1
        if saque < verificador:
            print(f'Você precisou de {cont_1 - 1} notas de 1')
            break

    
        


