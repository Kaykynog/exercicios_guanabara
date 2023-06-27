# Exercício Python 071: Crie um programa que simule
#  o funcionamento de um caixa eletrônico. No início,
#  pergunte ao usuário qual será o valor a ser sacado
#  (número inteiro) e o programa vai informar
#  quantas cédulas de cada valor serão entregues.
#  
# OBS:
# considere que o caixa possui cédulas de 
# R$50, R$20, R$10 e R$1.
verificador = 0
cont_50 = cont_20 = cont_10 = cont_1 = 0
saque = int(input('Qual valor você irá sacar: '))

while True:
    verificador += 50
    while saque > verificador:
        cont_50 +=1
        if verificador == saque:
            print(f'Você precisou de {cont_50} notas de 50')

            break
        break

    
        


