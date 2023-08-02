# Exercício Python 72: Crie um programa que tenha uma tupla
# totalmente preenchida com uma contagem por extenso, de zero 
# até vinte. Seu programa deverá ler um número pelo 
# teclado (entre 0 e 20) e mostrá-lo por extenso.

numero = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito' , 'Nove', 'Dez', 'Onze','Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete' ,'dezoito', 'Dezenove', 'Vinte')

while True:
    solicitacao = int(input('digite um numero e saiba ele escrito por extenso: '))
    if 0 <= solicitacao <= 20:
        break
    print('Digite um numero entre 0 e 20!!', end= '')
print(numero[solicitacao])