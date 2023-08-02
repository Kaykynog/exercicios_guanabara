# VERIFICANDO MAIORIDADE DE 7 PESSOAS
# maioridade = 21 anos


# SOLUÇÃO SEM A BIBLIOTECA DATETIME
# menor = 0
# maior = 0
# for c in range(0,7):
#     ano = int(input('Que ano vc nasceu? '))
#     maioriade = 2023 - ano
#     if maioriade >= 21:
#         maior = maior + 1
#     else:
#         menor = menor +1

# print(f'maior de idade: {maior}\nmenor de idade: {menor}')
    
# COM DATETIME
from datetime import date

ano_atual = date.today().year
tot_maior = 0
tot_menor = 0

for pessoa in range(1,8):
    nasc = int(input('Em que ano você nasceu? '))
    idade = ano_atual - nasc
    if idade >= 21:
        tot_maior += 1
    else:
        tot_menor += 1

print(f'{tot_maior} são maiores de idade, e {tot_menor} são menores')