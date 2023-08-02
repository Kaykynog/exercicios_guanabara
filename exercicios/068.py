# Programa que jogue par ou impar com a maquina, o jogo só sera interrompido quando o usuario
# perder, mostrando o toal de vitória consecutivas que ele conquistou no no final do jogo
from random import randint
contador = 0    
vitorias = 1

while vitorias != 0:
    computador = randint(0,5)
    usuario = int(input('Digite um numero: [Continuarei pedindo se você ganhar!] -> '))
    par_ou_impar = str(input('Par ou Impar? P/I ')).upper().strip()[0]
    if par_ou_impar in 'P':
        par = computador + usuario
        verifica = par % 2
        if verifica == 0:
            vitorias += 1
        if verifica != 0:
            print(f'Computador: {computador}')
            print(f'Você: {usuario} ')
            print('Deu impar, voce perdeu!')
            break
    if par_ou_impar in 'I':
        impar = computador + usuario
        verifica = impar % 2
        if verifica != 0:
            vitorias += 1
        else:
            print(f'Computador: {computador}')
            print(f'Você: {usuario} ')
            print('Deu par, você perdeu') 
            break
print(f'Você ganhou {vitorias -1} vezes! ')
    
    
    