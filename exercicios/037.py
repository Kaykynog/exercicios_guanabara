salario = float(input('Qual seu salario: '))
if salario > 1250.00:
    ajuste = salario *10 / 100
    print(f'Seu aumento será de {ajuste}')
else:
    ajuste2 = salario *15 / 100
    print(f'Seu aumento será de {ajuste2}')
