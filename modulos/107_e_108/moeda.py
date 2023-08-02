# Funções

def aumentar(valor, calc):
    num = valor + (valor * calc / 100)
    return num

def diminuir(valor, calc):
    num = valor - (valor * calc / 100) 
    return num
    

def dobro(valor):
    num = valor * 2
    return num

def metade(valor):
    num = valor / 2
    return num

def moeda(valor = 0, moeda = 'R$' ):
    return f'{moeda}{valor}'.replace('.', ',')