# Programa que le a idade e o sexo de varias pessoas, ate o usuario não quiser mais

verifica = True
masculino = 0
feminino = 0
maioridade = 0
menos_de_20 = 0
while verifica == True:
    print('-'*20)
    print('Cadastre uma pessoa')
    print('-'*20)
    idade = int(input("Qual sua idade? "))
    if idade >= 18:
        maioridade +=1
    sexo = str(input("Qual seu sexo M/F ? ")).upper().strip()[0]
    if sexo in 'Mm':
        masculino += 1
    if sexo in 'Ff':
        feminino =+ 1
        if idade <= 20:
            menos_de_20 += 1
    continua = str(input('Deseja continuar? S/N ')).upper().strip()[0]
    if continua in 'Sn':
        ...
    if continua in 'Nn':
        verifica = False

print(f'Você cadastrou {maioridade} pessoas com mais de 18 anos!')
print(f'Você cadastrou {masculino} homens e {feminino} mulheres!')
print(f'Mulheres com menos de 20: {menos_de_20}')