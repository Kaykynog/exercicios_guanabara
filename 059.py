# Faça um programa que leia o sexo de uma pessoa. mas só aceite os valores "M", 
# ou "F". se estiver errado peça que digite até acertar
sexo = str(input('Qual seu sexo? M/F ?')).strip().upper()[0]
print(sexo)

while sexo not in 'MmFf':
    # sexo = str(input('Qual seu sexo? M/F ?')).upper()
    print('Sexo inválido, digite novamente')
    sexo = str(input('Qual seu sexo? M/F ?')).upper()

print('Anotado!')


   