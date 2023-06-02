nasc = int(input('Que ano vc nasceu? '))
ano_atual = 2023
idade = ano_atual - nasc
idade_ideal = 18

if idade < 18:
    print(f'ainda falta {idade_ideal-idade} anos pra vc') 

elif idade == 18: 
    print('Vai se alistar irmao')

else: 
    print(f'voce ja passou {idade_ideal-idade} anos do prazo irmao')