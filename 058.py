# Programa que le nome idade e sexo de 4 pessoas
# Retornar : A media de idade do grupo, nome do HOMEM mais velho, 
# quantidade de mulheres com menos de 20 anos
soma_idade = 0 
for p in range(1,5):
    print(f'____ {p}ª PESSOA ____')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F :')).strip()
    soma_idade += idade
media = soma_idade / p
print(f'Media de idades -> {media}')

