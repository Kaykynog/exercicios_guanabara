# Aluguel de carros
# preço da diaria é 60
# preço por km rodado é 0.15

km = float(input('Quanto vc rodou? '))
dias = float(input('Por quantos dias? '))

dias_calc = 60 * dias
km_calc =  km * 0.15
valor_total = dias_calc + km_calc

print(f'Valor total = {valor_total}')