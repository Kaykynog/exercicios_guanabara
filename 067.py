# Programa que le numeros ate que o usuario nao queira mais
# Quando ele não quiser mais, o programa deve retornar: a media dos numeros lidos
# o meior e o menor numero digitado e perguntar novamente se o usuario quer continuar
# decisao = str(input('Deseja continuar: S/N')).lower()
decisao = 's'
contador = 0
media = 0
number = []
while decisao == 's':
    number.append(float(input('Digite um numero: ')))
    media = media + number
    contador += 1
    decisao = str(input('Deseja continuar: S/N -> ')).lower()
media = media / contador

print(f'A media dos numeros é {media} o maior numero foi{max(number)} e o menor foi {min(number)}')



    

