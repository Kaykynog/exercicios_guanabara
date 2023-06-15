# Faça um programa que leia o sexo de uma pessoa. mas só aceite os valores "M", 
# ou "F". se estiver errado peça que digite até acertar

while True:
    sexo = str(input('Qual seu sexo? M/F ?')).upper()

    if sexo in "M" or 'F':
        print('anotado ')
    else:
        print('digita certo cara')


   