# maioridade = 21 anos

menor = 0
maior = 0
for c in range(0,7):
    ano = int(input('Que ano vc nasceu? '))
    maioriade = 2023 - ano
    if maioriade >= 21:
        maior = maior + 1
    else:
        menor = menor +1

print(f'maior de idade: {maior}\nmenor de idade: {menor}')
    