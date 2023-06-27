# Programa que le numeros ate que o usuario nao queira mais
# Quando ele não quiser mais, o programa deve retornar: a media dos numeros lidos
# o meior e o menor numero digitado e perguntar novamente se o usuario quer continuar
# decisao = str(input('Deseja continuar: S/N')).lower()

decisao = 's'
contador = 0
media = 0
number = 0
maior = 0
menor = 0
while decisao == 's':
    number = (int(input('Digite um numero: ')))
    media = media + number
    contador += 1
    if contador == 1:
        maior = menor = number
    else:
        if number > maior:
            maior = number
        if number < menor:
            menor = number

    decisao = str(input('Deseja continuar: S/N -> ')).lower().strip()[0]
media = media / contador

print(f'A media dos numeros é {media} o maior numero foi {maior} e o menor foi {menor}')



    

