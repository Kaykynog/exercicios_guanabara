# Exercício Python 097: Faça um programa que tenha uma função 
# chamada escreva(), que receba um texto qualquer como parâmetro 
# e mostre uma mensagem com tamanho adaptável.                                  
# Ex:                                                                                                                                                                        
# escreva(‘Olá, Mundo!’) Saída:                                                                                                                          
# ~~~~~~~~~                                                                                                                                                            
# Olá, Mundo!                                                                                                                                                          
# ~~~~~~~~~      
def escreva(mensagem):
    tamanho = len(mensagem)
    print('~' * tamanho)
    print(f' {mensagem}')
    print('~' * tamanho)

escreva('Kayky Nogueira')


